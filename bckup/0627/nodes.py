from config import *
import logging
from node import *
from grid import *

class Nodes(list):
  """This class stores a list with all network nodes plus the base sta-
  tion. Its methods ensure the network behavior.
  """
  def __init__(self, init_nodes=None):
    logging.debug('Instantiating nodes...')
    if init_nodes:
      self.extend(init_nodes)
    else:
      nodes = [Node(i, self) for i in range(0,NB_NODES)]
      self.extend(nodes)
      # last node in nodes is the base station
      base_station = Node(BSID, self)
      base_station.pos_x = BS_POS_X
      base_station.pos_y = BS_POS_Y
      self.append(base_station)

    self.initial_energy = self.get_remaining_energy()

  def run_round(self):
    """Run one round. Every node captures using its sensor. Then this
    information is forwarded through the intermediary nodes to the base
    station.
    """
    for i in range(0, MAX_TX_PER_ROUND):
      self._sensing_phase()
      self._communication_phase()

  def _sensing_phase(self):
    """Every alive node captures information using its sensor."""
    for node in self.get_alive_nodes():
      node.sense()

  def _communication_phase(self):
    """Each node transmits respecting its hierarchy: leaves start the 
    communication, then cluster heads forward the messages, until all
    messages reach the base station. This method works for any hierar-
    chy (even for LEACH).
    """
    ordinary_nodes = self.get_ordinary_nodes()
    heads = self.get_ch_nodes()
    msg = str("%d ordinary nodes, %d heads." % (len(ordinary_nodes), len(heads)))
    logging.debug("Hierarchical communication: %s" % (msg))

    alive_nodes = self.get_alive_nodes()
    self._recursive_comm(alive_nodes)

  def _recursive_comm(self, alive_nodes):
    """Hierarchical communication using recursivity. This method suppo-
    ses that there is no cycle in the network (network is a tree).
    Otherwise, expect infinite loop.
    """
    # TODO store communication order and reuse it instead of calling
    # this function always
    next_alive_nodes = alive_nodes[:]
    for node in alive_nodes:
      #check if other nodes must send info to this node
      depends_on_other_node = 0
      for other_node in alive_nodes:
        #if other_node == node:
        #  continue
        if other_node.next_hop == node.id:
          depends_on_other_node = 1
          break

      if not depends_on_other_node:
        node.transmit()
        next_alive_nodes = [n for n in next_alive_nodes if n != node]

    if len(next_alive_nodes) == 0:
      return
    else:
      self._recursive_comm(next_alive_nodes)

  def get_alive_nodes(self):
    """Return nodes that have positive remaining energy."""
    return [node for node in self[0:-1] if node.alive]

  def get_active_nodes(self):
    """Return nodes that have positive remaining energy and that are
    awake."""
    is_active = lambda x: x.alive and not x.is_sleeping
    return [node for node in self[0:-1] if is_active(node)]

  def get_ordinary_nodes(self):
    return [node for node in self if node.is_ordinary_node() and node.alive]

  def get_ch_nodes(self, only_alives=1):
    input_set = self.get_alive_nodes() if only_alives else self
    return [node for node in input_set if node.is_cluster_head()]

  def someone_alive(self):
    """Finds if there is at least one node alive. It excludes the base station,
       which is supposed to be always alive."""
    for node in self[0:-1]:
      if node.alive == 1:
        return 1
    return 0

  def count_alive_nodes(self):
    count = 0
    for node in self:
      if node.alive == 1:
        count += 1
    return count

  def get_BS(self):
    # intention: make code clearer for non-Python readers
    return self[-1]

  def notify_position(self):
    """Every node transmit its position directly to the base station."""
    for node in self.get_alive_nodes():
      node.transmit(msg_length=MSG_LENGTH, destination=self.get_BS())

  def broadcast_next_hop(self):
    """Base station informs nodes about their next hop."""
    base_station = self.get_BS()
    for node in self.get_alive_nodes():
      base_station.transmit(msg_length=MSG_LENGTH, destination=node)

  def get_nodes_by_membership(self, membership, only_alives=1):
    """Returns all nodes that belong to this membership/cluster."""
    input_set = self.get_alive_nodes() if only_alives else self
    condition = lambda node: node.membership == membership
    return [node for node in input_set if condition(node)]

  def get_remaining_energy(self, ignore_nodes=None):
    """Returns the sum of the remaining energies at all nodes."""
    set = self.get_alive_nodes()
    if len(set) == 0:
      return 0
    if ignore_nodes:
      set = [node for node in set if node not in ignore_nodes]
    transform = lambda x: x.energy_source.energy
    energies = [transform(x) for x in set]
    return reduce(lambda x, y: x+y, energies)

  def set_zero_cost_aggregation(self, value):
    """Sets the zero_cost_aggregation property for all nodes."""
    for node in self:
      node.zero_cost_aggregation = value
    
  def _calculate_nb_neighbors(self, target_node, coverage_radius):
    """Calculate the number of neighbors given the sensor coverage
    radius.
    """
    # if number of neighbors was calculated at least once
    # skips calculating the distance
    if target_node.nb_neighbors != -1:
      # only check if there are dead nodes
      nb_neighbors = target_node.nb_neighbors
      for idx, neighbor in enumerate(target_node.neighbors):
        if not neighbor.alive:
          nb_neighbors -= 1
          del target_node.neighbors[idx]
      return nb_neighbors

    nb_neighbors = 0
    for node in self.get_alive_nodes():
      if node != target_node:
        distance = calculate_distance(target_node, node)
        if distance <= coverage_radius:
          nb_neighbors += 1
          target_node.neighbors.append(node) 
    return nb_neighbors

  def split_in_clusters(self, nb_clusters=LEACH_NB_CLUSTERS):
    """Split this nodes object into other nodes objects that contain only
    information about a single cluster."""
    # TODO: add BS as last element to keep compatibility between node 
    # and cluster
    clusters = []
    for cluster_idx in range(0, nb_clusters):
      nodes = self.get_nodes_by_membership(cluster_idx)
      cluster = Nodes(init_nodes=nodes)
      clusters.append(cluster)
    return clusters

  def calculate_sleep_prob(self):
    for node in self:
      nb_neighbors = self._calculate_nb_neighbors(node, COVERAGE_RADIUS)
      # only update if something changed (to speed up simulation)
      if nb_neighbors != node.nb_neighbors:
        node.nb_neighbors = nb_neighbors
        node.calculate_sleep_prob(nb_neighbors)

  def paint_grid(self):
    # in order to calculate the coverage/overlapping of multiple over-
    # lapping circles, we use a numeric approach instead of an analyti-
    # cal one. We first draw the coverages of all nodes in a grid with
    # N points, then we can sum the area related to each point to get
    # the coverage and overlapping areas
    if not hasattr(self, 'regions'): # first time here
      grid = Grid()
      for node in self[0:-1]:
        grid.add_node(node, COVERAGE_RADIUS)

    # since we must calculate the coverage/overlapping area in absence
    # of some nodes (fitness function), we will not use the grid itself
    # but rather an optimized structure that contain regions on the map
    # covered by unique distributions of nodes/owners
    # these regions are saved in each nodes instance in order to be
    # reused without the need of repainting the grid (which is costly).
      self.regions = Regions(grid)

  def get_network_coverage(self, ignore_nodes):
    """Just a wrapper method to access Regions method."""
    return self.regions.get_network_coverage(ignore_nodes)

  def get_network_overlapping(self, ignore_nodes):
    """Just a wrapper method to access Regions method."""
    return self.regions.get_network_overlapping(ignore_nodes)

  def get_both(self, ignore_nodes):
    """Just a wrapper method to access Regions method."""
    return self.regions.get_both(ignore_nodes)


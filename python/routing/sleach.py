import logging, sys
import config as cf
import simpy
from python.network.network import * 
from python.network.node import * 
from python.routing.routing_protocol import * 


class SLEACH(RoutingProtocol):


  def setup_phase(self, network, round_nb=None):
    """The base station decides which nodes   are cluster heads in this
    round, depending on a probability. Then it broadcasts this information
    to all network.
    Reference:
      W. Heinzelman, A. Chandrakasan, and H. Balakrishnan, Energy-
      efficient communication protocols for wireless sensor networks, In
      Proceedings of the 33rd Annual Hawaii International Conference on
      System Sciences (HICSS), Hawaii, USA, January 2000.
    """
    logging.info('SLEACH: Setup phase - Configuration procedure.')#novo
    # data structures are populated (100 nodes) - node(NodeId, sts, srs)
    node1 = (1, 'Light', 100)
    print(node1)
    node2 = (2, 'Humidity', 100)
    print(node2)
    node3 = (3, 'Temperature', 100) 
    print(node3)
    node4 = (4, 'Voltage', 10)
    print(node4)
  
    logging.info('SLEACH: setup phase - Select role.')
    # decide which network are cluster heads
    prob_ch = float(cf.NB_CLUSTERS)/float(cf.NB_NODES)
    
    heads = []
    #clusters = network.clusters #novo
    alive_nodes = network.get_alive_nodes()
    logging.info('SLEACH: setup phase - cluster formation - deciding which nodes are cluster heads.')
    idx = 00
    while len(heads) != cf.NB_CLUSTERS:
      node = alive_nodes[idx]
      u_random = np.random.uniform(0, 1)
      # node will be a cluster head
      if u_random < prob_ch:
        node.next_hop = cf.BSID

        heads.append(node)
       
      idx = idx+1 if idx < len(alive_nodes)-1 else 0
  
    # ordinary network choose nearest cluster heads
    logging.info('SLEACH: setup phase - ordinary nodes choose nearest cluster head')
    for node in alive_nodes:
      if node in heads: # node is cluster head
        continue
      nearest_head = heads[0]

          
      # find the nearest cluster head
      for head in heads[1:]:
        if calculate_distance(node, nearest_head) > calculate_distance(node, head):
          nearest_head = head
  
      node.next_hop = nearest_head.id
  
    network.broadcast_next_hop()

    logging.info('SLEACH: awareness phase')#novo 
   
    
    app1 = (1, 'Light', 100)
    print(app1)
    app2 = (2, 'Humidity', 100)
    print(app2)
    app3 = (3, 'Temperature', 100) 
    print(app3)
    app4 = (4, 'Voltage', 10)
    print(app4)
 
    logging.info('SLEACH: steady state phase')#novo
    
    print(" Coletar dados  ou Usar dados do dataset")
    

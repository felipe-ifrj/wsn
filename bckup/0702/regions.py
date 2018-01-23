# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_regions', [dirname(__file__)])
        except ImportError:
            import _regions
            return _regions
        if fp is not None:
            try:
                _mod = imp.load_module('_regions', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _regions = swig_import_helper()
    del swig_import_helper
else:
    import _regions
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _regions.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _regions.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _regions.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _regions.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _regions.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _regions.SwigPyIterator_equal(self, x)

    def copy(self):
        return _regions.SwigPyIterator_copy(self)

    def next(self):
        return _regions.SwigPyIterator_next(self)

    def __next__(self):
        return _regions.SwigPyIterator___next__(self)

    def previous(self):
        return _regions.SwigPyIterator_previous(self)

    def advance(self, n):
        return _regions.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _regions.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _regions.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _regions.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _regions.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _regions.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _regions.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _regions.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vector0(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector0, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector0, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _regions.vector0_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _regions.vector0___nonzero__(self)

    def __bool__(self):
        return _regions.vector0___bool__(self)

    def __len__(self):
        return _regions.vector0___len__(self)

    def __getslice__(self, i, j):
        return _regions.vector0___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _regions.vector0___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _regions.vector0___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _regions.vector0___delitem__(self, *args)

    def __getitem__(self, *args):
        return _regions.vector0___getitem__(self, *args)

    def __setitem__(self, *args):
        return _regions.vector0___setitem__(self, *args)

    def pop(self):
        return _regions.vector0_pop(self)

    def append(self, x):
        return _regions.vector0_append(self, x)

    def empty(self):
        return _regions.vector0_empty(self)

    def size(self):
        return _regions.vector0_size(self)

    def swap(self, v):
        return _regions.vector0_swap(self, v)

    def begin(self):
        return _regions.vector0_begin(self)

    def end(self):
        return _regions.vector0_end(self)

    def rbegin(self):
        return _regions.vector0_rbegin(self)

    def rend(self):
        return _regions.vector0_rend(self)

    def clear(self):
        return _regions.vector0_clear(self)

    def get_allocator(self):
        return _regions.vector0_get_allocator(self)

    def pop_back(self):
        return _regions.vector0_pop_back(self)

    def erase(self, *args):
        return _regions.vector0_erase(self, *args)

    def __init__(self, *args):
        this = _regions.new_vector0(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _regions.vector0_push_back(self, x)

    def front(self):
        return _regions.vector0_front(self)

    def back(self):
        return _regions.vector0_back(self)

    def assign(self, n, x):
        return _regions.vector0_assign(self, n, x)

    def resize(self, *args):
        return _regions.vector0_resize(self, *args)

    def insert(self, *args):
        return _regions.vector0_insert(self, *args)

    def reserve(self, n):
        return _regions.vector0_reserve(self, n)

    def capacity(self):
        return _regions.vector0_capacity(self)
    __swig_destroy__ = _regions.delete_vector0
    __del__ = lambda self: None
vector0_swigregister = _regions.vector0_swigregister
vector0_swigregister(vector0)

class vector1(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector1, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector1, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _regions.vector1_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _regions.vector1___nonzero__(self)

    def __bool__(self):
        return _regions.vector1___bool__(self)

    def __len__(self):
        return _regions.vector1___len__(self)

    def __getslice__(self, i, j):
        return _regions.vector1___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _regions.vector1___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _regions.vector1___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _regions.vector1___delitem__(self, *args)

    def __getitem__(self, *args):
        return _regions.vector1___getitem__(self, *args)

    def __setitem__(self, *args):
        return _regions.vector1___setitem__(self, *args)

    def pop(self):
        return _regions.vector1_pop(self)

    def append(self, x):
        return _regions.vector1_append(self, x)

    def empty(self):
        return _regions.vector1_empty(self)

    def size(self):
        return _regions.vector1_size(self)

    def swap(self, v):
        return _regions.vector1_swap(self, v)

    def begin(self):
        return _regions.vector1_begin(self)

    def end(self):
        return _regions.vector1_end(self)

    def rbegin(self):
        return _regions.vector1_rbegin(self)

    def rend(self):
        return _regions.vector1_rend(self)

    def clear(self):
        return _regions.vector1_clear(self)

    def get_allocator(self):
        return _regions.vector1_get_allocator(self)

    def pop_back(self):
        return _regions.vector1_pop_back(self)

    def erase(self, *args):
        return _regions.vector1_erase(self, *args)

    def __init__(self, *args):
        this = _regions.new_vector1(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _regions.vector1_push_back(self, x)

    def front(self):
        return _regions.vector1_front(self)

    def back(self):
        return _regions.vector1_back(self)

    def assign(self, n, x):
        return _regions.vector1_assign(self, n, x)

    def resize(self, *args):
        return _regions.vector1_resize(self, *args)

    def insert(self, *args):
        return _regions.vector1_insert(self, *args)

    def reserve(self, n):
        return _regions.vector1_reserve(self, n)

    def capacity(self):
        return _regions.vector1_capacity(self)
    __swig_destroy__ = _regions.delete_vector1
    __del__ = lambda self: None
vector1_swigregister = _regions.vector1_swigregister
vector1_swigregister(vector1)

class map0(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map0, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map0, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _regions.map0_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _regions.map0___nonzero__(self)

    def __bool__(self):
        return _regions.map0___bool__(self)

    def __len__(self):
        return _regions.map0___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _regions.map0___getitem__(self, key)

    def __delitem__(self, key):
        return _regions.map0___delitem__(self, key)

    def has_key(self, key):
        return _regions.map0_has_key(self, key)

    def keys(self):
        return _regions.map0_keys(self)

    def values(self):
        return _regions.map0_values(self)

    def items(self):
        return _regions.map0_items(self)

    def __contains__(self, key):
        return _regions.map0___contains__(self, key)

    def key_iterator(self):
        return _regions.map0_key_iterator(self)

    def value_iterator(self):
        return _regions.map0_value_iterator(self)

    def __setitem__(self, *args):
        return _regions.map0___setitem__(self, *args)

    def asdict(self):
        return _regions.map0_asdict(self)

    def __init__(self, *args):
        this = _regions.new_map0(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def empty(self):
        return _regions.map0_empty(self)

    def size(self):
        return _regions.map0_size(self)

    def swap(self, v):
        return _regions.map0_swap(self, v)

    def begin(self):
        return _regions.map0_begin(self)

    def end(self):
        return _regions.map0_end(self)

    def rbegin(self):
        return _regions.map0_rbegin(self)

    def rend(self):
        return _regions.map0_rend(self)

    def clear(self):
        return _regions.map0_clear(self)

    def get_allocator(self):
        return _regions.map0_get_allocator(self)

    def count(self, x):
        return _regions.map0_count(self, x)

    def erase(self, *args):
        return _regions.map0_erase(self, *args)

    def find(self, x):
        return _regions.map0_find(self, x)

    def lower_bound(self, x):
        return _regions.map0_lower_bound(self, x)

    def upper_bound(self, x):
        return _regions.map0_upper_bound(self, x)
    __swig_destroy__ = _regions.delete_map0
    __del__ = lambda self: None
map0_swigregister = _regions.map0_swigregister
map0_swigregister(map0)

class Regions(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Regions, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Regions, name)
    __repr__ = _swig_repr

    def __init__(self, _exclusive, _overlapping):
        this = _regions.new_Regions(_exclusive, _overlapping)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _regions.delete_Regions
    __del__ = lambda self: None

    def test(self):
        return _regions.Regions_test(self)

    def get_all(self, ignore_nodes):
        return _regions.Regions_get_all(self, ignore_nodes)
Regions_swigregister = _regions.Regions_swigregister
Regions_swigregister(Regions)

# This file is compatible with both classic and new-style classes.



# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_visilibity', [dirname(__file__)])
        except ImportError:
            import _visilibity
            return _visilibity
        if fp is not None:
            try:
                _mod = imp.load_module('_visilibity', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _visilibity = swig_import_helper()
    del swig_import_helper
else:
    import _visilibity
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _visilibity.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _visilibity.SwigPyIterator_value(self)
    def incr(self, n = 1): return _visilibity.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _visilibity.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _visilibity.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _visilibity.SwigPyIterator_equal(self, *args)
    def copy(self): return _visilibity.SwigPyIterator_copy(self)
    def next(self): return _visilibity.SwigPyIterator_next(self)
    def __next__(self): return _visilibity.SwigPyIterator___next__(self)
    def previous(self): return _visilibity.SwigPyIterator_previous(self)
    def advance(self, *args): return _visilibity.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _visilibity.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _visilibity.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _visilibity.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _visilibity.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _visilibity.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _visilibity.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _visilibity.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class pointList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pointList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pointList, name)
    __repr__ = _swig_repr
    def iterator(self): return _visilibity.pointList_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _visilibity.pointList___nonzero__(self)
    def __bool__(self): return _visilibity.pointList___bool__(self)
    def __len__(self): return _visilibity.pointList___len__(self)
    def pop(self): return _visilibity.pointList_pop(self)
    def __getslice__(self, *args): return _visilibity.pointList___getslice__(self, *args)
    def __setslice__(self, *args): return _visilibity.pointList___setslice__(self, *args)
    def __delslice__(self, *args): return _visilibity.pointList___delslice__(self, *args)
    def __delitem__(self, *args): return _visilibity.pointList___delitem__(self, *args)
    def __getitem__(self, *args): return _visilibity.pointList___getitem__(self, *args)
    def __setitem__(self, *args): return _visilibity.pointList___setitem__(self, *args)
    def append(self, *args): return _visilibity.pointList_append(self, *args)
    def empty(self): return _visilibity.pointList_empty(self)
    def size(self): return _visilibity.pointList_size(self)
    def clear(self): return _visilibity.pointList_clear(self)
    def swap(self, *args): return _visilibity.pointList_swap(self, *args)
    def get_allocator(self): return _visilibity.pointList_get_allocator(self)
    def begin(self): return _visilibity.pointList_begin(self)
    def end(self): return _visilibity.pointList_end(self)
    def rbegin(self): return _visilibity.pointList_rbegin(self)
    def rend(self): return _visilibity.pointList_rend(self)
    def pop_back(self): return _visilibity.pointList_pop_back(self)
    def erase(self, *args): return _visilibity.pointList_erase(self, *args)
    def __init__(self, *args): 
        this = _visilibity.new_pointList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _visilibity.pointList_push_back(self, *args)
    def front(self): return _visilibity.pointList_front(self)
    def back(self): return _visilibity.pointList_back(self)
    def assign(self, *args): return _visilibity.pointList_assign(self, *args)
    def resize(self, *args): return _visilibity.pointList_resize(self, *args)
    def insert(self, *args): return _visilibity.pointList_insert(self, *args)
    def reserve(self, *args): return _visilibity.pointList_reserve(self, *args)
    def capacity(self): return _visilibity.pointList_capacity(self)
    __swig_destroy__ = _visilibity.delete_pointList
    __del__ = lambda self : None;
pointList_swigregister = _visilibity.pointList_swigregister
pointList_swigregister(pointList)

class polygonList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, polygonList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, polygonList, name)
    __repr__ = _swig_repr
    def iterator(self): return _visilibity.polygonList_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _visilibity.polygonList___nonzero__(self)
    def __bool__(self): return _visilibity.polygonList___bool__(self)
    def __len__(self): return _visilibity.polygonList___len__(self)
    def pop(self): return _visilibity.polygonList_pop(self)
    def __getslice__(self, *args): return _visilibity.polygonList___getslice__(self, *args)
    def __setslice__(self, *args): return _visilibity.polygonList___setslice__(self, *args)
    def __delslice__(self, *args): return _visilibity.polygonList___delslice__(self, *args)
    def __delitem__(self, *args): return _visilibity.polygonList___delitem__(self, *args)
    def __getitem__(self, *args): return _visilibity.polygonList___getitem__(self, *args)
    def __setitem__(self, *args): return _visilibity.polygonList___setitem__(self, *args)
    def append(self, *args): return _visilibity.polygonList_append(self, *args)
    def empty(self): return _visilibity.polygonList_empty(self)
    def size(self): return _visilibity.polygonList_size(self)
    def clear(self): return _visilibity.polygonList_clear(self)
    def swap(self, *args): return _visilibity.polygonList_swap(self, *args)
    def get_allocator(self): return _visilibity.polygonList_get_allocator(self)
    def begin(self): return _visilibity.polygonList_begin(self)
    def end(self): return _visilibity.polygonList_end(self)
    def rbegin(self): return _visilibity.polygonList_rbegin(self)
    def rend(self): return _visilibity.polygonList_rend(self)
    def pop_back(self): return _visilibity.polygonList_pop_back(self)
    def erase(self, *args): return _visilibity.polygonList_erase(self, *args)
    def __init__(self, *args): 
        this = _visilibity.new_polygonList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _visilibity.polygonList_push_back(self, *args)
    def front(self): return _visilibity.polygonList_front(self)
    def back(self): return _visilibity.polygonList_back(self)
    def assign(self, *args): return _visilibity.polygonList_assign(self, *args)
    def resize(self, *args): return _visilibity.polygonList_resize(self, *args)
    def insert(self, *args): return _visilibity.polygonList_insert(self, *args)
    def reserve(self, *args): return _visilibity.polygonList_reserve(self, *args)
    def capacity(self): return _visilibity.polygonList_capacity(self)
    __swig_destroy__ = _visilibity.delete_polygonList
    __del__ = lambda self : None;
polygonList_swigregister = _visilibity.polygonList_swigregister
polygonList_swigregister(polygonList)


def uniform_random_sample(*args):
  return _visilibity.uniform_random_sample(*args)
uniform_random_sample = _visilibity.uniform_random_sample
class Bounding_Box(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Bounding_Box, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Bounding_Box, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x_min"] = _visilibity.Bounding_Box_x_min_set
    __swig_getmethods__["x_min"] = _visilibity.Bounding_Box_x_min_get
    if _newclass:x_min = _swig_property(_visilibity.Bounding_Box_x_min_get, _visilibity.Bounding_Box_x_min_set)
    __swig_setmethods__["x_max"] = _visilibity.Bounding_Box_x_max_set
    __swig_getmethods__["x_max"] = _visilibity.Bounding_Box_x_max_get
    if _newclass:x_max = _swig_property(_visilibity.Bounding_Box_x_max_get, _visilibity.Bounding_Box_x_max_set)
    __swig_setmethods__["y_min"] = _visilibity.Bounding_Box_y_min_set
    __swig_getmethods__["y_min"] = _visilibity.Bounding_Box_y_min_get
    if _newclass:y_min = _swig_property(_visilibity.Bounding_Box_y_min_get, _visilibity.Bounding_Box_y_min_set)
    __swig_setmethods__["y_max"] = _visilibity.Bounding_Box_y_max_set
    __swig_getmethods__["y_max"] = _visilibity.Bounding_Box_y_max_get
    if _newclass:y_max = _swig_property(_visilibity.Bounding_Box_y_max_get, _visilibity.Bounding_Box_y_max_set)
    def __init__(self): 
        this = _visilibity.new_Bounding_Box()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _visilibity.delete_Bounding_Box
    __del__ = lambda self : None;
Bounding_Box_swigregister = _visilibity.Bounding_Box_swigregister
Bounding_Box_swigregister(Bounding_Box)
cvar = _visilibity.cvar
FIOS_PRECISION = cvar.FIOS_PRECISION

class Point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Point(*args)
        try: self.this.append(this)
        except: self.this = this
        
    #userFriendly :)
    def __getattr__(self, attribut):
        if attribut == "x":
            return self.get_x()
        elif attribut == "y":
            return self.get_y()
            
    def __setattr__(self, attribut, value):
        if attribut == "x":
            self.set_x(value)
        elif attribut == "y":
            self.set_y(value)
        else:
            self.__dict__[attribut] = value
        
    def __str__(self):
        return "("+str(self.get_x())+", "+str(self.get_y())+")"
        
    def __eq__(self,other):
        return (self.get_x() == other.x and self.get_y() == other.y)
    
    def get_x(self, *args): return _visilibity.Point_x(self)
    def get_y(self, *args): return _visilibity.Point_y(self)
    def set_x(self, *args): return _visilibity.Point_set_x(self, *args)
    def set_y(self, *args): return _visilibity.Point_set_y(self, *args)
    
    def projection_onto(self, *args): return _visilibity.Point_projection_onto(self, *args)
    def projection_onto_vertices_of(self, *args): return _visilibity.Point_projection_onto_vertices_of(self, *args)
    def projection_onto_boundary_of(self, *args): return _visilibity.Point_projection_onto_boundary_of(self, *args)
    def on_boundary_of(self, *args): return _visilibity.Point_on_boundary_of(self, *args)
    def in_relative_interior_of(self, *args): return _visilibity.Point_in_relative_interior_of(self, *args)
    def _in(self, *args): return _visilibity.Point__in(self, *args)
    def is_endpoint_of(self, *args): return _visilibity.Point_is_endpoint_of(self, *args)
    def snap_to_vertices_of(self, *args): return _visilibity.Point_snap_to_vertices_of(self, *args)
    def snap_to_boundary_of(self, *args): return _visilibity.Point_snap_to_boundary_of(self, *args)
    __swig_destroy__ = _visilibity.delete_Point
    __del__ = lambda self : None;
Point_swigregister = _visilibity.Point_swigregister
Point_swigregister(Point)


def cross(*args):
  return _visilibity.cross(*args)
cross = _visilibity.cross
class Line_Segment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Line_Segment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Line_Segment, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Line_Segment(*args)
        try: self.this.append(this)
        except: self.this = this
    def first(self): return _visilibity.Line_Segment_first(self)
    def second(self): return _visilibity.Line_Segment_second(self)
    def size(self): return _visilibity.Line_Segment_size(self)
    def midpoint(self): return _visilibity.Line_Segment_midpoint(self)
    def length(self): return _visilibity.Line_Segment_length(self)
    def is_in_standard_form(self): return _visilibity.Line_Segment_is_in_standard_form(self)
    def set_first(self, *args): return _visilibity.Line_Segment_set_first(self, *args)
    def set_second(self, *args): return _visilibity.Line_Segment_set_second(self, *args)
    def reverse(self): return _visilibity.Line_Segment_reverse(self)
    def enforce_standard_form(self): return _visilibity.Line_Segment_enforce_standard_form(self)
    def clear(self): return _visilibity.Line_Segment_clear(self)
    __swig_destroy__ = _visilibity.delete_Line_Segment
    __del__ = lambda self : None;
Line_Segment_swigregister = _visilibity.Line_Segment_swigregister
Line_Segment_swigregister(Line_Segment)

def __mul__(*args):
  return _visilibity.__mul__(*args)
__mul__ = _visilibity.__mul__

class Angle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Angle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Angle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Angle(*args)
        try: self.this.append(this)
        except: self.this = this
    def get(self): return _visilibity.Angle_get(self)
    def set(self, *args): return _visilibity.Angle_set(self, *args)
    def set_to_2pi(self): return _visilibity.Angle_set_to_2pi(self)
    def randomize(self): return _visilibity.Angle_randomize(self)
    __swig_destroy__ = _visilibity.delete_Angle
    __del__ = lambda self : None;
Angle_swigregister = _visilibity.Angle_swigregister
Angle_swigregister(Angle)

def distance(*args):
  return _visilibity.distance(*args)
distance = _visilibity.distance

def intersect(*args):
  return _visilibity.intersect(*args)
intersect = _visilibity.intersect

def intersect_proper(*args):
  return _visilibity.intersect_proper(*args)
intersect_proper = _visilibity.intersect_proper


def geodesic_distance(*args):
  return _visilibity.geodesic_distance(*args)
geodesic_distance = _visilibity.geodesic_distance

def geodesic_direction(*args):
  return _visilibity.geodesic_direction(*args)
geodesic_direction = _visilibity.geodesic_direction
class Polar_Point(Point):
    __swig_setmethods__ = {}
    for _s in [Point]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Polar_Point, name, value)
    __swig_getmethods__ = {}
    for _s in [Point]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Polar_Point, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Polar_Point(*args)
        try: self.this.append(this)
        except: self.this = this
    def polar_origin(self): return _visilibity.Polar_Point_polar_origin(self)
    def range(self): return _visilibity.Polar_Point_range(self)
    def bearing(self): return _visilibity.Polar_Point_bearing(self)
    def set_polar_origin(self, *args): return _visilibity.Polar_Point_set_polar_origin(self, *args)
    def set_x(self, *args): return _visilibity.Polar_Point_set_x(self, *args)
    def set_y(self, *args): return _visilibity.Polar_Point_set_y(self, *args)
    def set_range(self, *args): return _visilibity.Polar_Point_set_range(self, *args)
    def set_bearing(self, *args): return _visilibity.Polar_Point_set_bearing(self, *args)
    def set_bearing_to_2pi(self): return _visilibity.Polar_Point_set_bearing_to_2pi(self)
    __swig_destroy__ = _visilibity.delete_Polar_Point
    __del__ = lambda self : None;
Polar_Point_swigregister = _visilibity.Polar_Point_swigregister
Polar_Point_swigregister(Polar_Point)

def __add__(*args):
  return _visilibity.__add__(*args)
__add__ = _visilibity.__add__

def __sub__(*args):
  return _visilibity.__sub__(*args)
__sub__ = _visilibity.__sub__

class Ray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Ray(*args)
        try: self.this.append(this)
        except: self.this = this
    def base_point(self): return _visilibity.Ray_base_point(self)
    def bearing(self): return _visilibity.Ray_bearing(self)
    def set_base_point(self, *args): return _visilibity.Ray_set_base_point(self, *args)
    def set_bearing(self, *args): return _visilibity.Ray_set_bearing(self, *args)
    __swig_destroy__ = _visilibity.delete_Ray
    __del__ = lambda self : None;
Ray_swigregister = _visilibity.Ray_swigregister
Ray_swigregister(Ray)

def __gt__(*args):
  return _visilibity.__gt__(*args)
__gt__ = _visilibity.__gt__

def __lt__(*args):
  return _visilibity.__lt__(*args)
__lt__ = _visilibity.__lt__

def __ge__(*args):
  return _visilibity.__ge__(*args)
__ge__ = _visilibity.__ge__

def __le__(*args):
  return _visilibity.__le__(*args)
__le__ = _visilibity.__le__

class Polyline(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Polyline, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Polyline, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Polyline(*args)
        try: self.this.append(this)
        except: self.this = this
        
    #userfriendly :)
    def __getitem__(self,key):
        return self.get_Point(key)
        
    def get_Point(self, *args): return _visilibity.Polyline_get_Point(self, *args)
    def size(self): return _visilibity.Polyline_size(self)
    def length(self): return _visilibity.Polyline_length(self)
    def diameter(self): return _visilibity.Polyline_diameter(self)
    def bbox(self): return _visilibity.Polyline_bbox(self)
    def clear(self): return _visilibity.Polyline_clear(self)
    def push_back(self, *args): return _visilibity.Polyline_push_back(self, *args)
    def pop_back(self): return _visilibity.Polyline_pop_back(self)
    def set_vertices(self, *args): return _visilibity.Polyline_set_vertices(self, *args)
    def eliminate_redundant_vertices(self, epsilon = 0.0): return _visilibity.Polyline_eliminate_redundant_vertices(self, epsilon)
    def reverse(self): return _visilibity.Polyline_reverse(self)
    def append(self, *args): return _visilibity.Polyline_append(self, *args)
    __swig_destroy__ = _visilibity.delete_Polyline
    __del__ = lambda self : None;
Polyline_swigregister = _visilibity.Polyline_swigregister
Polyline_swigregister(Polyline)

def intersection(*args):
  return _visilibity.intersection(*args)
intersection = _visilibity.intersection

class Polygon(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Polygon, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Polygon, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Polygon(*args)
        try: self.this.append(this)
        except: self.this = this
    def n(self): return _visilibity.Polygon_n(self)
    def r(self): return _visilibity.Polygon_r(self)
    def is_simple(self, epsilon = 0.0): return _visilibity.Polygon_is_simple(self, epsilon)
    def is_in_standard_form(self): return _visilibity.Polygon_is_in_standard_form(self)
    def boundary_length(self): return _visilibity.Polygon_boundary_length(self)
    def area(self): return _visilibity.Polygon_area(self)
    def centroid(self): return _visilibity.Polygon_centroid(self)
    def diameter(self): return _visilibity.Polygon_diameter(self)
    def bbox(self): return _visilibity.Polygon_bbox(self)
    def random_points(self, *args): return _visilibity.Polygon_random_points(self, *args)
    def write_to_file(self, *args): return _visilibity.Polygon_write_to_file(self, *args)
    def set_vertices(self, *args): return _visilibity.Polygon_set_vertices(self, *args)
    def push_back(self, *args): return _visilibity.Polygon_push_back(self, *args)
    def clear(self): return _visilibity.Polygon_clear(self)
    def enforce_standard_form(self): return _visilibity.Polygon_enforce_standard_form(self)
    def eliminate_redundant_vertices(self, epsilon = 0.0): return _visilibity.Polygon_eliminate_redundant_vertices(self, epsilon)
    def reverse(self): return _visilibity.Polygon_reverse(self)
    def __getitem__(self, *args): return _visilibity.Polygon___getitem__(self, *args)
    __swig_destroy__ = _visilibity.delete_Polygon
    __del__ = lambda self : None;
Polygon_swigregister = _visilibity.Polygon_swigregister
Polygon_swigregister(Polygon)

class Environment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Environment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Environment, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Environment(*args)
        try: self.this.append(this)
        except: self.this = this
    def h(self): return _visilibity.Environment_h(self)
    def n(self): return _visilibity.Environment_n(self)
    def r(self): return _visilibity.Environment_r(self)
    def is_in_standard_form(self): return _visilibity.Environment_is_in_standard_form(self)
    def is_valid(self, epsilon = 0.0): return _visilibity.Environment_is_valid(self, epsilon)
    def boundary_length(self): return _visilibity.Environment_boundary_length(self)
    def area(self): return _visilibity.Environment_area(self)
    def diameter(self): return _visilibity.Environment_diameter(self)
    def bbox(self): return _visilibity.Environment_bbox(self)
    def random_points(self, *args): return _visilibity.Environment_random_points(self, *args)
    def shortest_path(self, *args): return _visilibity.Environment_shortest_path(self, *args)
    def compute_partition_cells(self, *args): return _visilibity.Environment_compute_partition_cells(self, *args)
    def write_to_file(self, *args): return _visilibity.Environment_write_to_file(self, *args)
    def __call__(self, *args): return _visilibity.Environment___call__(self, *args)
    def set_outer_boundary(self, *args): return _visilibity.Environment_set_outer_boundary(self, *args)
    def add_hole(self, *args): return _visilibity.Environment_add_hole(self, *args)
    def enforce_standard_form(self): return _visilibity.Environment_enforce_standard_form(self)
    def eliminate_redundant_vertices(self, epsilon = 0.0): return _visilibity.Environment_eliminate_redundant_vertices(self, epsilon)
    def reverse_holes(self): return _visilibity.Environment_reverse_holes(self)
    __swig_destroy__ = _visilibity.delete_Environment
    __del__ = lambda self : None;
Environment_swigregister = _visilibity.Environment_swigregister
Environment_swigregister(Environment)

def __eq__(*args):
  return _visilibity.__eq__(*args)
__eq__ = _visilibity.__eq__

def __ne__(*args):
  return _visilibity.__ne__(*args)
__ne__ = _visilibity.__ne__

def equivalent(*args):
  return _visilibity.equivalent(*args)
equivalent = _visilibity.equivalent

def boundary_distance(*args):
  return _visilibity.boundary_distance(*args)
boundary_distance = _visilibity.boundary_distance

class Guards(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Guards, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Guards, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Guards(*args)
        try: self.this.append(this)
        except: self.this = this
    def N(self): return _visilibity.Guards_N(self)
    def are_lex_ordered(self): return _visilibity.Guards_are_lex_ordered(self)
    def noncolocated(self, epsilon = 0.0): return _visilibity.Guards_noncolocated(self, epsilon)
    def _in(self, *args): return _visilibity.Guards__in(self, *args)
    def diameter(self): return _visilibity.Guards_diameter(self)
    def bbox(self): return _visilibity.Guards_bbox(self)
    def write_to_file(self, *args): return _visilibity.Guards_write_to_file(self, *args)
    def push_back(self, *args): return _visilibity.Guards_push_back(self, *args)
    def set_positions(self, *args): return _visilibity.Guards_set_positions(self, *args)
    def enforce_lex_order(self): return _visilibity.Guards_enforce_lex_order(self)
    def reverse(self): return _visilibity.Guards_reverse(self)
    def snap_to_vertices_of(self, *args): return _visilibity.Guards_snap_to_vertices_of(self, *args)
    def snap_to_boundary_of(self, *args): return _visilibity.Guards_snap_to_boundary_of(self, *args)
    __swig_destroy__ = _visilibity.delete_Guards
    __del__ = lambda self : None;
Guards_swigregister = _visilibity.Guards_swigregister
Guards_swigregister(Guards)

class Visibility_Polygon(Polygon):
    __swig_setmethods__ = {}
    for _s in [Polygon]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Visibility_Polygon, name, value)
    __swig_getmethods__ = {}
    for _s in [Polygon]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Visibility_Polygon, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Visibility_Polygon(*args)
        try: self.this.append(this)
        except: self.this = this
    def observer(self): return _visilibity.Visibility_Polygon_observer(self)
    __swig_destroy__ = _visilibity.delete_Visibility_Polygon
    __del__ = lambda self : None;
Visibility_Polygon_swigregister = _visilibity.Visibility_Polygon_swigregister
Visibility_Polygon_swigregister(Visibility_Polygon)

class Visibility_Graph(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Visibility_Graph, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Visibility_Graph, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _visilibity.new_Visibility_Graph(*args)
        try: self.this.append(this)
        except: self.this = this
    def n(self): return _visilibity.Visibility_Graph_n(self)
    def __call__(self, *args): return _visilibity.Visibility_Graph___call__(self, *args)
    __swig_destroy__ = _visilibity.delete_Visibility_Graph
    __del__ = lambda self : None;
Visibility_Graph_swigregister = _visilibity.Visibility_Graph_swigregister
Visibility_Graph_swigregister(Visibility_Graph)



def __lshift__(*args):
  return _visilibity.__lshift__(*args)
__lshift__ = _visilibity.__lshift__


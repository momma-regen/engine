from math import max, min
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class CollisionShape:
    active = True
    event = None # solid, trigger
    data = None
    _polygon = None
    _max = (None, None)
    _min = (None, None)
    
    def __init__(self, points, event = "solid", data = 0):
        self._max = (max([x[0] for x in points], max(y[1] for y in points)))
        self._polygon = Polygon(points)
        self.event = event
        self.data = data
            
    check = lambda self, target: ( # We check to see that both shapes are active and then create pretendsies rectangles using the shapes' min and max X and Y values to save on computing costs of comparing more complex shapes
        self.active # Is THIS collision currently active?
        and isinstance(target, CollisionShape) # Is the object we're colliding with ALSO a collision shape?
        and target.active # Is THAT collision currently active?
        and max(target._min[0], self._min[0]) > min(target._max[0], self._max[0]) # Pretend the shapes are a rectangle and compare on the X axis
        and max(target._min[1], self._min[1]) > min(target._max[1], self._max[1]) # Pretend the shapes are a rectangle and compare on the Y axis
        and self._polygon.intersects(target) # If all the easy checks have passed, compare the actual shapes to find collision
    )
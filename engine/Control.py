from pygame import mouse
from CollisionShape import CollisionShape

class Control(Entity):
    _func = lambda: None
    
    def __init__(self, func):
        if callable(func): self._func = func
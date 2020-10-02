from pygame import mouse
from engine.CollisionShape import CollisionShape
from engine.Entity import Entity

class Control(Entity):
    _func = lambda: None
    
    def __init__(self, func):
        if callable(func): self._func = func
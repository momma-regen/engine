from engine.FileHandler import FileHandler
from engine.Obj import Obj

class Level(Obj):
    _name = None
    _images = []
    _entities = []
    _collision = []
    _type = 0 # 0 => Top, 1 => Side, 2 => Face
    _flags = []
    
    def __init__(self, name, state = None):
        self._name = name
        file = FileHandler().load(f"lvl/{name}.dat")
        self._images = file.images
        self._entities = file.entities
        self._collision = file.collision
        self._type = file.type
        
        state.player().pos(file.playerSpawnPos, True)
        state.player().rot(file.playerSpawnRot, True)
        
    def collision(self, target):
        cols = []
        for entitiy in self._entities:
            for inx, col in enumerate(entity.col()):
                if col.check(target): cols.append((entity, inx))
        return cols
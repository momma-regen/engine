from FileHandler import FileHandler

class Level:
    _name = ""
    _images = []
    _entities = []
    _collision = []
    _type = 0 # 0 => Top, 1 => Side, 2 => Face
    _flags = []
    
    def __init__(self, name, state = None):
        self._name = name
        file = FileHandler(name)
        self._images = file.read("images", [])
        self._entities = file.read("entities", [])
        self._collision = file.read("collision", [])
        self._type = file.read("type", 0)
        
        state.player().pos(file.read("playerSpawnPos", None), True)
        state.player().rot(file.read("playerSpawnRot", None), True)
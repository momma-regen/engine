from engine.Entity import Entity
import engine.Log as Log
import engine.Control as Control

class Player(Entity):
    _name = None
    _sprites = {}
    _scheme = None
    _health = [0,0] #current/max
    _stats = {}
    
    def __init__(self, name):
        self._name = name
        self._load()
        
    def _load(self):
        file = FileHandler().load(f"ent/{self._name}.dat")
        for indx, sprt in enumerate(file.spriteList):
            name = sprt["name"]
            animations = sprt["animations"] if "animations" in sprt.keys() else None
            frameSize = sprt["frameSize"] if "frameSize" in sprt.keys() else None
            size = sprt["size"] if "size" in sprt.keys() else None
            self._sprites[name] = Sprite(file.images[indx].toBytes(), animations, frameSize, size)
        for name, value in file.data["stats"]:
            self.__setattr__(name, value)
            
    def scheme(self, scheme = None):
        if scheme == None: return self._scheme
        self._scheme = scheme
        if scheme != "td" and scheme != "ss":
            self._scheme = None
            Log.e(f'"{scheme}" is not a valid Player scheme')
            
    def health(self, update = None):
        if isinstance(update, int): self._health[0] = min(max(self._health[0] + update, 0), self._health[1])
        elif isinstance(update, tuple):
            for i, new in update: self._health[i] = new if new != None else self._health[i]
        else: return self._health
        
    def stats(self, name, update = None):
        try: 
            if update == None: return self._stats[name]
            self._stats[name] = update
        except: return None

    set_sprite = lambda self, name: _sprite = sprite(self._sprites[name])
    controls = lambda self: Control(controls[self._scheme])
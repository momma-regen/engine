from engine.File import File
from engine.Obj import Obj

class FlagController(Obj):
    _data = {}
    
    def __init__(self, data = None):
        try:
            for key, val in data: self.__setattr__(key, value)
        except: pass
                
    def __setattr__(self, name, value = None):
        if isinstance(value, (int, bool)) and name != "data": self._data[name] = int(value)
            
    def __getattr__(self, name):
        if name in self._data.keys(): return self._data[name]
        return 0
    
    def dump(self):
        return self._data
import Log

class GameState:
    _player = None
    _meter = {}
    
    def meter(self, target, value = None):
        if (value != None):
            try: self._meter[target] = max(min([100, value]), 0)
            except: 
                Log.e("Could not set meter \"{}\" to value \"{}\"".format(target, value))
                return False
        return self._meter[target] if value == None else True
        
    def player(self, new = None):
        if (not isinstance(new, Player)): return self._player
        self._player = new
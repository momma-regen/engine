from math import floor
from Sprite import Sprite

class Entity:
    _pos = (0,0)
    _rot = 0
    _col = []
    _sprite = None #refers to an entire sprite sheet
    _animations = {}
    
    def pos(self, update = None, replace = False):
        if not isinstance(update, tuple): return self._pos
        try: self._pos = (float(update[0]) + (self._pos[0] * int(not replace)), float(update[1]) + (self._pos[1] * int(not replace)))
        except: return False
        return True
    
    def rot(self, update = None, replace = False):
        if update == None: return self._rot
        try: self._rot = (float(update) + (self._rot * int(not replace))) - (360 * floor((float(update) + (self._rot * int(not replace)))/360))
        except: return False
        return True
            
    def col(self, key, update = None):
        try:
            if not isinstance(update, CollisionShape): return self._col[key]
            self._col[key] = update
        except: return False
        return True
    
    def sprite(self, update = None):
        if not isinstance(update, Sprite): return this._sprite
        try: this._sprite = update
        except: return False
        return True
    
    def anim(self, key, update = None):
        try: 
            if not isinstance(update, int): return this._animations[key]
            this._animations[key] = update
        except: return False
        return True
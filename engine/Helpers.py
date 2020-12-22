import sys

def isNumber(num, isInt = False):
    try: _ = float(num) if not isInt else int(num)
    except: return False
    return True if not isInt else num == _

flatten = lambda l: [item for sublist in l for item in sublist]

class PUBLIC(object):
    _class = None
    _value = None
    
    def __new__(self, value, *args, **kwargs):
        instance = super(PUBLIC, self).__new__(self, *args, **kwargs)
        instance.__init__(value, sys._getframe(1).f_locals["self"].__class__.__name__)
        return instance
    
    def __init__(self, value, class_name): 
        self._value = value
        self._class = class_name
        return 
        
    def __fromself__(self, frame):
        try: return frame.f_locals["self"].__class__.__name__ == super(PUBLIC, self).__getattribute__("class")
        except: return False
        
    def __getattr__(self, name):
        return super(PUBLIC, self).__getattribute__("_value").__getattr__(name)
    
    def __getattribute__(self, name):
        return super(PUBLIC, self).__getattribute__("_value").__getattribute__(name)
    
    def __setattr__(x, y, z):
        return super(PUBLIC, self).__getattribute__("_value").__setattr__(name)
        
    def __pos__(self): return self._value.__pos__()
    def __neg__(self): return self._value.__neg__()
    def __abs__(self): return self._value.__abs__()
    def __invert__(self): return self._value.__invert__()
    def __round__(self,n ): return self._value.__round__(n)
    def __floor__(self): return self._value.__floor__()
    def __ceil__(self): return self._value.__ceil__()
    def __trunc__(self): return self._value.__trunc()
    
    def __iadd__(self, other): return self._value.__iadd__(other)
    def __isub__(self, other): return self._value.__isub__(other)
    def __imul__(self, other): return self._value.__imul__(other)
    def __ifloordiv__(self, other): return self._value.__ifloordiv__(other)
    def __idiv__(self, other): return self._value.__idiv__(other)
    def __itruediv__(self, other): return self._value.__itruediv__(other)
    def __imod__(self, other): return self._value.__imod__(other)
    def __ipow__(self, other): return self._value.__ipow__(other)
    def __ilshift__(self, other): return self._value.__ilshift(other)
    def __irshift__(self, other): return self._value.__irshift(other)
    def __iand__(self, other): return self._value.__iand__(other)
    def __ior__(self, other): return self._value.__ior__(other)
    def __ixor__(self, other): return self._value.__ixor__(other)
    
    def __int__(self): return self._value.__int__()
    def __float__(self): return self._value.__float__()
    def __complex__(self): return self._value.__complex()
    def __oct__(self): return self._value.__oct__()
    def __hex__(self): return self._value.__hex__()
    def __index__(self): return self._value.__index__()
    def __trunc__(self): return self._value.__trunc__()
    
    def __str__(self): return self._value.__str__()
    def __repr__(self): return self._value.__repr__()
    def __unicode__(self): return self._value.__unicode__()
    def __format__(self, formatstr): return self._value.__format__(formatstr)
    def __hash__(self): return self._value.__hash__()
    def __nonzero__(self): return self._value.__nonzero__()
    def __dir__(self): return self._value.__dir__()
    def __sizeof__(self): return self._value.__sizeof__()
    
    def __add__(self, other): return self._value.__add__(other)
    def __sub__(self, other): return self._value.__sub__(other)
    def __mul__(self, other): return self._value.__mul__(other)
    def __floordiv__(self, other): return self._value.__floordiv__(other)
    def __truediv__(self, other): return self._value.__truediv__(other)
    def __mod__(self, other): return self._value.__mod__(other)
    def __pow__(self, other): return self._value.__pow__(other)
    def __lt__(self, other): return self._value.__lt__(other)
    def __gt__(self, other): return self._value.__gt__(other)
    def __le__(self, other): return self._value.__le__(other)
    def __ge__(self, other): return self._value.__ge__(other)
    def __eq__(self, other): return self._value.__eq__(other)
    def __ne__(self, other): return self._value.__ne__(other)
    
class PROTECTED(PUBLIC):
    def __getattr__(self, name): 
        return self._value.__getattr__(name)
    
    def __getattribute__(self, name):
        return self._value.__getattribute__(name)
    
    def __setattr__(x, y, z):
        if not self.__fromself__(sys._getframe(1)): raise AttributeError(f"Variable {name} is {self.__class__.__name__}")
        return self._value.__setattr__(name)
    
class PRIVATE(PROTECTED):
    def __getattr__(self, name): 
        if not self.__fromself__(sys._getframe(1)): raise AttributeError(f"Variable {name} is private")
        return self._value.__getattr__(name)
    
    def __getattribute__(self, name): 
        if not self.__fromself__(sys._getframe(1)): raise AttributeError(f"Variable {name} is private")
        return self._value.__getattr__(name)
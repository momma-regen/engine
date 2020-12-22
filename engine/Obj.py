from engine.Helpers import PUBLIC, PROTECTED, PRIVATE
import types
import sys

class Obj(object):
    def __getattr__(self, name):
        fl = sys._getframe(1).f_locals
        try: fs = fl["self" if "self" in fl else "__qualname__"] == super(Obj, self).__class__.__name__
        except: fs = False
            
        target = super(Obj, self).__getattribute__(name)

        if fs and type(target).__name__ in ["PUBLIC", "PRIVATE", "PROTECTED"]: return target._value
        elif not fs and isinstance(target, PRIVATE): raise AttributeError(f"Variable {name} is private")
        return target
    
    def __getattribute__(self, name):
        fl = sys._getframe(1).f_locals         
        try: fs = fl["self" if "self" in fl else "__qualname__"] == super(Obj, self).__class__.__name__         
        except: fs = False
            
        target = super(Obj, self).__getattribute__(name)
            
        if fs and type(target).__name__ in ["PUBLIC", "PRIVATE", "PROTECTED"]: return target._value
        elif not fs and isinstance(target, PRIVATE): raise AttributeError(f"Variable {name} is private")
        return target
    
    def __setattr__(self, name, value):
        fl = sys._getframe(1).f_locals         
        try: fs = fl["self" if "self" in fl else "__qualname__"] == super(Obj, self).__class__.__name__         
        except: fs = False
            
        target = super(Obj, self).__getattribute__(name)
            
        if fs and type(target).__name__ in ["PUBLIC", "PRIVATE", "PROTECTED"]: return target.__setattr__("_value", value)
        elif not fs:
            if isinstance(target, PRIVATE): raise AttributeError(f"Variable {name} is private")
            if isinstance(target, PROTECTED): raise AttributeError(f"Variable {name} is protected")
        return super(Obj, self).__setattr__(name, value)
    
    def __delattr__(self, name):
        fl = sys._getframe(1).f_locals         
        try: fs = fl["self" if "self" in fl else "__qualname__"] == super(Obj, self).__class__.__name__         
        except: fs = False
            
        target = super(Obj, self).__getattribute__(name)
            
        if fs and type(target).__name__ in ["PUBLIC", "PRIVATE", "PROTECTED"]: return super(Obj, self).__delattr__(name)
        elif not fs:
            if isinstance(target, PRIVATE): raise AttributeError(f"Variable {name} is private")
            if isinstance(target, PROTECTED): raise AttributeError(f"Variable {name} is protected")
        return super(Obj, self).__delattr__(name)
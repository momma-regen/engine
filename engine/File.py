from Img import Img

class File:
    _filepath = None
    _encrypted = None
    _data = None
    _images = []
    
    def __getattr__(self, name):
        try: 
            if isinstance(self._data, list):
                return self._data if name == "data" else None
            else:
                return self._data[name] if name != "images" else self._images
        except: return None
        
    def __setattr__(self, name, value):
        if isinstance(self._data, list) and name == "data": self._data = str(value)
        elif name == "images" and not isinstance(self._data, list):
            if isinstance(value, Img): value = [value]
            elif isinstance(value, bytes): value = [Img(value)]
            elif isinstance(value, list): value = filter(lambda x: x != None, map(lambda v: v if isinstance(v, Img) else Img(v) is isinstance(v, bytes) else None, value))
            self._images = value
        elif name[1] == "_" and super(File, self).__getattr__(name) == None: super(File, self).__setattr__(name, value)
        else: self._data[name] = value
            
    def __delattr__(self, name):
        if name == "images": self._images = []
        elif isinstance(self._data, list) and name == "data": self._data = []
        else: del self._data[name]
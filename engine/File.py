from engine.Img import Img

class File(object):
    _filepath = None
    _encrypted = None
    _data = None
    _images = []
    
    def __getattr__(self, name):
        try: 
            if name == "data" or name == "_data": return super(File, self).__getattribute__("_data")
            if isinstance(self._data, list): return None
            else: return self._data[name] if name != "images" else self._images
        except: return None
        
    def __setattr__(self, name, value):
        if isinstance(self._data, list) and (name == "data" or name == "_data"): super(File, self).__setattr__("_data", str(value))
        elif (name == "images" or name == "_images") and not isinstance(self._data, list):
            if isinstance(value, Img): value = [value]
            elif isinstance(value, bytes): value = [Img(value)]
            elif isinstance(value, list): value = list(filter(lambda x: x != None, list(map(lambda v: v if isinstance(v, Img) else Img(v) if isinstance(v, bytes) else None, value))))
            super(File, self).__setattr__("_images", value if value else [])
        elif name[0] == "_" and super(File, self).__getattribute__(name) == None: super(File, self).__setattr__(name, value)
        else: self._data[name] = value
            
    def __delattr__(self, name):
        if name == "images": self._images = []
        elif isinstance(self._data, list) and name == "data": self._data = []
        else: del self._data[name]
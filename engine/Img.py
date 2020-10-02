from PIL import Image
import io

class Img:
    _data = None
    
    def __init__(self, data): # I'd make this a lambda too if it'd let me
        self._data = data
           
    display = lambda self: Image.open(io.BytesIO(self._data))
    
    toBytes = lambda self: self._data
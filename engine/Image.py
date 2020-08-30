from PIL import Image
import io

class Image:
    _display = None
    
    def __init__(self, data):
        stream = io.BytesIO(data)
        self._display = Image.open(stream)
        
    def display(self):
        return self._display
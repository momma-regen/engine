import os
import json
import re
import cryptography
from engine.Img import Img
from engine.File import File
from cryptography.fernet import Fernet
from engine.Obj import Obj

class FileHandler(Obj):
    _key = None
    _loaded = False
    _separation_mark = b"\x9F\x44\x54\x46\x2A\x1A\x0A\x0A"
        
    def key(self):
        if (self._key == None):
            try: self._key = open("c14v.is", "rb").read()
            except:
                self._key = Fernet.generate_key()
                open("c14v.is", "wb+").write(self._key)
        return self._key
    
    def load(self, filepath, is_data = True):
        file = File()
        if (is_data):
            try: content = Fernet(self.key()).decrypt(open(filepath, "rb").read())
            except: content = str(open(filepath, "w+").close())[0:0] #open the file and initialize content as an empty string, all in one line   
            content = content.split(self._separation_mark)
            img_start = 1
            try: file._data = json.loads(content[0].decode("UTF-8"))
            except: 
                file._data = {}
                img_start = 0
            file._images = [Img(i_bytes) for i_bytes in content[img_start:]]
        else:
            try: file._data = re.compile("(\r\n|\r|\n)").split(open(filepath, "r").read())
            except: file._data = [open(filepath, "w+").close()][0:0] #same as above, but empty array
        self._loaded = True
        return file

    def save(self, file, override = False):
        if not self._loaded and not override: return
        if isinstance(file._data, dict): 
            data = json.dumps(file._data).encode() + self._separation_mark #+ self._separation_mark.join([img.toBytes() for img in file._images if isinstance(img, Img)])
            for image in file._images:
                if isinstance(image, Img): data += image.toBytes() + self._separation_mark
            data = data[:-8]
            open(file._filepath, "wb").write(Fernet(self.key()).encrypt(data))
        else: 
            print(str(self._data))
            open(file._filepath, "w").write("\n".join(file._data))
            
    def delete(self, file): 
        self._loaded = not bool(os.remove(file._filepath))
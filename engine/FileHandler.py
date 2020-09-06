import os
import json
import re
import cryptography
from Img import Img
from File import File
from cryptography.fernet import Fernet

class FileHandler:
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
            value = b""
            for i in range(len(content)):
                value += temp[i:i+1]
                if value[-8:] == self._separation_mark or i == (len(content)-1):
                    if file._data == None:
                        file._data = value[:-8].decode("UTF-8")
                    else:
                        file._images.append(value[:-8])
                    value = b""
            file._data = json.loads(file._data)
            file._images = list(map(lambda i_bytes: Image(i_bytes), file._images))
        else:
            try: file._data = re.compile("(\r\n|\r|\n)").split(open(filepath, "r").read())
            except: file._data = [open(filepath, "w+").close()][0:0] #same as above, but empty array
        self._loaded = True
        return file

    def save(self, file):
        if not _loaded: return
        if isinstance(file._data, dict): open(file._filepath, "wb").write(json.dumps(file._data).encode() + self._separation_mark.join([img.to_bytes for img in file._images]))
        else: open(file._filepath, "w").write("\n".join(file._data))
            
    delete = lambda self, file: self._loaded = not bool(os.remove(file._filepath))
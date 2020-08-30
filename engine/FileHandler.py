import os
import math
import cryptography
from os import path
from cryptography.fernet import Fernet
from Helpers import isNumber

class FileHandler:
    _content = {}
    _key = None
    _separate = b'\x9F\x44\x54\x46\x2A\x1A\x0A\x0A'
    _pointer = None
    _keys = []
    
    def __init__(self, fileName, text = False, enc = None):
        self._fileName = fileName
        self._text = text
        self._enc = enc if enc != None else not text
        
        try:
            if (not path.exists(self._fileName)): open(self._fileName, "w+")
        except:
            direct = "/".join((self._fileName.replace("\\", "/").split("/"))[:-1])
            os.mkdir(direct)
            open(self._fileName, "w+")
            
        self.load()
        
    def key(self):
        if (self._key == None):
            try:
                self._key  = open("c14v.is", "rb").read()
            except:
                self._key = Fernet.generate_key()
                with open("c14v.is", "wb+") as key_file:
                    key_file.write(self._key)
                
        return self._key

    def load(self):
        with open(self._fileName, "r" if self._text else "rb") as reader:
            if (self._text):
                i = 0
                for line in reader:
                    if (self._enc):
                        f = Fernet(self.key())
                        line = f.decrypt(line)
                    self._content[i] = line
                    i += 1
            else:
                temp = reader.read()
                v_name = ""
                value = b''
                v_type = 0
                if (self._enc):
                    f = Fernet(self.key())
                    if (len(temp)):
                        temp = f.decrypt(temp)
                for i in range(len(temp)):
                    value += temp[i:i+1]
                    if (value[-8:] == self._separate): #Check last 8 bytes to see if we hit the separation mark
                        if (len(v_name)):
                            if (not bool(v_type%2)):
                                value = value.decode("UTF-8")
                                if (v_type == 2): value = float(value)
                            elif (v_type == 1):
                                value = int.from_bytes(value, byteorder="little", signed=True)
                            if (self._content.has_key(v_name)):
                                self._content[v_name] = (self._content[v_name] if isinstance(self._content[v_name], list) else []) + [value]
                            else:
                                self._content[v_name] = value
                            
                        value = b''
                        i += 1
                        v_type = int.from_bytes(temp[i:i+1], byteorder="little", signed=True)
                        i += 2
                        v_name_tmp = b''
                        while True:
                            byte = temp[i:i+1]
                            if byte == b'\x0A': break
                            v_name_tmp += byte
                            i += 1
                        v_name = v_name.decode("UTF-8")
        self._keys = self._content.keys()
                        
    def save(self):
        with open(self._fileName, "w" if self._text else "wb") as writer:
            if(self._text):
                for key in self._content:
                    line = self._content[key]
                    if not line: continue
                    if (self._enc):
                        f = Fernet(self.key())
                        line = f.encrypt(line)
                    writer.write("{}\n".format(line))
            else:
                as_bytes = b''
                
                for key in self._content:
                    var = self._content[key]
                    # Type[0-3] | \n | Var Name | \n | Data | Separation Byte Mark
                    if (isinstance(var, bytes)):
                        as_bytes += b'\x03\x0A' + ("{}".format(key)).encode() + b'\x0A' + var + self._separate
                    elif (isinstance(var, int)):
                        as_bytes += b'\x01\x0A' + ("{}".format(key)).encode() + b'\x0A' + (line).to_bytes(math.round((math.log2(line)/8)+1), byteorder="little", signed=True) + self._separate
                    elif (isinstance(var, float)):
                        as_bytes += b'\x02\x0A' + ("{}".format(key)).encode() + b'\x0A' + ("{}".format(line)).encode() + self._separate
                    else:
                        as_bytes += b'\x00\x0A' + ("{}".format(key)).encode() + b'\x0A' + line.encode() + self._separate

                if (self._enc):
                    f = Fernet(self.key())
                    as_bytes = f.encrypt(as_bytes)
                    
                writer.write(as_bytes)
                
    def delete(self):
        os.remove(self._fileName)
    
    def write(self, x, y = None):
        keylist = self._content.keys() or ["-1"]
        print(keylist)
        if (y == None):
            key = max(int(max(list(filter(lambda x: isNumber(x, True), keylist)))) + 1, 0) #Can you use a negative number as a key? Yes. Am I going to let you do it automatically? No, get fucked
            val = x
        else:
            key = x
            val = y
        self._content[key] = val
            
    def read(self, key = None, alt = None):
        if key == None:
            r_val = alt if key >= len(self._content) else self._content[(self._content.keys())[self._pointer]]
            self._pointer += 1
        else:
            r_val = self._content[key] if key in (self._content.keys() or []) else alt
        
        return r_val
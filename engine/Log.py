from engine.FileHandler import FileHandler

class _log:
    def __init__(self, file):
        self._fh = FileHandler()
        self._file = self._fh.read(f"log/{file}.log", False)
        
    def __del__(self):
        self._fh.save(self._file)
    
    write = lambda self, text: self._file.data.append(text) or self._fh.save(self._file)
                       
    clear = lambda self: self._fh.delete()
                
write = lambda file, msg: _log(file).write(msg)
        
e = lambda msg = "": _log("error").write(msg)
d = lambda msg = "": _log("debug").write(msg)
i = lambda msg = "": _log("info").write(msg)
w = lambda msg = "": _log("warn").write(msg)
clear = lambda file: _log(file).clear()
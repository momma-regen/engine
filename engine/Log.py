from FileHandler import FileHandler

class _log:
    def __init__(self, file):
        self._file = "log/{}.log".format(file)
        
    def write(self, text):
        FH = FileHandler(self._file, True)
        FH.write(text)
        FH.save()
        del FH
        
    def clear(self, delete):
        FH = FileHandler(self._file, True)
        if (delete):
            FH.delete()
        else:
            FH._content = {}
            FH.save()
        
class _ql:
    def _shared(self, logType, msg = None):
        lf = _log(logType)
        if msg != None and not isinstance(msg, bool):
            lf.write(msg)
        elif msg != None:
            lf.clear(msg)
class e(_ql):
    def __init__(self, msg = None): super()._shared("error", msg)
class d(_ql):
    def __init__(self, msg = None): super()._shared("debug", msg)
class i(_ql):
    def __init__(self, msg = None): super()._shared("info", msg)
class w(_ql):
    def __init__(self, msg = None): super()._shared("warn", msg)
class clear(_ql):
    def __init__(self, trgt, delt = True): super()._shared(trgt, delt)
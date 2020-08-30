def isNumber(num, isInt = False):
    try: _ = float(num) if not isInt else int(num)
    except: return False
    return True if not isInt else num == _

flatten = lambda l: [item for sublist in l for item in sublist]
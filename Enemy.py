from engine.Entity import Entity

class Enemy(Entity):
    _eid = None
    
    def __init__(self, enemyID):
        self._eid = enemyID
        # Load shit here
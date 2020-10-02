from pygame import mouse
from engine.Control import Control
from engine.CollisionShape import CollisionShape

class Menu:
    _name = None
    _background = None
    _controls = [None]
    
    def __init__(self, name):
        self._name = name
    
    def m_open(self):
        #Draw background graphic if != None
        #Draw controls to screen
        mouse.set_visible(True)
        
    def m_close(self):
        mouse.set_visible(False)
        
    def control(self, key, update = None):
        if isinstance(update, Control): self._controls[key] = update
        else: return self._controls[key]
        return True
        
    def collision(self):
        col_list = []
        m_x, m_y = mouse.get_pos()
        m_col = CollisionShape([[m_x - 3, m_y - 3], [m_x + 3, m_y - 3], [m_x + 3, m_y + 3], [m_x - 3, m_y + 3]]) # Give a little leeway to the mouse pointer
        for control in self._controls:
            if control.col(0).check(m_col): col_list.append((control, 0))   # Formatted to keep standard with level collision function. 
        # Should only collide with one control and control should only have one collision shape
        return col_list
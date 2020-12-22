from engine.Helpers import isNumber, flatten
from math import floor, ceil
from engine.Img import Img

class Sprite(Img):
    _frame = 0 #FRAME
    _currAnimation = 0 #INDEX
    _animations = [] #FRAMES
    _frameSize = (32,32) #PIXELS
    _size = (32,32) #PIXELS
    _max = (1,1) #FRAMES
    
    def __init__(self, data, animations = [((1,1), (1,1))], frameSize = None, size = None): #This will default to displaying the entire image as the sprite to avoid a crash
        super().__init__(data)
        if isinstance(animations, list) and self._fa(animations): self._animations = animations
        if isinstance(size, tuple) and isNumber(size[0]) and isNumber(size[1]): self._size = size
        if isinstance(frameSize, tuple) and isNumber(frameSize[0]) and isNumber(frameSize[1]): self._frameSize = frameSize
            
        width, height = self._display.size
        self._max = (floor(width/self._frameSize[0]), floor(height/self._frameSize[1]))
        if size == None: size = self._frameSize
            
    def _fa(self, animations):
        try: 
            x = flatten(flatten(animations))
            sum(x)
        except: return False
        return not bool(len(x)%4)
        
    def animate(self): # Animations are stored as [(Start X,Y), (End X,Y)]
        end = self._animations[self._currentAnimation][1]
        self._frame += 1
        x, y = self.frame(False) # Horizontal and vertical index of current frame
        if y * 100 + x > end[1] * 100 + end[0]: # Y is increased after going through a row of X's. Therefor, 1 Y = several X's. As long as there aren't more than 100 frames per row, this makes for an easy comparison
            self._frame = 0 # Frame has gone past the last frame of animation. Start from beginning
            
    def frame(self, bounds = True): # Bounds returns the actual frame position on the image. Otherwise x and y will be the indicies of the frames horizontally and vertically
        start, end = self._animations[self._currentAnimation]
        over = max((start[0] + self._frame + 1) - self._max[0], 0)
        x = over - (self._max[0] * floor(over/self._max[0]))
        y = start[1] + floor(over/self._max[0])
        return ((x * self._frameSize, y * self._frameSize), ((x+1) * self._frameSize), (y+1) * self._frameSize) if bounds else (x, y)
    
    def size(self, update = None):
        if not isinstance(update, tuple): return self._size
        if not isNumber(update[0]) or not isNumber(update[1]): return False
        self._size = update
        
    def animation(self, update = None):
        self._currAnimation = update if isinstance(update, int) else self._currAnimation
        return self._currAnimation == update
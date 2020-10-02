import pygame, sys
import random
from pygame.locals import *
from engine.Loader import *

def die():
    pygame.quit()
    sys.exit()
    
def update():
    quit = False
    return not quit

def draw():
    pass

data = FileHandler().load("data/main.dat")
title = data.title
screen_size = tuple(data.screen_size)
fps = data.fps

del data

pygame.init()
displaySurface = pygame.display.set_mode(screen_size)
displaySurface.fill((0, 0, 0))
pygame.display.set_caption(title)

# Main Game Loop
while True:
    if not update() break;
    draw()
    clock.tick(fps)
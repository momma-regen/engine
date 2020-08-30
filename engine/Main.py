import pygame, sys
from pygame.locals import *
import random
import os.path
from os import path

from FileHandler import FileHandler
import Log

def die():
    pygame.quit()
    sys.exit()
    
def update():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            die()
        else:
            Log.e("Event \"{}\" not found!".format(event.type))
    
def draw():
    pass
    # draw

#####################

data = FileHandler("data/main.dat")

gameTitle = data.read(0, "GAME TITLE")
screenSize = (data.read(1, 600), data.read(2, 400))
FPS = data.read(3, 60)
clock = pygame.time.Clock()

data.save()
del data

pygame.init()
displaySurface = pygame.display.set_mode(screenSize)
displaySurface.fill((0, 0, 0))
pygame.display.set_caption(gameTitle)

# Main game loop
while True:
    update()
    draw()
    clock.tick(FPS)
import pygame,sys,os
from pygame.locals import * #load constants

red=(255,0,0)

# Initialize pygame
pygame.init()

# Set up window
windowSurface=pygame.display.set_mode((1000,600))
pygame.display.set_caption('Snake Game')

# set up drawing surface
screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
# main game loop
    for event in pygame.event.get():
        print(event)
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

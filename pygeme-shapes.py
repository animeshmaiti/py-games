#imports
import pygame,sys
from pygame.locals import *

pygame.init()

# set up the window
surface=pygame.display.set_mode((400,300),0,32) #doc written in readme
pygame.display.set_caption('Drawings')

#set up the colors (RGB)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

# draw the surg=face object
""" surface->This parameter specifies the surface on which you want
to draw the circle. It's the target surface where the circle will be drawn."""
pygame.draw.polygon(surface,GREEN,((230, 55),(120, 90),(120,200),(230, 245),(300,150)))
# 5 co-ordinates connect the points and fill with color green

pygame.draw.line(surface,BLUE,(60,60),(120,60),4) # 2 co-ordinates and as tuple and thickness of line
pygame.draw.line(surface,BLUE,(120,60),(60,120)) # here ony have 2 co-ordinates no thickness
pygame.draw.line(surface,BLUE,(60,120),(120,120),4)

pygame.draw.circle(surface,BLUE,(300,50),20,0)
# (300,50) co-ordinate of center of circle '20'-> is radius
# '0' thickness of outline
pygame.draw.ellipse(surface,RED,(300,200,40,80),1)
#'(300, 200, 40, 80)':(300, 200, 40, 80): This tuple represents the position and dimensions of the ellipse.
# The first value (300) is the X-coordinate of the top-left corner of the bounding rectangle, the second value (200) is the Y-coordinate,
# the third value (40) is the width of the ellipse, and the fourth value (80) is the height.
pygame.draw.rect(surface,RED,(200,150,100,50))
# '(200,150,100,50)' :This tuple represents the position and dimensions of the rectangle. The first value (200)
# is the X-coordinate of the top-left corner of the rectangle, the second value (150) is the
# Y-coordinate, the third value (100) is the width of the rectangle, and the fourth value (50) is the height.

pixObj=pygame.PixelArray(surface)
pixObj[380][280]=BLACK
pixObj[382][282]=BLACK
pixObj[384][284]=BLACK
pixObj[386][286]=BLACK
pixObj[388][288]=BLACK
del pixObj

while True:
    for event in pygame.event.get():
        print(event)
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
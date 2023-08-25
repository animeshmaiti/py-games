import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pentagon Drawing")

def calculate_pentagon_vertices(center_x, center_y, size):
    vertices = []
    for i in range(5):
        angle = 2 * math.pi * i / 5  # Divide the circle into 5 equal parts
        print(angle)
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        print(x,y)
        vertices.append((x, y))
    return vertices

center_x, center_y = width // 2,height // 2
print(center_x,center_y)
pentagon_size = 100
pentagon_vertices = calculate_pentagon_vertices(center_x, center_y, pentagon_size)

running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen

    # Draw the pentagon
    pygame.draw.polygon(screen, (255, 255, 255), pentagon_vertices)

    pygame.display.flip()

pygame.quit()

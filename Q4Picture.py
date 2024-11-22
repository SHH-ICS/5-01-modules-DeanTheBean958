# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame, sys
from pygame import Color
from pygame import draw, Rect
from pygame.locals import QUIT

pygame.init()
Surface = pygame.display.set_mode((600, 300))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    Surface.fill("Lightblue")
    
    draw.rect(Surface, Color('darkgreen'), Rect(0, 200, 500, 200))

    draw.rect(Surface, Color('brown'), Rect(100, 50, 300, 150))


    draw.circle(Surface, Color('yellow'), (50, 50), 50)
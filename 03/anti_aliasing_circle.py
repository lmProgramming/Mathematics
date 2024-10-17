from pygame import gfxdraw
import pygame
import pygame.gfxdraw
from pygame.locals import *
import math
import itertools

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False

white = pygame.Color(255, 255, 255)
times_clicked = 0

pygame.display.set_caption("Bresenham Circle")

radius = 50
center = (200, 200)

def circle_points(x, y, center):
    screen.set_at((x + center[0], y + center[1]),                   
                  white)    
    screen.set_at((y + center[0], x + center[1]),                  
                  white)    
    screen.set_at((y + center[0], -x + center[1]),                  
                  white)    
    screen.set_at((x + center[0], -y + center[1]),                   
                  white)    
    screen.set_at((-x + center[0], -y + center[1]),                   
                  white)    
    screen.set_at((-y + center[0], -x + center[1]),                   
                  white)    
    screen.set_at((-y + center[0], x + center[1]),                   
                  white)
    screen.set_at((-x + center[0], y + center[1]),                   
                  white)

def plot_circle(radius, center):
    x = 0
    y = radius
    d = 5/4.0 - radius
    
    circle_points(x, y, center)
    while y > x:
        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2 * (x - y) + 5
            x += 1
            y -= 1
        circle_points(x, y, center)

while not done:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True    
    
    pygame.draw.circle(screen, white, (500, 500), 200, 1)
    
    pygame.gfxdraw.aacircle(screen, 500, 500, 210, white)
    
    pygame.display.update()

pygame.quit()
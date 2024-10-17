import pygame
from pygame.locals import *
import math

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False

white = pygame.Color(255, 255, 255)
times_clicked = 0

pygame.display.set_caption("Naive Circle")

radius = 50
center = (200, 200)

while not done:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True    
            
    for x in range(-50, 50):
        y = math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
        
        screen.set_at((int(x + center[0]), int(y + center[1])), white)
        
        y = -y
        
        screen.set_at((int(x + center[0]), int(y + center[1])), white)
                
    pygame.display.update()

pygame.quit()
import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False

white = pygame.Color(255, 255, 255)
times_clicked = 0

points = []

while not done:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True    
        elif event.type == MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())
            
        if len(points) > 2:                
            pygame.draw.polygon(screen, white, points)
        elif len(points) == 2:
            pygame.draw.line(screen, white, *points)
        elif len(points) == 1:
            pygame.draw.circle(screen, white, *points, radius=1)
        pygame.display.update()

pygame.quit()
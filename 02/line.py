import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False

white = pygame.Color(255, 255, 255)
times_clicked = 0

while not done:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True    
        elif event.type == MOUSEBUTTONDOWN:      
            if times_clicked == 0:        
                point1 = pygame.mouse.get_pos()      
            else:        
                point2 = pygame.mouse.get_pos()      
            times_clicked += 1      
            if times_clicked > 1:        
                pygame.draw.line(screen, white, point1,                         
                                point2, 1)        
                times_clicked = 0  
        pygame.display.update()

pygame.quit()
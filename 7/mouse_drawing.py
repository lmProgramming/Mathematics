import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, 
                                  screen_height))
done = False
white = pygame.Color(255, 255, 255)

clock = pygame.time.Clock()
fps = 30
mouse_down = False
last_mouse_pos = (0, 0)

button_pos = (10, 10)
button_size = (100, 50)
button_color = (0, 255, 0)

while not done:  
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            last_mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            pygame.draw.line(screen, white, last_mouse_pos, event.pos, 5)
            last_mouse_pos = event.pos
            if button_pos[0] < event.pos[0] < button_pos[0] + button_size[0] and button_pos[1] < event.pos[1] < button_pos[1] + button_size[1]:
                print('Button clicked')
                
    pygame.draw.rect(screen, button_color, (button_pos, button_size))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()

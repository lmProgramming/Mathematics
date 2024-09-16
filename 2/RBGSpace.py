import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            screen.set_at((x, y), 
                          pygame.Color(
                              0,
                              int(x/SCREEN_WIDTH * 255), 
                              int(y/SCREEN_HEIGHT * 255)))
            
    pygame.display.update()

pygame.quit()
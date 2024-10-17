import pygame


pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255,255,255)

stars = []

class Star:
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y

while not done:  
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            done = True  
            
        position = (100, 100)
        pygame.draw.rect(screen, white, 
                     (position[0],position[1],
                     10, 10))
    pygame.display.update()

pygame.quit()

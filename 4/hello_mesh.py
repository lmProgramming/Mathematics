import pygame
from pygame.locals import *
from OpenGL.GL import *
from mesh3d import *
from OpenGL.GLU import *

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, 
                                  screen_height),   
                                 DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)

mesh = Mesh3D()

cube = Cube()

gluPerspective(30, (screen_width / screen_height), 0.1, 100.0)
glTranslatef(0.2, 0.1, -3)

while not done:  
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    cube.draw()
    glRotate(5, 1, 0, 1)
    pygame.time.wait(100)
    pygame.display.flip()
pygame.quit()

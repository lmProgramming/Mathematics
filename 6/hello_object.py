from object import *
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

objects = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, -1)))
cube.add_component(Cube(GL_POLYGON, "models/brick_texture.jpg"))
objects.append(cube)

cube2 = Object("Cube2")
cube2.add_component(Transform((1.1, 0, -1)))
cube2.add_component(Cube(GL_POLYGON, "models/brick_texture.jpg"))
objects.append(cube2)

glMatrixMode(GL_PROJECTION)
gluPerspective(30, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.2, 0.1, -3)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))

clock = pygame.time.Clock()
fps = 30
while not done:  
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:      
            done = True  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    for object in objects: 
        object.update()
    glRotate(5, 1, 0, 1)
    print('tick={}, fps={}'.format(clock.tick(), clock.get_fps()))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()

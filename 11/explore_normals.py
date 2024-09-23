from typing import List
from pygame.event import Event
from object import *
import pygame
from pygame.locals import *
from OpenGL.GL import *
from mesh3d import *
from OpenGL.GLU import *
from button import *
from settings import *
from grid import *
from display_normals import *
from load_mesh import *

pygame.init()

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, 
                                  SCREEN_HEIGHT),   
                                 DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

def print_hello() -> None:
    print("Hey")
    
objects_3d: list[Object] = []
objects_2d: list[Object] = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, -1.5)))
cube.add_component(LoadMesh(GL_LINE_LOOP, "models/planesm.obj"))
cube.add_component(DisplayNormals(cube.get_component(LoadMesh).vertices, cube.get_component(LoadMesh).triangles))
objects_3d.append(cube)

def set_2d() -> None:
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ORTHODOX_WIDTH, 0, ORTHODOX_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    
def set_3d() -> None:
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    glEnable(GL_DEPTH_TEST)

clock = pygame.time.Clock()
fps = 30

while not done:      
    events: List[Event] = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):      
            done = True
    
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    
    set_3d()
    for object in objects_3d: 
        object.update(events)
    set_2d()
    for object in objects_2d: 
        object.update(events)
        
    glPopMatrix()    
    pygame.display.flip()
    dt = clock.tick(fps)
pygame.quit()

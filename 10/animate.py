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
cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON, "models/brick_texture.jpg"))
objects_3d.append(cube)

cube2 = Object("Cube2")
cube2.add_component(Transform((0, 1, -5)))
cube2.add_component(Cube(GL_POLYGON, "models/brick_texture_2.jpg"))
objects_3d.append(cube2)

grid = Object("Grid")
grid.add_component(Transform((0, 0, -5)))
grid.add_component(Grid(0.5, 8, green))
objects_3d.append(grid)

speed = 0.1

def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ORTHODOX_WIDTH, 0, ORTHODOX_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    
def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    glEnable(GL_DEPTH_TEST)

clock = pygame.time.Clock()
fps = 30

trans: Transform = cube.get_component(Transform)

start_position = pygame.Vector3(-3, 0, -5)
end_position = pygame.Vector3(0, 0, -5)
v: pygame.Vector3 = end_position - start_position
t: float = 0
dt: float = 0

trans2: Transform = cube2.get_component(Transform)

while not done:      
    events: List[Event] = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):      
            done = True
                
    if t <= 1:
        trans.set_position(start_position + v * t)
        t += 0.0001 * dt
    
    x_change = 0
    y_change = 0           
    keys = pygame.key.get_pressed()
    
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

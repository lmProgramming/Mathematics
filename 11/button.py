from OpenGL.GL import *
from utils import *
import pygame
from settings import *

class Button:
    def __init__(self, screen, position, width, height, color, over_color, pressed_color, on_click) -> None:
        self.screen = screen
        self.position = position
        self.width = width
        self.height = height
        self.normal_color = color
        self.over_color = over_color
        self.pressed_color = pressed_color
        self.on_click = on_click
        self.pressed = False
        
    def set_correct_color(self, events, inside) -> None:
        if not inside:
            glColor3f(self.normal_color[0], self.normal_color[1], self.normal_color)
            return
        
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                glColor3f(self.pressed_color[0], self.pressed_color[1], self.pressed_color[2])
                self.on_click()
                return
        glColor3f(self.over_color[0], self.over_color[1], self.over_color[2])     
        
    def draw(self, events = None) -> None:
        mouse_pos: pygame.Tuple[int] = pygame.mouse.get_pos()
        mx = map_value(0, SCREEN_WIDTH, 0, ORTHODOX_WIDTH, mouse_pos[0])
        my = map_value(0, SCREEN_HEIGHT, ORTHODOX_HEIGHT, 0, mouse_pos[1])
        glPushMatrix()
        glLoadIdentity()
        mouse_inside = self.position[0] < mx < self.position[0] + self.width \
            and self.position[1] < my < self.position[1] + self.height
        
        self.set_correct_color(events, mouse_inside)
        
        glBegin(GL_POLYGON)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        glEnd()
        glPopMatrix()
from pygame import Vector3
from mesh3d import *
from transform import *
from button import *
from grid import *
from display_normals import *
from typing import TypeVar, Type

T = TypeVar('T')

class Object:
    def __init__(self, obj_name) -> None:
        self.name = obj_name
        self.components: list[object] = []
        self.scene_angle: float = 0
        
    def add_component(self, component) -> None:
        self.components.append(component)
        
    def get_component(self, class_type: Type[T]) -> T:
        for c in self.components:
            if isinstance(c, class_type):
                return c
        raise ValueError(f"Component of type {class_type} not found")
        
    def update(self, events) -> None:
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
                pos: Vector3 = c.get_position()
                glTranslatef(pos.x, pos.y, pos.z)
                self.scene_angle += 0.5
                glRotate(self.scene_angle, 0, 1, 0)
                print(self.scene_angle)
            elif isinstance(c, Mesh3D):
                glColor(1, 1, 1)
                c.draw()
            elif isinstance(c, Button):
                c.draw(events)
            elif isinstance(c, Grid):
                c.draw()
            elif isinstance(c, DisplayNormals):
                c.draw()
        glPopMatrix()
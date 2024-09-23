from mesh3d import *
from transform import *
from button import *
from grid import *
from display_normals import *

class Object:
    def __init__(self, obj_name) -> None:
        self.name = obj_name
        self.components: list[object] = []
        
    def add_component(self, component):
        self.components.append(component)
        
    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None
        
    def update(self, events):
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
                pos = c.get_position()
                glTranslatef(pos.x, pos.y, pos.z)
                glRotate(45, 0, 1, 0)
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
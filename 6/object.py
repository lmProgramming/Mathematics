from mesh3d import *
from transform import *

class Object:
    def __init__(self, obj_name) -> None:
        self.name = obj_name
        self.components = []
        
    def add_component(self, component):
        self.components.append(component)
        
    def update(self):
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
                pos = c.get_position()
                glTranslatef(pos.x, pos.y, pos.z)
            if isinstance(c, Mesh3D):
                c.draw()
        glPopMatrix()
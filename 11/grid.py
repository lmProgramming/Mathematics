from OpenGL.GL import *

class Grid:
    def __init__(self, interval, half_size, color) -> None:
        self.interval = interval
        self.half_size = half_size
        self.color = color
        
    def draw(self) -> None:
        glColor3f(self.color[0], self.color[1], self.color[2])
        glBegin(GL_LINES)
        for x in range(-self.half_size, self.half_size):
            for y in range(-self.half_size, self.half_size):
                glVertex3fv((x * self.interval, y * self.interval - 10, 0))
                glVertex3fv((x * self.interval, y * self.interval + 500, 0))
                
                glVertex3fv((y * self.interval - 10, x * self.interval, 0))
                glVertex3fv((y * self.interval + 500, x * self.interval, 0))
        glEnd()
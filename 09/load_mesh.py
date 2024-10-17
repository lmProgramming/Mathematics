from mesh3d import *
        
class LoadMesh(Mesh3D):
    def __init__(self, draw_type, model_filename) -> None:
        self.vertices, self.triangles = self.load_model(model_filename)
        self.draw_type = draw_type
        
    def load_model(self, model_filename):
        vertices = []
        triangles = []
        with open(model_filename, 'r') as f:
            for line in f:
                if line.startswith('v '):
                    vertices.append(list(map(float, line[2:].split())))
                elif line.startswith('f '):
                    triangles.extend([int(x.split('/')[0]) - 1 for x in line[2:].split()])
                    
        return vertices, triangles

    def draw(self) -> None:
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            for i in range(3):
                v = self.vertices[self.triangles[t + i]]
                glVertex3f(v[0], v[1], v[2])
            glEnd()
        glDisable(GL_TEXTURE_2D)
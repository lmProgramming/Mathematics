from mesh3d import *
        
class LoadMesh(Mesh3D):
    def __init__(self, draw_type, model_filename, texture_file="") -> None:
        self.vertices, self.uvs, self.triangles = self.load_model(model_filename)
        self.texture_file = texture_file
        self.draw_type = draw_type
        if self.texture_file != "":
            self.texture = pygame.image.load(self.texture_file)
            self.texId = glGenTextures(1)
            textureData = pygame.image.tostring(self.texture, "RGB", 1)
            width = self.texture.get_width()
            height = self.texture.get_height()
            glBindTexture(GL_TEXTURE_2D, self.texId)
            glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
        
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
        if self.texture_file != "":
            glEnable(GL_TEXTURE_2D)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
            glBindTexture(GL_TEXTURE_2D, self.texId)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            if self.texture_file != "":
                glTexCoord2fv(self.uvs[self.triangles[t]])
                glTexCoord2fv(self.uvs[self.triangles[t + 1]])
                glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        if self.texture_file != "":
            glDisable(GL_TEXTURE_2D)
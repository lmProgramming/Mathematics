from OpenGL.GL import *
import pygame


class Mesh3D:
    def __init__(self) -> None:
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)
                         ]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP
        self.texId = 0

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texId)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glTexCoord2fv(self.uvs[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t]])
            glTexCoord2fv(self.uvs[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glDisable(GL_TEXTURE_2D)

    def init_texture(self):
        self.texId = glGenTextures(1)
        texture_data = pygame.image.tostring(self.texture, "RGB", 1)

        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texId)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, texture_data)


class Cube(Mesh3D):
    def __init__(self, draw_type, file_name) -> None:
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (-0.5, -0.5, -0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (-0.5, -0.5, -0.5),
                         (-0.5, -0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (-0.5, 0.5, -0.5),
                         (-0.5, -0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (0.5, 0.5, -0.5),
                         (0.5, 0.5, 0.5),
                         (0.5, -0.5, 0.5)
                         ]

        self.triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5,
                          8, 5, 9, 10, 6, 7, 10, 7, 11,
                          12, 13, 14, 12, 14, 15, 16, 17, 18,
                          16, 18, 19, 20, 21, 22, 20, 22, 23]

        self.uvs = [(0.0, 0.0),
                    (1.0, 0.0),
                    (0.0, 1.0),
                    (1.0, 1.0),
                    (0.0, 1.0),
                    (1.0, 1.0),
                    (0.0, 1.0),
                    (1.0, 1.0),
                    (0.0, 0.0),
                    (1.0, 0.0),
                    (0.0, 0.0),
                    (1.0, 0.0),
                    (0.0, 0.0),
                    (0.0, 1.0),
                    (1.0, 1.0),
                    (1.0, 0.0),
                    (0.0, 0.0),
                    (0.0, 1.0),
                    (1.0, 1.0),
                    (1.0, 0.0),
                    (0.0, 0.0),
                    (0.0, 1.0),
                    (1.0, 1.0),
                    (1.0, 0.0)]
        self.texture = pygame.image.load(file_name)
        self.draw_type = draw_type
        self.init_texture()

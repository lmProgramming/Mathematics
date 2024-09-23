import pygame
from OpenGL.GL import *
from math_ogl import *

class DisplayNormals:
    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles
        self.normals = []
        for t in range(0, len(self.triangles), 3):
            v1 = self.vertices[self.triangles[t]]
            v2 = self.vertices[self.triangles[t + 1]]
            v3 = self.vertices[self.triangles[t + 2]]
            
            p = pygame.Vector3(v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])
            q = pygame.Vector3(v2[0] - v3[0], v2[1] - v3[1], v2[2] - v3[2])
            
            normal = cross_product(p, q)
            nstart = (0, 0, 0)
            self.normals.append((nstart, nstart + normal))
            
    def draw(self):
        glColor3fv((0, 1, 0))
        glBegin(GL_LINES)
        for i in range(len(self.normals)):
            glVertex3fv(self.normals[i][0])
            glVertex3fv(self.normals[i][1])
        glEnd()
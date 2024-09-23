import pygame
from OpenGL.GL import *
from math_ogl import *

class DisplayNormals:
    def __init__(self, vertices, triangles) -> None:
        self.vertices = vertices
        self.triangles = triangles
        self.normals = []
        for t in range(0, len(self.triangles), 3):
            v1 = self.vertices[self.triangles[t]]
            v2 = self.vertices[self.triangles[t + 1]]
            v3 = self.vertices[self.triangles[t + 2]]
            
            p = pygame.Vector3(v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])
            q = pygame.Vector3(v2[0] - v3[0], v2[1] - v3[1], v2[2] - v3[2])
            
            normal: pygame.Vector3 = cross_product(p, q)
            midpoint = v3 + q * .5
            v = (midpoint - v1) * 2 / 3
            centroid = v1 + v
            self.normals.append((centroid, centroid + normal * 10))
            
    def draw(self):
        glColor3fv((1, 1, 0))
        glBegin(GL_LINES)
        for i in range(len(self.normals)):
            start_point = self.normals[i][0]
            end_point = self.normals[i][1]
            
            glVertex3fv((
                start_point[0],
                start_point[1],
                start_point[2]
            ))
            glVertex3fv((
                end_point[0],
                end_point[1],
                end_point[2]
            ))
        glEnd()
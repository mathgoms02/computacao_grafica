import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Vértices do cubo: Cada ponto no espaço 3D é definido por (x, y, z)
vertices = [
    (1, -1, -1),    # 0
    (1, 1, -1),     # 1
    (-1, 1, -1),    # 2
    (-1, -1, -1),   # 3
    (1, -1, 1),     # 4
    (1, 1, 1),      # 5
    (-1, -1, 1),    # 6
    (-1, 1, 1)      # 7
]

# Linhas que conectam os vértices para formar as arestas do cubo
edges = [
    (0, 1), # ligando o vértice 0 no 1, por isso vértices numerados
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

def draw_cube():
    glBegin(GL_LINES) #Desenhar linhas??
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex]) # Define a posição dos vértices para cada linha desenhada

    glEnd()

def main():
    
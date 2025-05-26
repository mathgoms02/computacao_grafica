import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define vértices do cubo
vertices = (
    (1, -1, -1),    # 0
    (1, 1, -1),     # 1
    (-1, 1, -1),    # 2
    (-1, -1, -1),   # 3
    (1, -1, 1),     # 4
    (1, 1, 1),      # 5
    (-1, -1, 1),    # 6
    (-1, 1, 1)      # 7
)

# Define as arestas para desenhar o contorno do cubo (opcional)
edges = (
    (0, 1), # ligando o vértice 0 no 1, por isso vértices numerados
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7),
    (6, 7),
    (6, 4),
    (0, 4),
    (1, 5),
    (2, 7),
    (3, 6)
)

# Define as faces do cubo ??
faces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

# Define uma cor para o cubo
color = (1, 1, 1)  # Verde branco

def Cube():
    glBegin(GL_QUADS)
    glColor3fv(color)  # Define a cor
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])  # Desenha os vértices da face
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))  # Preto para as arestas
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glClearColor(0.2, 0.3, 0.7, 1.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Rotaciona o cubo
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

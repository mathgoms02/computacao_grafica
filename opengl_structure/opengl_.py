#pip install PyOpenGL PyOpenGL_accelerate pygame

import pygame    # pygame responsavel pela janela
from pygame.locals import *
from OpenGL.GL import *     # Utilizado para desenhar e fazer animação
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Desenhando linha simples 
# def draw_line_1():
#     vertices = [
#         # primeira linha
#         [1,1,-1], #ponto inicial da linha 
#         [1,1,1], #ponto final da linha
#     ]

#     glBegin(GL_LINES)
#     for vertex in vertices:
#         glVertex3fv(vertex) # 3fv é de tridimensional
#     glEnd()

def draw_line():
    vertices = [
        # primeira linha
        [1,1,-1], #ponto inicial da linha 
        [1,1,1], #ponto final da linha

        # segunda linha
        [1,-1,-1],
        [1,-1, 1]
    ]

    # criando as linhas entre os vertices
    edges= [
        (0,1),
        (2,3)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex]) # 3fv é de tridimensional
    glEnd()

def main():
    pygame.init()    # inicializa o pygame
    display = (800, 600) # tamanho da tela

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0) # configura a projeção perspectiva função(angulo, proporção altura e largura, distancia minima da visão, distancia máxima)
    glTranslatef(0.0, 0.0, -5) # translada o centro da câmera para o ponto (-5,0,0). Fica a -5 de distancia da minha camera

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1.0, 0.0, 0.0) # Cor vermelha

        draw_line() # desenha a linha

        glRotatef(1,3,1,1) # aonde colocar valor positivo, vai rotacionar funcao(angulo, eixoX{quanto maior, mais rotaciona}, eixoY, eixoZ )
        pygame.display.flip() # faz ele atualizar
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import requests
import time



# Define vértices do cubo
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Define as faces do cubo com os índices dos vértices
faces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

# # Define as arestas para desenhar o contorno do cubo
# edges = (
#     (0, 1),
#     (1, 2),
#     (2, 3),
#     (3, 0),
#     (4, 5),
#     (5, 7),
#     (7, 6),
#     (6, 4),
#     (0, 4),
#     (1, 5),
#     (2, 7),
#     (3, 6)
# )

# Coordenadas de textura para cada face
texture_coords = (
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1),
)

# Função para carregar a textura
def load_texture(image_path):
    texture = glGenTextures(1,[1])
    image = pygame.image.load(image_path)
    image = pygame.transform.flip(image, False, True)  # Inverte a imagem verticalmente
    image_data = pygame.image.tostring(image, "RGBA", True)
    width, height = image.get_rect().size
    
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    return texture

# Função para desenhar o cubo com textura
def draw_textured_cube(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        for j, vertex in enumerate(face):
            glTexCoord2fv(texture_coords[j])  # Mapeia coordenadas de textura
            glVertex3fv(vertices[vertex])
    glEnd()

# Configuração de textura com base na temperatura
def get_texture_by_temperature(temperature, textures):
    if temperature is not None and temperature > 30.0:
        return textures['hot']    # Textura para quente
    elif temperature is not None and temperature > 20.0:
        return textures['warm']   # Textura para médio quente
    else:
        return textures['cold']   # Textura para frio

# # Função para desenhar o cubo com faces coloridas
# def draw_faces(color):
#     glColor3f(*color)
#     glBegin(GL_QUADS)
#     for face in faces:
#         for vertex in face:
#             glVertex3fv(vertices[vertex])
#     glEnd()

# # Função para desenhar as arestas do cubo em preto
# def draw_edges():
#     glColor3f(0, 0, 0)
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(vertices[vertex])
#     glEnd()

# # Configuração de cor com base na temperatura
# def get_cube_color(temperature):
#     if temperature is not None and temperature > 28.0:
#         return (1, 0, 0)  # Vermelho para quente
#     elif temperature is not None and temperature > 25.0:
#         return (1, 1, 0)  # Amarelo para médio quente
#     else:
#         return (0, 0, 1)  # Azul para frio

# Configurações iniciais de pygame e OpenGL
# def main():
#     pygame.init()
#     display = (800, 600)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
#     glTranslatef(0.0, 0.0, -5)

#     glClearColor(1.0, 1.0, 1.0, 1.0)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return

#         # Pega a temperatura do servidor
#         temperature = get_temperature()
#         color = get_cube_color(temperature)
        
#         # Rotaciona o cubo
#         glRotatef(1, 3, 1, 1)

#         # Limpa a tela
#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#         # Desenha o cubo com faces coloridas e edges pretos
#         draw_faces(color)
#         draw_edges()
        
#         pygame.display.flip()
#         pygame.time.wait(10)

# main()

# Configurações iniciais de pygame e OpenGL
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)  # Habilita o uso de texturas
    glEnable(GL_DEPTH_TEST)  # Habilita o teste de profundidade
    glDepthFunc(GL_LEQUAL)   # Define a função de comparação de profundidade


    temperature = 15.0  
    temp_increasing = True  
    time_factor = 0

    # Carrega as três texturas
    textures = {
        'cold': load_texture("/home/matheusg/Documents/UNASP/8°SEM/computacao_grafica/projeto_integrador/textura/agua.png"),   # Textura para frio
        'warm': load_texture("/home/matheusg/Documents/UNASP/8°SEM/computacao_grafica/projeto_integrador/textura/pedra.jpeg"),   # Textura para morno
        'hot': load_texture("/home/matheusg/Documents/UNASP/8°SEM/computacao_grafica/projeto_integrador/textura/lava.jpeg")      # Textura para quente
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        if temp_increasing:
            temperature += 0.1
            if temperature >= 40:
                temp_increasing = False
        else:
            temperature -= 0.1
            if temperature <= 15:
                temp_increasing = True


        time_factor += 0.1  # Incrementa o fator de tempo para animações

        print(f"Temperatura atual: {temperature:.1f}°C")
        # Obtem a temperatura do servidor
        # temperature = get_temperature()
        texture = get_texture_by_temperature(temperature, textures)
        
        # Rotaciona o cubo
        glRotatef(1, 3, 1, 1)

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenha o cubo com a textura correspondente à temperatura
        draw_textured_cube(texture)
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
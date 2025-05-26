import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import requests
import time

# URL do ESP com o valor da temperatura
url = "http://192.168.246.138/temperaturec"  # Coloque o IP do ESP32/ESP8266

# Função para pegar a temperatura atual do servidor
def get_temperature():
    try:
        response = requests.get(url)
        temperature = float(response.text.strip())
        return temperature
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ao ESP: {e}")
        return None
    except ValueError:
        print("Erro ao converter a resposta em número.")
        return None

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

# Define as arestas para desenhar o contorno do cubo
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7),
    (7, 6),
    (6, 4),
    (0, 4),
    (1, 5),
    (2, 7),
    (3, 6)
)

# Função para desenhar o cubo com faces coloridas
def draw_faces(color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# Função para desenhar as arestas do cubo em preto
def draw_edges():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Configuração de cor com base na temperatura
def get_cube_color(temperature):
    if temperature is not None and temperature > 28.0:
        return (1, 0, 0)  # Vermelho para quente
    elif temperature is not None and temperature > 25.0:
        return (1, 1, 0)  # Amarelo para médio quente
    else:
        return (0, 0, 1)  # Azul para frio

# Configurações iniciais de pygame e OpenGL
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glClearColor(1.0, 1.0, 1.0, 1.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Pega a temperatura do servidor
        temperature = get_temperature()
        color = get_cube_color(temperature)
        
        # Rotaciona o cubo
        glRotatef(1, 3, 1, 1)

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenha o cubo com faces coloridas e edges pretos
        draw_faces(color)
        draw_edges()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import random

def render_text_in_opengl(text, x, y, screen_width, screen_height):
    font = pygame.font.SysFont("Monospace", 15, True, True)
    text_surface = font.render(text, True, (255, 255, 255), (0, 0, 0))  # Texto com fundo preto
    texture_data = pygame.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_size()
    
    text_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, text_texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, screen_width, 0, screen_height)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, text_texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)
    glTexCoord2f(1, 0)
    glVertex2f(x + width, y)
    glTexCoord2f(1, 1)
    glVertex2f(x + width, y + height)
    glTexCoord2f(0, 1)
    glVertex2f(x, y + height)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glDeleteTextures(1, [text_texture])

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", True)
    width, height = texture_surface.get_size()
    
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    return texture_id

def get_sword_vertices():
    blade = [
        (0.05, 1.5, 0.05), (-0.05, 1.5, 0.05),
        (0.1, -0.5, 0.05), (-0.1, -0.5, 0.05),
        (0.1, -0.5, -0.05), (-0.1, -0.5, -0.05),
        (0.05, 1.5, -0.05), (-0.05, 1.5, -0.05)
    ]
    
    guard = [
        (0.4, -0.6, 0.15), (0.4, -0.8, 0.15), (-0.4, -0.8, 0.15), (-0.4, -0.6, 0.15),
        (0.4, -0.6, -0.15), (0.4, -0.8, -0.15), (-0.4, -0.8, -0.15), (-0.4, -0.6, -0.15)
    ]
    
    handle = [
        (0.1, -0.8, 0.1), (0.1, -1.3, 0.1), (-0.1, -1.3, 0.1), (-0.1, -0.8, 0.1),
        (0.1, -0.8, -0.1), (0.1, -1.3, -0.1), (-0.1, -1.3, -0.1), (-0.1, -0.8, -0.1)
    ]
    
    pommel = [
        (0.15, -1.3, 0.15), (0.15, -1.5, 0.15), (-0.15, -1.5, 0.15), (-0.15, -1.3, 0.15),
        (0.15, -1.3, -0.15), (0.15, -1.5, -0.15), (-0.15, -1.5, -0.15), (-0.15, -1.3, -0.15)
    ]
    
    return blade, guard, handle, pommel

texture_coords = [(0, 0), (1, 0), (1, 1), (0, 1)]

# função para desenhar as texturas
def draw_textured_faces(vertices, faces, texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_TEXTURE_2D)
    glColor4f(1, 1, 1, 1)  # Garante que a cor da textura não seja afetada
    glBegin(GL_QUADS)
    for face in faces:
        for i, vertex in enumerate(face):
            u, v = texture_coords[i % 4]  # Usa índices corretos para mapear coordenadas de textura
            glTexCoord2f(u, v)
            glVertex3fv(vertices[vertex])
    glEnd()
    glDisable(GL_TEXTURE_2D)


blade_faces = [
    (0, 1, 3, 2), (4, 5, 7, 6),  
    (0, 1, 7, 6), (2, 3, 5, 4),  
    (0, 2, 4, 6), (1, 3, 5, 7)
]

guard_faces = [
    (0, 1, 3, 2), (4, 5, 7, 6),
    (0, 2, 6, 4), (1, 3, 7, 5),
    (0, 1, 5, 4), (2, 3, 7, 6)
]

handle_faces = [
    (0, 1, 3, 2), (4, 5, 7, 6),
    (0, 2, 6, 4), (1, 3, 7, 5),
    (0, 1, 5, 4), (2, 3, 7, 6)
]

pommel_faces = [
    (0, 1, 3, 2), (4, 5, 7, 6),
    (0, 2, 6, 4), (1, 3, 7, 5),
    (0, 1, 5, 4), (2, 3, 7, 6)
]

edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),  
    (4, 5), (5, 7), (7, 6), (6, 4),  
    (0, 6), (1, 7), (2, 4), (3, 5)   
]

def draw_faces(vertices, faces, color):
    glColor4f(*color)
    glBegin(GL_QUADS)
    for face in faces:
        glNormal3f(0, 0, 1)  # Normal para superfícies planas; pode ser ajustado
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_edges(vertices):
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Função para desenhar chamas em 2D
def draw_2d_flames():
    glBegin(GL_TRIANGLES)
    for i in range(20):  # Quantidade de triângulos para simular as chamas
        base_x = random.uniform(-0.15, 0.15)  # Base da chama
        base_y = random.uniform(0.8, 1.5)     # Altura na lâmina
        offset = random.uniform(0.02, 0.05)   # Largura da chama
        height = random.uniform(0.1, 0.3)     # Altura da chama

        glColor3f(1.0, random.uniform(0.5, 1.0), 0.0)  # Cores variando entre amarelo e laranja

        # Triângulo representando a chama
        glVertex3f(base_x, 0.7, 0)
        glVertex3f(base_x - offset, base_y + height, 0)
        glVertex3f(base_x + offset, base_y + height, 0)
    glEnd()

def get_sword_color(temperature):
    if temperature < 20:
        return 'ice'
    elif 20 <= temperature <= 25:
        return 'gray'
    else:
        return 'lava'

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    ice_texture = load_texture("/home/matheusg/Documents/UNASP/8°SEM/computacao_grafica/projeto_integrador/textura/neve.jpg")
    lava_texture = load_texture("/home/matheusg/Documents/UNASP/8°SEM/computacao_grafica/projeto_integrador/textura/lava.jpeg")

    temperature = 15.0  
    temp_increasing = True  
    time_factor = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if temp_increasing:
            temperature += 0.1
            if temperature >= 30:
                temp_increasing = False
        else:
            temperature -= 0.1
            if temperature <= 15:
                temp_increasing = True

        time_factor += 0.1

        print(f"Temperatura atual: {temperature:.1f}°C")

        color = get_sword_color(temperature)

        glRotatef(1, 1, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        blade, guard, handle, pommel = get_sword_vertices()

        if color == 'ice':
            # textura de gelo
            draw_textured_faces(blade, blade_faces, ice_texture)
            # textura de lava
        elif color == 'lava':
            draw_textured_faces(blade, blade_faces, lava_texture)
            # cor cinza
        elif color == 'gray':
            draw_faces(blade, blade_faces, (0.6, 0.6, 0.6, 1))

        # Renderiza o texto como textura
        render_text_in_opengl(
            f"Temperatura: {temperature:.1f}°C", 
            50, 50,  # Posição do texto
            display[0], display[1]  # Dimensões da tela
        )

        draw_edges(blade)
        draw_faces(guard, guard_faces, (0.4, 0.4, 0.4, 1))
        draw_edges(guard)
        draw_faces(handle, handle_faces, (0.3, 0.3, 0.3, 1))
        draw_edges(handle)
        draw_faces(pommel, pommel_faces, (0.3, 0.2, 0.2, 1))
        draw_edges(pommel)
        
        if temperature > 25:
            # Desenha as chamas em 2D sobre a lâmina
            draw_2d_flames()

        pygame.display.flip()
        pygame.time.wait(10)
        time.sleep(0.05)

main()
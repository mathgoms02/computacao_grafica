import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicializa a fonte para exibir texto
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)

# Temperatura inicial
temperatura = 10
aumentando = True

def render_text_in_opengl(text, x, y, screen_width, screen_height):
    font = pygame.font.SysFont("Monospace", 20, True, True)
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

# Função para desenhar o termômetro
def desenhar_termometro():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configurar a câmera
    gluLookAt(0, -5, 3,  # Posição da câmera
              0, 0, 1,  # Para onde está olhando
              0, 0, 1)  # Vetor "up"

    # Desenhar o fundo
    desenhar_fundo()

    # Desenhar o líquido no termômetro (desenhado antes do corpo translúcido)
    desenhar_liquido(temperatura)

    # Desenhar o corpo do termômetro
    desenhar_corpo()

    glFlush()

# Função para desenhar o fundo
def desenhar_fundo():
    glBegin(GL_QUADS)
    glColor3f(0.1, 0.2, 0.3)  # Gradiente de cor
    glVertex3f(-5, -3, 0)
    glVertex3f(5, -3, 0)
    glColor3f(0.2, 0.3, 0.4)  # Gradiente mais claro
    glVertex3f(5, 3, 0)
    glVertex3f(-5, 3, 0)
    glEnd()

# Função para desenhar o corpo do termômetro
def desenhar_corpo():
    # Tornar o corpo do termômetro translúcido
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(1, 1, 1, 0.1)  # Branco translúcido com maior transparência

    # Corpo principal
    glPushMatrix()
    glTranslatef(0, 0, -1)  # Posicionar no fundo do termômetro
    gluCylinder(gluNewQuadric(), 0.2, 0.2, 2.5, 32, 32)  # Corpo do termômetro
    glPopMatrix()

    # Base arredondada translúcida
    glPushMatrix()
    glTranslatef(0, 0, -1.5)
    gluSphere(gluNewQuadric(), 0.3, 32, 32)  # Base arredondada
    glPopMatrix()

    glDisable(GL_BLEND)  # Desabilitar transparência para outras partes

# Função para desenhar o líquido do termômetro
def desenhar_liquido(temp):
    # Altura do líquido proporcional à temperatura
    altura_liquido = max((temp - 10) / 50.0 * 3.0, 0.05)

    # Tornar o líquido translúcido
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Ajustar a cor do líquido conforme a temperatura
    if temp <= 20:
        # Faixa verde (10°C até 20°C)
        r = 0  # Nenhum vermelho
        g = 1 - (20 - temp) / 20.0 # Totalmente verde
        b = 0  # Nenhum azul
    elif temp <= 40:
    # Faixa de transição (20°C até 40°C) - De verde para amarelo
        r = 0  
        g = 1 - (temp - 20) / 20.0  # Verde diminui até 0 (a transição de verde para amarelo)
        b = 0  # Azul permanece 0 durante a transição para amarelo
    elif temp <= 60:
        # Faixa vermelha (40°C até 60°C) - De amarelo para vermelho
        r = 1  # Vermelho total
        g = (60 - temp) / 20.0  # Verde diminui conforme a temperatura sobe
        b = 0  # Nenhum azul
    else:
        # Temperatura acima de 60°C
        r = 1  # Vermelho total
        g = 0  # Nenhum verde
        b = 0  # Nenhum azul

    # Aplicar cor com transparência
    glColor4f(r, g, b, 5)

    # Desenhar o líquido no tubo principal
    glPushMatrix()
    glTranslatef(0, 0, -1.5)
    gluCylinder(gluNewQuadric(), 0.18, 0.18, altura_liquido, 32, 32)
    glPopMatrix()

    # Desenhar a base do líquido (esfera arredondada na parte de baixo)
    glPushMatrix()
    glTranslatef(0, 0, -1.5)
    gluSphere(gluNewQuadric(), 0.18, 32, 32)
    glPopMatrix()

    # Desativar blend para o restante da cena
    glDisable(GL_BLEND)





def atualizar_temperatura():
    global temperatura, aumentando

    # Controlar o aumento e a diminuição da temperatura mais devagar
    if aumentando:
        temperatura += 0.05  # Incremento menor para suavizar o movimento
        if temperatura >= 60:
            aumentando = False
    else:
        temperatura -= 0.05
        if temperatura <= 10:
            aumentando = True


# Função principal
def main():
    pygame.init()
    display = (800, 800)
    largura, altura = 800, 600
    pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("Termômetro 3D")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.2, 0.3, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, largura / altura, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            elif evento.type == VIDEORESIZE:
                largura, altura = evento.w, evento.h
                glViewport(0, 0, largura, altura)
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(45, largura / altura, 0.1, 50.0)
                glMatrixMode(GL_MODELVIEW)

        atualizar_temperatura()
        desenhar_termometro()
        render_text_in_opengl(
            f"Temperatura: {temperatura:.1f}°C", 
            50, 50,  # Posição do texto
            display[0], display[1]  # Dimensões da tela
        )
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
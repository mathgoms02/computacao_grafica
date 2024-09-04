#síntese
import pygame
from IPython.display import display
from PIL import Image
import io

pygame.init()

window_size = (400,300)
screen = pygame.Surface(window_size)
screen.fill((255,255,255,255))

# Desenhando uma imagem simples
pygame.draw.circle(screen,(255,0,0), (200,150), 75)

# Trabalhando com a biblioteca Pillow para adicionar os canais RGB
image_string = pygame.image.tostring(screen, 'RGB')
image = Image.frombytes('RGB', window_size, image_string)
buffer = io.BytesIO()
image.save(buffer, format='PNG')
buffer.seek(0)

display(Image.open(buffer))
pygame.quit()

image.show()
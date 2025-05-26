import cv2
import numpy as np
import matplotlib.pyplot as plt

# criar bordas serrilhadas e padrões moire
def aplicar_borda_serrilhada(imagem):
    altura, largura = imagem.shape[:2]
    serrilhada = imagem.copy()

    # aplicando efeito
    for i in range(0, altura, 5): #altura
        for j in range(0, largura, 5):
            serrilhada[i:i+2, j:j+2]
    return serrilhada

# filtro (solução pra bordas serrilhadas, tentando corrigir imagem)
def filtro_passa_alta(imagem):
    sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(sobel_x**2 + sobel_y**2) #calculando magnitude das bordas

    return cv2.convertScaleAbs(sobel)

# filtro para suavizar imagem
def filtro_passa_baixa(imagem, tipo='gaussiano', kernel_size=5):
    if tipo == 'gaussiano':
        return cv2.GaussianBlur(imagem, (kernel_size, kernel_size), 0)
    elif tipo == 'mediana':
        return cv2.medianBlur(imagem, kernel_size)
    
caminho_imagem = "image/jedi.png"
imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

if imagem is None:
    print("Erro ao carregar a imagem")
else:
    imagem_serrilhada = aplicar_borda_serrilhada(imagem)
    imagem_passa_alta = filtro_passa_alta(imagem_serrilhada)
    imagem_suavizada = filtro_passa_baixa(imagem_passa_alta, tipo='mediana', kernel_size=5)

caminho_serrilhada = 'image/imagem_serrilhada.jpg'
caminho_passa_alta = 'image/imagem_passa_alta.jpg'
caminho_suavizada = 'image/imagem_suavizada.jpg'

cv2.imwrite(caminho_serrilhada, imagem_serrilhada)
cv2.imwrite(caminho_passa_alta, imagem_passa_alta)
cv2.imwrite(caminho_suavizada, imagem_suavizada)
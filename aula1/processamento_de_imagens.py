from PIL import Image
import io
import os
import matplotlib.pyplot as plt
# from google.colab import files

def convert_to_bicolor(image):
    grayscale_image = image.convert("L")

    threshold = 128
    bicolor_image = grayscale_image.point(lambda p:p > threshold and 255)

    return bicolor_image

# uploaded = files.upload()
# image_name = next(iter(uploaded))

image_path = "images/eu.jpeg"

with Image.open(image_path) as img:
    bicolor_image = convert_to_bicolor(img)

    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title("Imagem Original")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title("Imagem Coisada")
    plt.imshow(bicolor_image, cmap='gray')
    plt.axis('off')

    plt.show()
import matplotlib.pyplot as plt

pontos = [(0,0),(0,2),(2,2),(2,0)]

x = [p[0] for p in pontos]
y = [p[1] for p in pontos]

x.append(pontos[0][0]) # Adicionando o primeiro ponto x(0) ao final da minha lista
y.append(pontos[0][1]) # Adicionando o primeiro ponto y(0) ao final da minha lista

plt.plot(x,y, marker='o')

plt.title('Quadrado no plano cartesiano')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.axis("equal")
plt.show()
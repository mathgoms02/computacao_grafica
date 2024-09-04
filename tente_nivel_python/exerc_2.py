"""
2 - Escreva um programa que receba um número do usuário e determine se ele é par ou ímpar.
"""
print('### VERIFICADOR PAR/IMPAR ###')

num = int(input('Digite um número: '))

if num % 2 == 0:
    print('Seu número é par')
else:
    print('Seu número é impar')
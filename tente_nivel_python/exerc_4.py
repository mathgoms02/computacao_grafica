"""
4 - Escreva um programa que verifique se uma palavra é um palíndromo (palavra que se lê da
mesma forma de trás para frente).
"""

palavra = input('Digite uma palavra: ')

print('palavra || contrário')

palavra_contrario = []
contador_reverso = 0
for letra in palavra:
    contador_reverso -= 1
    if letra == palavra[contador_reverso]:
        print(f'      {letra} || {palavra[contador_reverso]}')
        palavra_contrario += palavra[contador_reverso]
    else:
        print(f'Num é')
        break

    if len(palavra) == len(palavra_contrario):
        print('Parabens, viu, ao contrário fica a mesma coisa')

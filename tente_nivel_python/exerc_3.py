"""
3 - Escreva um programa que funcione como uma calculadora simples. O programa deve pedir
ao usuário dois números e a operação (adição, subtração, multiplicação ou divisão) e exibir o
resultado.
"""

while True:
    numeros_validos = None

    try:
        num1 = float(input('Digite um valor: '))
        op = input('Digite um Operador (+ - / *): ')
        num2 = float(input('Digite outro valor: '))
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos')
        continue

    operadores_permitidos = '+-*/'

    if op not in operadores_permitidos:
        print('Operador Inválido')
        continue
    if len(op) > 1:
        print('Digite apenas um operador')
        continue

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print('Digite um operador válido:')

    print(result)

    sair = input('\nDeseja sair? ').lower().startswith('s')

    if sair is True:
        break
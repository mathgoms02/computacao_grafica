"""
5 - Escreva um programa que ordene uma lista de números fornecida pelo usuário. O programa
deve solicitar os números até que o usuário insira um valor vazio e então exibir a lista
ordenada.
"""

skip = ''
nums_int = []

nums = input("Faça uma lista de números separados por virgula: ")
nums = nums.split(',')

for i in nums:
    nums_int.append(int(i))

nums_int.sort()

print(nums_int)
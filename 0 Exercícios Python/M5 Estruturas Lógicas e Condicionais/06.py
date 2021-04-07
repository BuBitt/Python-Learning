"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior
deles assim como a diferença existente entre ambos.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro:'))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)

if num1 > num2:
    print(f'A diferença entre {num1} e {num2} é {num1 - num2}.')
else:
    print(f'A diferença entre {num2} e {num1} é {num2 - num1}.')

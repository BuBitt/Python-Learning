"""
Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes medidas de acordo com um valor numérico
digitado pelo usuário:
"""


def cubic_root(x):
    return x ** (1/3)


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

print(f'Média Geométrica: {cubic_root(num1 * num2 * num3)}')
print(f'Média Ponderada: {(num1 + 2 * num2 + 3 * num3) / 6}')
print(f'Média Harmônica: {1 / ((1 / num1) + (1 / num2) + (1 / num3))}')
print(f'Média Aritmética: {(num1 + num2 + num3) / 3}')

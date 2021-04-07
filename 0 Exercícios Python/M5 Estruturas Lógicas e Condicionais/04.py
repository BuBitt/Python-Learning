"""
Faça um programa que leia um número e, caso ele seja positivo,
calcule e mostre:

    - O número digitado ao quadrado.
    - A raiz quadrada do número digitado.
"""
from math import sqrt

num = float(input('Digite um número: '))

if num > 0:
    print(sqrt(num))
    print(num ** 2)
else:
    print('O número digitado é negativo.')

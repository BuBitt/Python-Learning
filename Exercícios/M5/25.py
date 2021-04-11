"""
Calcule as raízes da equação do 2º grau.

x = (-b +- sqrt(delta)) / 2

delta = (b ** 2) - 4 * a * c
"""
from math import sqrt

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = (b ** 2) - 4 * a * c

if delta > 0:
    x1 = (-b + sqrt(delta)) / 2
    x2 = (-b - sqrt(delta)) / 2
    print(f'\nAs raízes da equação são {x1} e {x2}.')

elif delta == 0:
    x = (-b) / 2
    print(f'\nRaiz única {x}')

else:
    print('\nNão existe raiz.')

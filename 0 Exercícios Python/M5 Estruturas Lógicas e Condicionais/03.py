"""
Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""
from math import sqrt

# Input: Número real
num = float(input('Digite um número real: '))

# Processamento: raiz quadrada e quadrado do número.
if num > 0:
    print(sqrt(num))
else:
    print(num ** 2)

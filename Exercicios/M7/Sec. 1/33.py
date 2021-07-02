"""
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja,
elimine as posições com valor 0. Para isso, todos os elementos à frente
do valor 0, devem ser movidos uma posição atras no vetor.
"""
from random import randrange


v = []


for i in range(15):
    v.append(randrange(100))

print(v)

v.pop(0)

print(v)

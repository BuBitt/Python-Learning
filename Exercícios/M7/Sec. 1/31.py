"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união
entre os 2 vetores anteriores, ou seja, contém os números dos dois vetores. Não deve
conter números repetidos.
"""
from random import randrange


v1 = set()
v2 = set()


for i in range(10):
    v1.add(randrange(100))
    v2.add(randrange(100))

i = v1 | v2

print(i)
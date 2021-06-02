"""
Leia um vetor com 10 números reais, ordene os elementos deste vetor,
e no final escreva os elementos do vetor ordenado.
"""
from random import randrange


vetor = []


for i in range(10):
    vetor.append(randrange(1000))


print(vetor)
vetor.sort()


for i, v in enumerate(vetor):
    print(v, end=", ")

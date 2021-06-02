"""
Faça um programa que leia 2 vetores de 10 elementos. crie um vetor que seja a intersecção entre
os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores.
Não deve conter números repetidos.
"""
from random import randrange


v1 = set()
v2 = set()
v = []


while len(v1) or len(v2) < 10:
    if len(v1) < 10:
        v1.add(randrange(10))

    elif len(v2) < 10:
        v2.add(randrange(10))

    else:
        break

print(v1)
print(v2)


i = v1 & v2

if i == set(v):
    print("Os vetores não possuem nenhuma intersecção.")
else:
    print(f"A interseção entre os 2 vetores é: {i}.")

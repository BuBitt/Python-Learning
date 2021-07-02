"""
Leia um vetor de 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores impares de v para v1, e os valores pares de v para v2. Note que cada um dos
vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são utilizados.
No final escreva os elementos UTILIZADOS de v1 e v2.
"""
from random import randrange


v = []
v_1 = []
v_2 = []


for i in range(10):
    v.append(randrange(1000))


for i, va in enumerate(v):
    if va % 2 == 0:
        v_1.append(va)
    else:
        v_2.append(va)

print(f'Em v1 foram utilizados {len(v_1)} elementos, e em v2, {len(v_2)} elementos.')

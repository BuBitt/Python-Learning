"""
Faça um programa que leia 10 conjuntos de 2 valores, o primeiro representando número do aluno
e o segundo representando sua altura em metros, Encontre o aluno mais baixo e o mais alto.
Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
"""
from random import random


l_maior = []
l_menor = []
n = []

maior = 0


#  Gerar os conjuntos de 2 valores aleatoriamente
for p in range(10):
    t_ = []
    n_gen = round(1 + random(), 2)
    t_.append(p + 1)
    t_.append(n_gen)
    n.append(t_)
print(n)


for p in range(10):
    temp_list_max = n[p]
    v_t = int(temp_list_max[1] * 100)

    if v_t > maior:
        maior = v_t
        l_maior = temp_list_max

menor = maior
for p in range(10):
    temp_list_min = n[p]
    v_t = int(temp_list_min[1] * 100)

    if v_t < menor:
        menor = v_t
        l_menor = temp_list_min

print(f'O aluno número {l_maior[0]} é o mais alto, com {l_maior[1]}m.')
print(f'O aluno número {l_menor[0]} é o mais baixo, com {l_menor[1]}m.')

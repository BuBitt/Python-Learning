"""
Faça um programa que leia uma matriz de 3 x 6 com valores reais:

(a) Imprima a soma de todos os elementos das colunas ímpares
(b) Imprima a média aritimética dos elementos da segunda e quarta colunas.
(c) Subistitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a matriz modificada.
"""
from random import randrange


k = 0
v = []  # Vetor da matriz
a = []  # Vetor de (a)
b = []  # vetor de (b)
c = []  # Vetor de (c)


# *Gerando Matriz:
for i in range(3):
    local = []
    for j in range(6):
        local.append(randrange(10, 99))
    v.append(local)
print()

for i in range(3):
    for j in range(6):
        print(v[i][j], end=" ")
    print()
print()


# *Fazendo (a):
for i in range(6):
    for j in range(3):

        if i == 0:
            k += v[j][i]

        elif i % 2 == 0:
            k += v[j][i]

    a.append(k)


# *Fazendo (b):
for i in range(6):
    som = 0

    for j in range(3):
        if i % 2 == 1:
            som += v[j][i]

    if i % 2 == 1:
        b.append(som)

    if i == 3:
        break


# *Fazendo (c):
for i in range(3):
    v[i][5] = v[i][0] + v[i][1]


# !(a):
print("a:")
print(k)
print()


# !(b):
print("b:")
for i in range(2):
    print(b[i], end=" ")
print()
print()


# *Fazendo (d):
print("d:")
for i in range(3):
    for j in range(6):
        print(v[i][j], end=" ")
    print()

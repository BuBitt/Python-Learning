"""
Faça um programa que leia duas matrizes A e B de tamanho 3x3 e calcule C = A * B.
"""
from random import randrange


a = []
b = []
c = []


# *Gerando A:
for i in range(3):
    local = []
    for j in range(3):
        local.append(randrange(10, 99))
    a.append(local)


# *Gerando B:
for i in range(3):
    local = []
    for j in range(3):
        local.append(randrange(10, 99))
    b.append(local)


# *Gerando C = A * B:
for i in range(3):
    local = []
    for j in range(3):
        local.append(a[i][j] * b[i][j])
    c.append(local)


# !Construindo matriz A:
for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()
print()


# !Construindo matriz B:
for i in range(3):
    for j in range(3):
        print(b[i][j], end=" ")
    print()
print()


# !Construindo matriz C:
for i in range(3):
    for j in range(3):
        print(c[i][j], end=" ")
    print()
print()

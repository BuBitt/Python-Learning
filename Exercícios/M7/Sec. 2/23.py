"""
Faça um programa que leia uma matriz A de tamanho 3x3 e calcule B = A².
"""
from random import randrange


a = []
b = []


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
        local.append(a[i][j] * a[i][j])
    b.append(local)


# !Construindo A:
print("A:")
for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()
print()

# !Construindo B:
print("B:")
for i in range(3):
    for j in range(3):
        print(b[i][j], end=" ")
    print()
print()

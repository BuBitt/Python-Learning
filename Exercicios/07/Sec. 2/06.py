"""
Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição
das matrizes lidas.
"""
from random import randrange


m1 = []
m2 = []
mf = []


# Gerando e imprimindo primeira matriz:
print("\nPrimeira Matriz:")
for i in range(4):
    local = []
    for j in range(4):
        local.append(randrange(10, 99))
    m1.append(local)

for i in range(4):
    for j in range(4):
        print(m1[i][j], end=" ")
    print()
print()
print()


# Gerando e imprimindo sefunda matriz:
print("Segunda Matriz:")
for i in range(4):
    local = []
    for j in range(4):
        local.append(randrange(10, 99))
    m2.append(local)

for i in range(4):
    for j in range(4):
        print(m2[i][j], end=" ")
    print()
print()
print()


# Gerando matriz final:
print("Matriz Resultante:")
for i in range(4):
    local = []
    for j in range(4):
        if m1[i][j] > m2[i][j]:
            local.append(m1[i][j])
        else:
            local.append(m2[i][j])
    mf.append(local)

for i in range(4):
    for j in range(4):
        print(mf[i][j], end=" ")
    print()
print()

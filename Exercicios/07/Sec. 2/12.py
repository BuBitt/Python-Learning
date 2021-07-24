"""
Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.
"""
from random import randrange


m = []
mt = []


# Matriz:
print("Matriz:")
for i in range(3):
    local = []
    for j in range(3):
        local.append(randrange(10, 99))
    m.append(local)

# Impressão da matriz:
for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()
print()


# Matriz transposta:
print("Matriz Transposta:")
for i in range(3):
    local = []
    for j in range(3):
        local.append(m[j][i])
    mt.append(local)

# Impressão da matriz transposta:
for i in range(3):
    for j in range(3):
        print(mt[i][j], end=" ")
    print()
print()

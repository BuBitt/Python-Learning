"""
Leia uma matriz 3 x 3 elementos. Calcule a soma dos elementos que estão abaixo
da diagonal principal.
"""
from random import randrange


m = []
k = 0


for i in range(3):
    local = []
    for j in range(3):
        local.append(randrange(10, 99))
    m.append(local)

for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()
print()


for i in range(3 - 2):
    for j in range(3 - 2):
        k = m[i + 1][j] + m[i + 2][j + 1]
print(f"A soma dos termos abaixo da diagonal é {k}.")

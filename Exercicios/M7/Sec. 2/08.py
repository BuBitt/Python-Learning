"""
Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da
diagonal principal.
"""
from random import randrange


m = []


# Gerando Matriz:
for i in range(3):
    local = []
    for j in range(3):
        local.append(randrange(10, 99))
    m.append(local)
print()

for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()
print()


# Gerando soma dos números acima da diagonal:
for i in range(3 - 2):
    for j in range(3 - 2):
        k = m[i][j + 1] + m[i + 1][j + 2]
print(f"A soma dos números acima da diagonal é {k}.")

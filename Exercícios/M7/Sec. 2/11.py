"""
Leia uma matriz 3 x 3 eementos. Calcule a soma dos elementos que estão
na diagonal secundária.
"""
from random import randrange


m = []
k = 00


# Gerando matriz:
for i in range(3):
    local = []
    for j in range(3):
        local.append(randrange(10, 99))
    m.append(local)

for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()


# Gerando soma reversa:
m = m[::-1]

for i in range(3):
    for j in range(3):
        if i == j:
            k += m[i][j]

print(f"\nA soma da diagonal secundária é {k}.")

"""
Leia uma matriz de 3 x 3. Calcule a soma dos elementos que estão
na diagonal principal.
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


for i in range(3):
    for j in range(3):
        if i == j:
            k += m[i][j]

print(f"\nA soma dos termos da diagonal é {k}.")

"""
Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna)
do maior valor.
"""
from random import randrange


m = []
maior = [0, 1]
mm = 0


for i in range(4):
    add = []
    for j in range(4):
        add.append(randrange(10, 99))
    m.append(add)


for i in range(4):
    for j in range(4):
        vef = m[i][j]

        if vef > mm:
            mm = vef
            maior[0] = i + 1
            maior[1] = j + 1
print()


for i in range(4):
    for j in range(4):
        print(m[i][j], end=" ")
    print()


print(f"\nO Maior valor se encontra na lina {maior[0]} e coluna {maior[1]}.")

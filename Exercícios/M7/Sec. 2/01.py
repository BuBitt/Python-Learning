"""
Leia uma matriz de 4 x 4, conte e escreva quantos valores maiores que 10 possui.
"""
from random import randrange


m = []
m_10 = []


for i in range(4):
    mg = []

    for j in range(4):
        mg.append(randrange(15))
    m.append(mg)


print(m, '\n')


for i in range(4):
    for j in range(4):
        print(m[i][j], end=" ")
    print()
print()


for i in range(4):
    for j in range(4):
        if m[i][j] > 10:
            m_10.append(m[i][j])

print(f'Na matriz existem {len(m_10)} valores maiores que 10.')

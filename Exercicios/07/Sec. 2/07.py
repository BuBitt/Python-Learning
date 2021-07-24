"""
Gerar uma matriz tamanho 10 x 10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i² - 1 se i = j;
A[i][j] = 4i³ - 5j² + 1 se i > j.
"""
from random import randrange


m = []


# Gerando matriz primária:
for i in range(10):
    local = []
    for j in range(10):
        local.append(randrange(10, 99))
    m.append(local)

for i in range(10):
    for j in range(10):
        print(m[i][j], end=" ")
    print()
print()


# Gerando matriz condicional:
for i in range(10):
    for j in range(10):
        if i < j:
            m[i][j] = 2 * i + 7 * j - 2

        elif i == j:
            m[i][j] = 3 * (i ** 2) - 1

        elif i > j:
            m[i][j] = 4 * (i ** 3) - 5 * (j ** 2) + 1

for i in range(10):
    for j in range(10):
        print(m[i][j], end=" ")
    print()
print()

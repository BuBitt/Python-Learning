"""
Gere uma matriz 4 x 4 com valores no intevalor [1,20]. Escreva um programa que Trabalhando
a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os
elementos acima da diagonal principal. imprima a matriz original e a matriz transformada.
"""
from random import randrange


m = []


# Matriz original:
for i in range(4):
    local = []
    for j in range(4):
        local.append(randrange(1, 20))
    m.append(local)

for i in range(4):
    for j in range(4):
        print(m[i][j], end=" ")
    print()

print()

# Matriz transformada:
for i in range(4):
    for j in range(4):
        if i != j:
            m[i][j] = 0

for i in range(4):
    for j in range(4):
        print(m[i][j], end=" ")
    print()

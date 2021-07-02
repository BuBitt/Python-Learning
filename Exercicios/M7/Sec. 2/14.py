"""
Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de
bingo. Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere estes
dados de modo a não ter números repetidos dentro das cartelas. O número deve exibir
na tela a cartela gerada.
"""
from random import randrange


local = []
m = set()
k = []


vef = 0


# Gerando conjunto de números (Não repetidos):
while len(m) < 25:
    m.add(randrange(1, 99))
m = list(m)

# Separando a lista compĺeta em listas menores:
while vef < 25:
    local.append(m[vef])
    vef += 1

    if len(local) == 5:
        k.append(local)
        local = []

# Montando a matriz:
for i in range(5):
    for j in range(5):
        print(k[i][j], end=" ")
    print()

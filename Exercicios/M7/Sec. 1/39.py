"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
linhas do chamado Triângulo de Pascal:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""


k = [[1], [1, 1], [1, 2, 1]]


n = int(input('Digite quantas linhas o Triângulo de Pascal terá: '))

for i in range(n - 3):

    for i in range(len(k)):
        lista = []

        if i > 1:
            lista.append(1)

            for j in range(len(k[i]) - 1):
                som = k[i][j] + k[i][j + 1]
                lista.append(som)

            lista.append(1)
    k.append(lista)


for i in range(n):
    for j in range(len(k[i])):
        print(k[i][j], end=" ")
    print()

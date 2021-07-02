"""
Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma
busca desse valor na matriz e, no final, escrever a localização (linha e coluna)
ou uma menságem de "Não encontrado".
"""
from random import randrange


vetor = []
aux = True


# Geração das linhas da matriz:
for i in range(5):
    local = []

    for j in range(5):
        local.append(randrange(10, 99))

    vetor.append(local)
print()


# Montagem das colunas da matriz:
for i in range(5):
    for j in range(5):
        print(vetor[i][j], end=" ")
    print()
print()


# Procura de termo na matriz.
pr = int(input("Digite o número que deseja procurar (entre 10 e 99): "))

for i in range(5):
    for j in range(5):

        if vetor[i][j] == pr:
            print(f"O valor {pr} está na linha {i + 1} e coluna {j + 1}.")
            aux = False
            break
if aux:
    print(f"\n{pr} não encontrado.")

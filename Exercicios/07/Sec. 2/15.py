"""
Leia uma matriz de 5 x 10 que se refere respostas de 10 questões de multipla escolha,
referentes a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de
respostas que podem ser a, b, c ou d. Seu programa deverá comparar as respostas de
cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a 
pontuação correspondente a cada aluno.
"""
from random import randrange


gab = ["a", "b", "c", "d", "a", "b", "d", "a", "b", "c"]
vet = []
resultado = []


# *Tradução do gabarito:
for i in range(10):
    if gab[i] == "a":
        gab[i] = 1

    elif gab[i] == "b":
        gab[i] = 2

    elif gab[i] == "c":
        gab[i] = 3

    elif gab[i] == "d":
        gab[i] = 4


# *Geração randomica da matriz de questões:
for i in range(5):
    local = []
    for j in range(10):
        local.append(randrange(1, 5))
    vet.append(local)

# !Construção da matriz acima:
for i in range(5):
    for j in range(10):
        print(vet[i][j], end=" ")
    print()
print()


# *Comparação e conversão de resultados:
for i in range(5):
    local = []
    for j in range(10):
        if vet[i][j] == gab[j]:
            vet[i][j] = 1
        else:
            vet[i][j] = 0

# !Construção da matriz acima:
for i in range(5):
    for j in range(10):
        print(vet[i][j], end=" ")
    print()
print()

# *Gerando vetor resultado:
for i in range(5):
    k = 0
    k = sum(vet[i])
    resultado.append(k)
print(resultado, "<- Resultado por aluno\n")

for i in range(5):
    print(f"O aluno {i + 1} teve {resultado[i]} acertos.")

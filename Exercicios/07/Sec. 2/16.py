"""
Faça um programa para corrigir uma prova com 10 questões de multipla escolha (a, b,
c, d ou e), em uma turma com 3 alunos. Cada questão vale 1 ponto. Leia o gabarito, e
para cada aluno leia sua matricula (número inteiro) e suas respostas. Calcule e escreva:
Para cada aluno, escreva sua matricula, suas respostas e sua nota. O percentual de
aprovação, assumindo média 7.0.
"""
from random import randrange


# Gabarito
"""
'a' == 1
'b' == 2
'c' == 3
'd' == 4
'e' == 5
"""
gab = []  # Vetor Gabarito
que = []  # Vetor Questões
corr = []  # Vetor Correção
res = []  # Vetor resultado
nota = []  # Apendando os dados pedidos
ap = 0


# * Gerando gabarito aleatoriamente:
for i in range(10):
    gab.append(randrange(1, 6))


# *Geração de respostas dos alunos:
for i in range(3):
    local = []
    for j in range(10):
        local.append(randrange(1, 6))
    que.append(local)


# *Geração do vetor correção:
for i in range(3):
    local = []
    for j in range(10):

        if que[i][j] == gab[j]:
            local.append(1)

        else:
            local.append(0)
    corr.append(local)


# *Calculo das respostas corretas por aluno:
for i in range(3):
    nota.append(sum(corr[i]))


# *Tradução do gabarito para letras:
for i in range(3):
    local = []
    for j in range(10):
        if que[i][j] == 1:
            que[i][j] = "A"

        elif que[i][j] == 2:
            que[i][j] = "B"

        elif que[i][j] == 3:
            que[i][j] = "C"

        elif que[i][j] == 4:
            que[i][j] = "D"

        elif que[i][j] == 5:
            que[i][j] = "E"


# *Apendando as respostas ao vetor final:
for i in range(3):
    res.append(que[i])


# * Gerando percentual de aprovação:
for i in range(3):
    if nota[i] > 7:
        ap += 1

# !Gerando output:
for i in range(3):
    print(
        f"O aluno de matrícula nº {i + 1}, com gabarito: {res[i]}, teve nota {nota[i]}."
    )
print()

print(f"O percentual de aprovação foi de {ap / len(nota)}.")

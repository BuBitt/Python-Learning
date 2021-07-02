"""
Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva
o número de alunos cuja a pior nota foi na prova 1, o número de alunos cuja a pior
nota foi na prova 2, e o número de alunos cuja a pior nota foi na prova 3. Em caso
de empate das piores notas de um aluno, o critério de desempate é arbitrário, mas
o aluno deve ser contabilizado apenas uma vez.
"""
from random import randrange


v = []
n1 = 0
n2 = 0
n3 = 0


# *Gerando vetor da matriz:
for i in range(10):
    local = []

    for j in range(3):
        local.append(randrange(1, 9))
    v.append(local)


# *Verificação dos números da matriz:
for i in range(10):
    for j in range(3 - 2):
        k = v[i]

        if k[j + 1] > k[j] < k[j + 2]:
            n1 += 1

        elif k[j] > k[j + 1] < k[j + 2]:
            n2 += 1

        elif k[j] == k[j + 1] or k[j] == k[j + 2] or k[j + 1] == k[j + 2]:
            n1 += 1

        else:
            n3 += 1

print(
    f"""
O número de alunos com a menor nota na 1ª prova é: {n1};
O número de alunos com a menor nota na 2ª prova é: {n2};
O número de alunos com a menor nota na 3ª prova é: {n3}.
"""
)

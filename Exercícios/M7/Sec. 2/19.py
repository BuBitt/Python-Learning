"""
Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes
informações sobre os alunos de uma disciplina, sendo todas as informações do tipo
iteiro:

    1 - Número da matrícula (use número inteiro);
    2 - média das provas
    3 - média dos trabalhados
    4 - nota final

Elabore um programa que:

(a) Leia as três primeiras informações de cada aluno
(b) Calcule a nota final como sendo a soma da média das provas e da média
    dos trabalhados
(c) Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe
    uma maior nota)
(d) Imprima a média aritimética das notas finais
"""
from random import randrange


m = []
maior = 0
mat_m = 0


for i in range(5):
    local = []
    local.append(i + 1)

    for j in range(2):
        local.append(randrange(1, 9))

    sm = local[1] + local[2]
    local.append(sm)
    m.append(local)
print()


for i in range(5):
    if m[i][3] > maior:
        maior = m[i][3]
        mat_m = m[i][0]

    elif m[i][3] == maior:
        maior = maior
        mat_m = mat_m

print(f"O aluno com maior nota foi o da matrícula {mat_m}.\n")

for i in range(5):
    media = m[i][3] / 2
    print(f"A média do aluno {m[i][0]} foi {media}.")

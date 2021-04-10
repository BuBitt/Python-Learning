"""
10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
calcule e imprima a média geral.
"""
notas = []

for aluno in range(1, 15 + 1):
    nota_aluno = int(input(f'Digite a nota do aluno {aluno}: '))
    notas.append(nota_aluno)
    media = sum(notas) / aluno
print(f'A média geral é: {media}')

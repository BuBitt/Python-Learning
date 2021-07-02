"""
Faça um algorítimo que calcule a média ponderada das notas de 3 provas
A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ao maior a 60 pontos.
"""
prova1 = float(input('Digite a nota da primeira prova (0 à 100): '))
prova2 = float(input('Digite a nota da segunda prova (0 à 100): '))
prova3 = float(input('Digite a nota da terceira prova (0 à 100): '))

mediap = ((prova1 * 1) + (prova2 * 1) + (prova3 * 2)) / 4

if mediap >= 60:
    print(f'O aluno foi aprovado com a nota {mediap}')
else:
    print(f'O aluno foi reprovado com a nota {mediap}')

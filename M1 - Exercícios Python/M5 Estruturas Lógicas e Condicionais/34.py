"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas
ocorre uma redução de conceito.
"""
nota = int(input('Digite a sua nota: '))
faltas = int(input('Digite o número de faltas: '))

if 9 <= nota <= 10:
    if faltas < 20:
        print('Conceito A.')
    else:
        print('Conceito B.')

if 7.5 <= nota <= 8.9:
    if faltas < 20:
        print('Conceito B.')
    else:
        print('Conceito C.')

if 5 <= nota <= 7.4:
    if faltas < 20:
        print('Conceito C.')
    else:
        print('Conceito D.')

if 4 <= nota <= 4.9:
    if faltas < 20:
        print('Conceito D.')
    else:
        print('Conceito E.')

if 0 <= nota <= 3.9:
    if faltas < 20:
        print('Conceito E.')
    else:
        print('Conceito E.')

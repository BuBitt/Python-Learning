"""
46. Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar
    acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o
    chute é menor ou maior que o número gerado. O programa acaba quando o usuário
    acerta o número gerado. O programa deve informar em quantas tentativas o número foi
    descoberto.
"""
import random as rd

i = 0
r = rd.randrange(1, 1000)

while True:
    i = int(input('\nEm qual número estou pensando? '))
    if i < r:
        print(f'O número que estou pensando é maior que {i}.')

    elif i > r:
        print(f'O número que estou pensando é menor que {i}')

    else:
        print('''|-------------------------|
| Parabéns, Você acertou! |
|-------------------------|''')
        break

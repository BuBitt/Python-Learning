"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7
e imprima o dia da semana corresponde a este número.
isto é, Domingo 1, segunda 2 e assim por diante
"""
num = int(input('Digite um número de 1 a 7: '))

if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda-feira')
elif num == 3:
    print('Terça-feira')
elif num == 4:
    print('Quarta-feira')
elif num == 5:
    print('Quinta-feira')
elif num == 6:
    print('Sexta-feira')
elif num == 7:
    print('Sábado')
else:
    print('Não é um número válido.')

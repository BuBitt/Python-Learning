"""
Escreva um programa que, dada a idade de um nadador, classifique-o
em uma das seguintes categorias

Categoria    idade
infantil A   5 a 7
infantil B   8 a 10
juvenil A    11 a 13
juvenil B    14 a 17
Sênior       maiores de 18
"""
idade = int(input('Digite a idade: '))

if 5 <= idade <= 7:
    print('Você está na categoria Infantil A.')
elif 8 <= idade <= 10:
    print('Você está na categoria Infantil B.')
elif 11 <= idade <= 13:
    print('Você está na categoria Juvenil A.')
elif 14 <= idade <= 17:
    print('Você está na categoria Juvenil B.')
elif idade >= 18:
    print('Você está na categoria Sênior.')
else:
    print('Essa idade não faz parte de nenhuma categotia')

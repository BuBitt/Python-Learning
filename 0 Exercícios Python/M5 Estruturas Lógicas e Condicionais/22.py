"""
Leia o tempo de trabalho de um trabalhador e escreva se ele
pode ou não se aposentar. As condições são:

    - Ter pelo menos 65 anos.
    - Ou ter trabalhado pelo menos 30 anos.
    - ou ter pelo menos 60 anos e trabalhado 25 anos.
"""
idade = int(input('> Digite sua idade: '))
temptrab = int(input('> Digite o seu tempo de trabalho: '))

if idade >= 65 or temptrab == 30 or idade >= 60 and temptrab == 25:
    print('Você pode se aposentar.')
else:
    print('Você não pode se aposentar.')

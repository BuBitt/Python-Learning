"""
Faça um programa que mostre ao usuário um menu com 4 opções de oprações
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções
e o seu programa então pede valores númericos e realiza a operação,
mostrando o resultado e saindo.
"""
opbas = int(input('''
1 - Soma    2 - Subtração    3 - Multiplicação    4 - Divisão
> '''))

if opbas == 1:
    num1 = float(input('Primeiro número da soma: '))
    num2 = float(input('Segundo número da soma: '))

    soma = num1 + num2
    print(f'A soma de {num1} e {num2} é {soma}.')
elif opbas == 2:
    num1 = float(input('Primeiro número da subtração: '))
    num2 = float(input('Segundo número da subtração: '))

    sub = num1 - num2
    print(f'A subtração de {num1} e {num2} é {sub}.')
elif opbas == 3:
    num1 = float(input('Primeiro número da multiplicação: '))
    num2 = float(input('Segundo número da multiplicação: '))

    mult = num1 * num2
    print(f'A multiplicação de {num1} e {num2} é {mult}.')
else:
    num1 = float(input('Primeiro número da divisão: '))
    num2 = float(input('Segundo número da divisão: '))

    div = num1 / num2
    print(f'A divisão de {num1} e {num2} é {div}.')

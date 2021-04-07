"""
54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o número
    fornecido é primo ou não.
"""
num = 1

while num > 0:
    print('\nDigite "0" para sair do programa.')
    num = int(input('Digite um número: '))
    if num == 0:
        print('Você saiu do Programa.')

    elif num == 2 or num == 3 or num == 5 or num == 7:
        print(f'{num} é primo.')

    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(f'{num} não é primo')

    else:
        print(f'{num} é primo.')

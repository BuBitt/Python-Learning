"""
Faça um programa para verificar se um determinado número inteiro
é divisivel por 3 ou 5, mas não simultaneamente pelos dois.
"""
num = int(input('Digite um número para a verificação: '))

if (num % 5) == 0:
    print(f'{num} é divisivel por 5.')
else:
    print(f'{num} não é divisível por 5.')

if (num % 3) == 0:
    print(f'{num} é divisível por 3.')
else:
    print(f'{num} não é divisível por 3.')

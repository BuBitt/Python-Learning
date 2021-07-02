"""
7. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média.
"""
soma = 0
t_break = 0
c_b = 0

while t_break != 10:
    val = int(input('Digite um número inteiro positivo: '))

    if val >= 0:
        soma += val
        t_break += 1

    else:
        t_break += 0
        print('Número não positivo.\n')


print(f'\nA média dos 10 números positivos é {soma / 10}')

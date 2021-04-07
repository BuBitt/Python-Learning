"""
32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como
    saida o número de cada dado e a relação entre eles (>,<,=) de cada lançamento.
"""
import random


n_lancamento = int(input('Digite quantas vezes o dado será lançado: '))
for lancamento in range(1, n_lancamento + 1):
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    print(f'\nLançamento {lancamento}:')
    print(f'd1 = {d1} | d2 = {d2}')

    if d1 > d2:
        print(f'd1({d1}) é maior que d2({d2})')

    elif d1 == d2:
        print(f'd1({d1}) é igual a d2({d2})')

    else:
        print(f'd2({d2}) é maior que d1({d1})')

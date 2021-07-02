"""
Faça um programa que receba 6 números inteiros e mostre:
    1 - Os números pares digitados;
    2 - A soma dos números pares digitados;
    3 - Os números ímpares digitados;
    4 - A quantidade de números ímpares digitados.
"""
from random import randrange


v = []
n_p_dig = []
n_i_dig = []


for i in range(6):
    v.append(randrange(100))


for i, va in enumerate(v):
    if va % 2 == 0:
        n_p_dig.append(va)
    else:
        n_i_dig.append(va)

print(f'Os números pares recebidos {n_p_dig}, e sua soma é {sum(n_p_dig)}.')
print(f'Os números ímpares recebidos foram {n_i_dig}, e sua quantidade é {len(n_i_dig)}.')

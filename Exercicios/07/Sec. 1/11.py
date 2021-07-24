""""
Faça um programa que preencha um vetor com 10 números reais, calcule e motre a
quantidade de números negativos e a soma dos números positivos desse valor.
"""
from random import randrange

nl = []
l_b = []
l_n = []
som = 0

for loop in range(1, 11, 1):
    num = randrange(-100, 100)
    nl.append(num)

    if num < 0:
        l_n.append(num)
    else:
        som += num

print(f'Os únúmeros do vetor são:', end=' ')
for n in range(0, 10, 1):
    print(nl[n], end=' ')

print('\n')
print(f'A soma dos números positivos do vetor é: {som}')
print(f'O vetor possui {len(l_n)} números negativos')

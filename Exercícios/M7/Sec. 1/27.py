"""
Leia 10 números inteiro e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respectivas posições no vetor.
"""
from random import randrange


v = []


for i in range(10):
    if i == 0:
        num = int(input("Digite um número: "))
    else:
        num = int(input("Digite mais um número: "))

    v.append(num)
print(v)


for i in range(10):
    temp = v[i]

    for p in range(2, temp - 1):
        if temp % p == 0 or temp == 0 or temp == 1:
            break
    else:
        print(f'O número {temp}, na posição {i} é primo.')

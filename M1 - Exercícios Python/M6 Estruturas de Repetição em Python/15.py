"""
15. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
    números impares de 1 até N em ordem crescente.
"""
# Versão for
i_num = int(input('Digite um número inteiro impar: '))

for num in range(1, i_num + 2, 2):
    print(num)


# Versão while
w_i_num = int(input('Digite um número inteiro impar: '))
f_num = 1

while f_num != w_i_num + 2:
    print(f_num)
    f_num += 2

"""
16. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
    números impares de 1 até N em ordem decrescente.
"""
f_num = int(input('Digite um número inteiro impar positivo: '))

for num in range(f_num, - 1, -2):
    print(num)


f_num = int(input('Digite um número inteiro impar positivo: '))

while f_num != -1:
    print(f_num)
    f_num -= 2

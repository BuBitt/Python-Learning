"""
27. Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmónica:
H(n) = 1 + 1/2 + 1/3 + 1/4 +.. +1/n

Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
h_max = int(input('Digite um número n de H(n) para um série harmônica: '))
n = 0

for num in range(2, h_max + 1):
    n = 1 / num

print(f'H(n) = {1 + n}')

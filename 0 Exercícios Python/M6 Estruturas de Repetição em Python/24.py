"""
24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele próprio.

Ex: a soma dos divisores do número 66 é 1+2+3+6+11+22+33 = 78
"""
numero = int(input('Digite um número: '))
divs = 0

for num in range(1, numero):
    if numero % num == 0:
        divs += num

print(f'A soma dos divisores de {numero} é {divs}')

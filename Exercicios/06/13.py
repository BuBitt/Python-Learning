"""
13. Faça um programa que leia um número inteiro positivo par Ne imprima todos os números
    pares de 0 até N em ordem crescente.
"""
i_num = int(input('Digite um número inteiro positivo: '))

for num in range(0, i_num + 2, 2):
    print(num)

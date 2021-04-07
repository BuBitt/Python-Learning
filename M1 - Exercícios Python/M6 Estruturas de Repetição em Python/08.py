"""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""
import sys

maior = -2 ** 1031
menor = sys.maxsize

for loop in range(0, 10):
    val_inp = int(input('Digite um número: '))

    if val_inp > maior:
        maior = val_inp

    if val_inp < menor:
        menor = val_inp


print(f'''Maior número digitado: {maior}
Menor número digitado: {menor}\n''')

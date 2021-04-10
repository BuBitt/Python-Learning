"""
7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
   Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""
lista = []

for loop in range(1, 10 + 1):
    num = int(input('Digite um número: '))
    lista.append(num)

print(f'\n{lista}')
print(f'O maior número é {max(lista)}, e ele está na posição: {lista.index(max(lista))}')

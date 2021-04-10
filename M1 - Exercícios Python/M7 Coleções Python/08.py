"""
8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os
valores lidos na ordem inversa.
"""
lista = []
for loop in range(1, 6 + 1):
    val = int(input())
    lista.append(val)
print(lista[-1::-1])

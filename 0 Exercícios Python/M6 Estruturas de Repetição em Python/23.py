"""
23. Faca um algoritmo que leia um número positivo e imprima seus divisores.
"""
numero = int(input('Digite um número para saber seus divisores: '))

for num in range(1, numero):
    if numero % num == 0:
        print(num)

"""
55. Escreva um programa que leia um inteiro não negativo ne imprima a soma dos n primei-
    ros números primos.
"""
n = int(input('Digite o número para a soma: '))
n_soma = 0

for ciclo in range(1, n + 1):
    if ciclo == 2 or ciclo == 3 or ciclo == 5 or ciclo == 7:
        n_soma += ciclo

    elif not (ciclo % 2 == 0 or ciclo % 3 == 0 or ciclo % 5 == 0 or ciclo % 7 == 0):
        n_soma += ciclo
print(n_soma)

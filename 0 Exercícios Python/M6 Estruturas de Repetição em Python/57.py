"""
57. Faça um programa que conte quantos números primos existem entre a e b, onde a e b
    são números informados pelo usuário.

"""
n_i = int(input('Digite o valor inicial do intervalo: '))
n_f = int(input('Digite o valor final do intervalo: '))
n_soma = 0

for ciclo in range(n_i, n_f + 1):
    if ciclo == 2 or ciclo == 3 or ciclo == 5 or ciclo == 7:
        n_soma += 1

    elif not (ciclo % 2 == 0 or ciclo % 3 == 0 or ciclo % 5 == 0 or ciclo % 7 == 0) and ciclo != 1:
        n_soma += 1
print(n_soma)

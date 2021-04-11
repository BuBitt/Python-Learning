"""
53. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
    linhas do chamado Triangulo de Floyd. Para n = 6, temos:

1

2 3

4 5 6

7 8 9 10

11 12 13 14 15

16 17 18 19 20 21
"""
num = int(input('Digite um número: '))
check = 0
for loop in range(1, num + 1):

    for c in range(1, loop + 1):
        check += 1
        print(check, end=' ')

        if loop == c:
            print('\n')

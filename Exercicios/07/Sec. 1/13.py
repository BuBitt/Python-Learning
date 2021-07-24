"""
fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se
encontram o maior e o menor valor.
"""

num = []

for loop in range(0, 5):
    dn = int(input('Digite um número: '))
    num.append(dn)
    p_max = num.index(max(num))
    p_min = num.index(min(num))

print(f'O a posição do maior número, no vetor, é {p_max},e a do menor é {p_min}.')


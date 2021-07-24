"""
4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também
dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final
seu programa deverá escrever a soma dos valores encontrados nas respectivas 
posições X e Y.
"""
l = []
for loop in range(1, 8 + 1):
    v = int(input('Digite um número inteiro e real: '))
    l.append(v)

    if loop == 8:
        i_1 = int(input('\nDigite a posição desejada:'))
        i_2 = int(input('Digite a posição desejada:'))

s = l[i_1 - 1] + l[i_2 - 1]
print(f'\nA soma de {l[i_1 - 1]} e {l[i_2 - 1]} é igual a {s}')


"""9_Crie um programa que lê 6 valores inteiros pares e, em seguida,
mostre na tela os valores lidos na ordem inversa.
"""
par = []

while len(par) != 6:
    val = int(input())
    if val % 2 == 0:
        par.append(val)

for n in par:
    print(n, end=" ")
print('\n')


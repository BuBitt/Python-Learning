"""
2. Crie um programa que lê 6 valores inteiros e, em seguida, 
   mostre na tela os valores lidos.
"""
nb = []
for loop in range(1, 6 + 1):
    num = int(input('Digite um número: '))
    nb.append(num)

for nn in nb:
    print(nn)

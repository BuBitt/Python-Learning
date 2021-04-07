"""
5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
f_soma = 0

for num in range(0, 10):
    soma = int(input('Digite um número para soma: '))
    f_soma += soma

print(f_soma)

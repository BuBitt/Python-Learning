"""
25. Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
"""
soma = 0
for num in range(1000, 1, -1):
    if num % 3 == 0 or num % 5 == 0:
        soma += num

print(f'A soma de todos os multiplos de 3 e de 5 abaixo de 100 é {soma}.')

"""
6. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida
deverá ser impresso o maior e o menor elemento do vetor.
"""
vetor = []

for v in range(0, 10 + 1):
    n = int(input('Digite um número: '))
    vetor.append(n)

print(f'\nO maior número é: {max(vetor)}.')
print(f'O menor número é: {min(vetor)}.')

"""
Faça um programa que calcule o desvio padrão de um vetor c contendo n = 10 números,
onde m é a media do vetor.

Desvio Padrão = (((1 / (len(vetor) - 1)) ** 2) * ((vetor[i] - sum(vetor) / len(vetor) ** 2))
"""
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dv = 0

for i in range(10):
    dv = (1 / (len(vetor) - 1) * vetor[i] - (sum(vetor) / len(vetor)) ** 2) ** 2
print(dv)

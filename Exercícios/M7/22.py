"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor
contendo, nas posições pares os valores do primeiro e nas posções impares
o valor do segundo.
"""
from random import randrange


imp = []
par = []
fin = []


for i in range(10):
    imp.append(randrange(100))
    par.append(randrange(100))
print(f'{imp}\n{par}\n')

for p in range(10):
    fin.append(imp[p])
    fin.append(par[p])
print(fin)

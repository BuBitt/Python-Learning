"""
Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11,
ou seja, está ordenado em ordem crescente. Dado o vetor da questão anterior, proponha
um algorítimo para ordenar os elementos.
"""
from random import randrange


vetor = []


for i in range(11):
    vetor.append(randrange(1000))


vetor.sort()
print(vetor, '<- Vetor Gerado')


vet1 = vetor[0:6]
vet2 = vetor[6:11]


vet1 = vet1[::-1]
vet = vet2 + vet1
print(vet, '<- Vetor Resultante')

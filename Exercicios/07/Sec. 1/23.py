"""
Ler dois conjuntos de números reais armazenados em vetores e calcular o produto escalar
entre eles. Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos. Sendo que o
produto escalar é dado por: X1 * Y1 + X2 * Y2 + ... + Xn * Yn.
"""
from random import randrange


conj_1 = []
conj_2 = []
res = 0


for ls in range(5):
    conj_1.append(randrange(100))
    conj_2.append(randrange(100))
print(conj_1)
print(conj_2)

for p in range(5):
    res += (conj_1[p] * conj_2[p])
print(res)

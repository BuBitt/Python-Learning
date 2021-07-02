"""
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obitida.
"""
import numpy as np


mat = []


for i in range(5):
    add = []
    for j in range(5):
        if i == j:
            add.append(1)
        else:
            add.append(0)
    mat.append(add)
print()


for i in range(5):
    for j in range(5):
        print(mat[i][j], end=" ")
    print()

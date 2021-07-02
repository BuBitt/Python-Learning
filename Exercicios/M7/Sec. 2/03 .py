"""
Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha e
coluna de cada elemento. em seguida, imprima a matriz na tela.
"""
v = []


for i in range(4):
    local = []
    for j in range(4):
        local.append((i + 1) * (j + 1))
    v.append(local)

for i in range(4):
    for j in range(4):
        print(v[i][j], end=" ")
    print()
print()

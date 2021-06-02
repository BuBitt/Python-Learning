"""
Leia dois vetores x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:
    1 - Soma entre x e y. Soma de cada elemento de x com cada elemento da mesma posição em y
    2 - Produto entre x e y: multiplicação entre os elementos de x e y.
    3 - Diferença entre x e y.
    4 - Intersecção de x e y.
    5 - união de x e y.
"""
from random import randrange


vx = set()
vy = set()
td = []
total_som = []
total_prod = []


while len(vx) < 5 or len(vy) < 5:
    if len(vx) < 5:
        vx.add(randrange(100))
    elif len(vy) < 5:
        vy.add(randrange(100))


# Soma entre x e y.
for i in range(len(vx)):
    vx = list(vx)
    vy = list(vy)
    total_som.append(vx[i] + vy[i])
td.append(total_som)

# Produto.
for i in range(len(vx)):
    vx = list(vx)
    vy = list(vy)
    total_prod.append(vx[i] * vy[i])
td.append(total_prod)


# Diferença.
vx = set(vx)
vy = set(vy)
td.append(vx.difference(vy))


# Intersecção.
td.append(vx & vy)


# União.
td.append(vx | vy)


if td[3] == set():
    td[3] = 'Inexistente'


print(f"""
A soma entre x e y é {td[0]};
O produto entre os termos de x e y é {td[1]};
A Diferença entre vx e vy é {td[2]};
A intersecção entre vx e vy é {td[3]};
A União entre vx e vy é {td[4]}
""")

"""
Lei um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando
elementos repetidos.
"""

geral = []


# Inputs:

for inp in range(20):
    g_inp = int(input('Digite um número: '))
    geral.append(g_inp)


# Processamento

k = set(geral)
k = list(k)
k.sort()


# Output:

print('Os valores do vetor, removendo as repetições é:', end=' ')
for i, _ in enumerate(k[0:-1]):
    print(k[i], end=', ')

print(f'{k[-1]}.')

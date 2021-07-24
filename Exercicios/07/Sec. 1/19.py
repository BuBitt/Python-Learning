"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor (i + 5 * i) % (i + 1)
sedo i a posição do elemento no vetor. Em seguida imprima o vetor na tela.
"""

mem = []

for vet in range(50):
    mem.append((vet + (5 * vet)) % (vet + 1))
print(mem)

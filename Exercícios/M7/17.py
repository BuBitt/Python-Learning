"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que
possuírem valor negativo.
"""
mem = []
for n in range(10):
    v = int(input('Digite um número: '))
    mem.append(v)

for cont in range(len(mem)):
    if mem[cont] < 0:
        mem[cont] = 0

print(mem)

"""5. Leia um vetor de 10 posições. Contar e escrever quantos
valores pares ele possui.
"""
l_i = []
par = []


for cont in range(1, 10 + 1):
    inp = int(input('Digite um valor: '))
    l_i.append(inp)

for elemento in l_i:
    if elemento % 2 == 0:
        par.append(elemento)

print('\nOs Valores pares digitados são:', end=" ")

for par_i in par[0:-1]:
    print(f'{par_i}', end="")
    print(', ', end="")

print(f'{par[-1]}.')
print(f'Foram digitados {len(par)} valores pares.\n')

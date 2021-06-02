"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores
iguais e os escreva na tela.
"""

l_g = []  # + 'a' para forma com listas
repet = []


for inp in range(10):
    d_inp = int(input('Digite um número: '))

    if d_inp in l_g and d_inp not in repet:
        repet.append(d_inp)

    l_g.append(d_inp)


# Output:

print('Os valores repetidos foram ', end='')

for n, i in enumerate(repet):
    if not repet[n] == repet[n + 1:]:
        print(repet[n], end=', ')


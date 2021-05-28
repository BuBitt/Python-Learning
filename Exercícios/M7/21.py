"""
Faça um programa que receba do usuário 2 vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denominado C, calculando C = A - B. Mostre na tela os dados do vetor C.
"""
lista_a = []
lista_b = []
lista_c = []


for a in range(10):
    vet_a = int(input('Digite um número para o vetor A: '))
    lista_a.append(vet_a)

    if a == 9:
        print('\n')

for b in range(10):
    vet_b = int(input('Digite um número para o veto B: '))
    lista_b.append(vet_b)

    if b == 9:
        print('\n')


for i in range(10):
    c = lista_a.count(lista_b[i])

    if c < 1:
        lista_c.append(lista_b[i])

for i in range(10):
    c = lista_b.count(lista_a[i])

    if c < 1:
        lista_c.append(lista_a[i])
print(lista_c)

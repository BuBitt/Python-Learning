"""
1. Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
   O programa deve executar os seguintes passos:

    (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5,7.

    (b) Armazene em uma variável inteira (simples) a soma entre os valores das posições
       A[O], A[1] e A[5] do vetor e mostre na tela esta soma.

    (c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.

    (d) Mostre na tela cada valor do vetor A, um em cada linha.
"""
# (a)
vetor = [1, 0, 5, -2, -5, 7]
print(vetor)

# (b)
v = vetor[0] + vetor[1] + vetor[5]
print(v)

# (c)
vetor.insert(4, 100)
print(vetor)

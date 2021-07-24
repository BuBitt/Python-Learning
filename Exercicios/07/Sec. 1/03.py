"""
3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos
têm 10 elementos cada. Imprimir todos os conjuntos.
"""
l1 = []
l2 = []


for vetor in range(1, 10 + 1):
    inp_n = int(input('Digite um número inteiro real: '))
    l1.append(inp_n)

    while True:
        l2.append(inp_n ** 2)
        break

print('\n', l1)
print(l2)

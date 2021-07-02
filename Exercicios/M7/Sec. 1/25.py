"""
Faça um programa que preencha um vetor com os 100 primeiros números naturais
não multiplos de 7 ou que terminam com 7.
"""

lista = []


for n in range(100):
    v = str(n)
    v_t = v[-1]

    if n % 7 != 0 and v_t != '7':
        lista.append(n)
print(lista)

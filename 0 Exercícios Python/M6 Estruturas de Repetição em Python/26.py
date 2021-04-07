"""
26. Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""
import sys


num = int(input('Digite um número: '))
v_max = sys.maxsize

lista_11 = []
lista_13 = []
lista_17 = []

index_11 = len(lista_11)
index_13 = len(lista_13)
index_17 = len(lista_17)

for k in range(num, v_max):
    if k % 11 == 0:
        print(k, 'multiplo de 11')
        lista_11.append(k)
        index_11 = len(lista_11)

    elif k % 13 == 0:
        print(k, 'multiplo de 13')
        lista_13.append(k)
        index_13 = len(lista_13)

    elif k % 17 <= 0:
        print(k, 'multiplo de 17')
        lista_17.append(k)
        index_17 = len(lista_17)

    elif index_11 >= 3 and index_13 >= 3 and index_17 >= 3:
        break


print(f'''
Os multiplos de 11 são acima de {num}: {lista_11[0], lista_11[1], lista_11[2]}.
Os multiplos de 13 são acima de {num}: {lista_13[0], lista_13[1], lista_13[2]}. 
Os multiplos de 17 são acima de {num}: {lista_17[0], lista_17[1], lista_17[2]}.
''')

"""
Escreva uma função para determinar a quantidade de números primos abaixo de N:
"""


def numeros_primos_abaixo(numero=2):
    primos = []

    for verificado in range(2, numero):
        for verificando in range(2, verificado):

            if verificado % verificando == 0:
                break
        else:
            primos.append(verificado)

    return len(primos)


print(numeros_primos_abaixo(10))

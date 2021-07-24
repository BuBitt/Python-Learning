"""
faça uma função que receba dois números inteiros positivos por parâmetro e
retorne a soma dos N números inteiros existentes entre eles.
"""


def soma_num_inteiros(num_1, num_2):

    total = 0
    for termo_soma in range(num_1 + 1, num_2):
        total += termo_soma
    return total


print(soma_num_inteiros(1, 500))

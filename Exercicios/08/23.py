"""
Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n de largura.
Por exemplo, a saída para n = 4 seria:

*
**
***
****
***
**
*

"""


def triangulo_lateral(tamanho):
    for metade_1 in range(tamanho + 1):
        print('*' * metade_1)
    if not metade_1 == tamanho:
        print()
    for metade_2 in range(tamanho -1, 0, -1):
        print('*' * metade_2)
    print()


triangulo_lateral(5)


"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = sqrt(a² + b²). Faça uma função que receba os valores de a e b e calcule o
valor da hipotenusa através da equação.
"""


def sqrt(x):
    return x ** (1 / 2)


def hipotenusa(cateto_a, cateto_b):
    return sqrt(cateto_a ** 2 + cateto_b ** 2)


print(hipotenusa(3, 4))

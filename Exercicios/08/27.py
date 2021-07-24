"""
Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule
o valor do seno desse angulo usando sua respectiva série de taylor:


"""
def factorial(x):
    res = 1

    for i in range(2, x + 1):
        res *= i

    return res


def graus_to_radianos(graus):
    pi = 3.141593
    rad = graus * pi / 180
    return rad


def sin(x):
    for i in range(6):
        v = (- 1 ** i / factorial(2 * i + 1)) * (x ** (2 * i + 1))
    return v


print(sin(graus_to_radianos(180)))

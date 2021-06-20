"""
Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
sendo que o raio é passado por parãmetro.
"""
raio = float(input("Digite o valor do raio: "))


def volume_esfera(r):
    return 4 / 3 * 3.14 * r ** 3


print(volume_esfera(raio))

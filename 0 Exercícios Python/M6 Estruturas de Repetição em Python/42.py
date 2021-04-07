"""
42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
    escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
    a entrada de dados com um valor negativo ou zero.
"""
quad = 1
while int(quad) > 0:
    quad = int(input('Digite um valor: '))
    ao_q = quad ** 2
    ao_c = quad ** 3
    r_q = float(quad ** (1 / 2))
    print(ao_q, ao_c, r_q)

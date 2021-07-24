"""
Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas
com pontos de exclamação, confrome o exemplo abaixo.
"""


def criar_piramide(numero):
    for padrao in range(numero + 1):
        print('!' * padrao)
    print()



criar_piramide(70)

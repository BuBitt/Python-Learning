"""
Faça um algorítimo que receba um número inteiro positivo n e calcule o seu fatorial, n!.
"""


def fatorial(numero):
    fatorial_resultado = 1

    for c_fatorial in range(2, numero + 1):
        fatorial_resultado *= c_fatorial

    return fatorial_resultado


print(fatorial(9999999))

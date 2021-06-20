"""
Faça uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o
resultado de X^Z para o programa principal. Atenção não utilize nenhuma função
pronta de exponenciação.
"""


def exponenciacao(base, expoente):
    total = 1
    for i in range(expoente):
        total *= base
    return total


print(exponenciacao(10, 30))
print(10**30)

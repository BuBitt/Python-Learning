"""
Faça uma função para verificar se um npumero é positivo ou negativo. Sendo que o valor
de retorno será 1 se positivo, -1 se negativo e 0 se 0.
"""


def check_grandeza(numero):
    """Verifica se o número é neutro, negativo ou positivo.

    Args:
        numero (int): Número a ser verificado.

    Returns:
        int: retornos: 1, 0, -1.
    """
    if numero == 0:
        return 0
    elif numero < 1:
        return -1
    return 1


print(check_grandeza(10))
print(check_grandeza(-10))
print(check_grandeza(0))

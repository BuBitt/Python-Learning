"""
Faça uma função que verifica se um número é um quadrado perfeito. Um quadrado
perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de
outro número inteiro. Ex: 1, 4, 9;
"""


def vef_quadrado_perfeito(numero):
    if numero > 0:
        raiz_quadrada = numero ** 0.5

        if raiz_quadrada.is_integer():
            return f'O número {numero} é um quadrado perfeito.'

        return f'O número {numero} não é um quadrado perfeito.'
    return f'O número {numero} não é um quadrado perfeito.'


print(vef_quadrado_perfeito(8))

"""
Escreva uma função que receba um número inteiro maior do que zero e retorne a soma
de todos os seus algarismos. Por exemplos, ao número 251 corresponderá o valor 8
(2 + 5 + 1). Se o número lido não for maior que zero, o programa terminará com a
mensagem número inválido.
"""


def soma_algarismo(numero):
    numero = str(numero)
    numero = list(numero)
    soma = 0
    
    for indice in range(len(numero)):
        soma += int(numero[indice])
    
    if soma > 0:
        return soma
    return 'Número Inválido'


print(soma_algarismo(251))

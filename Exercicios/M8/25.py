"""
Faça uma função que receba um número inteiro N como parâmetro, calcule e retorne
o resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + + ... + (n² + 1)/(n + 3)
"""
def seq(n):
    sequencia = 0

    for s in range(n):
        sequencia += (n ** 2 + 1) / (n + 3)

    return f'{sequencia}'


print(seq(10000))

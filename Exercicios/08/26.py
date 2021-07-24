"""
Fala uma função que receba um número inteiro positivo n e calcule o somatório de 1 até n.
"""
import time
import datetime


begin_time = datetime.datetime.now()


def somatorio(n):
    print(datetime.datetime.now() - begin_time, '<- Matemática')
    return (n * (1 + n)) / 2


def somatorio_for(n):
    res = 0
    for n in range(1,n + 1):
        res += n
    print(datetime.datetime.now() - begin_time, '<- Loop for')
    return res


n = 999999999
print(somatorio(n))
print(somatorio_for(n),)

"""
52. Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
    de um banco e retorne quantas notas de cada valor serão necessárias para atender ao
    saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50,
    20, 10, 5, 2 e 1 real.
"""
v_s = int(input('Quanto deseja sacar? '))

for n in range(v_s, 0, -1):
    if n == 100 or n == 50 or n == 20 or n == 10 or n == 5 or n == 2 or n == 1:
        nn = v_s // n
        v_s -= nn * n
        print(f'{nn} nota(s) de {n}.')

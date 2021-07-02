"""
56. Faça um programa que calcule a soma de todos os números primos abaixo de dois
    milhoes.

for n in range(2, 2_000_000 + 1):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # loop fell through without finding a factor
        print(n, soma_p)
        soma_p += n
print(soma_p)
"""
soma_p = 0

for primo in range(1, 2_000_000 + 1):
    if primo < 10:
        soma_p = 17

    if primo > 10:
        if not (primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0):
            soma_p += primo
print(soma_p)

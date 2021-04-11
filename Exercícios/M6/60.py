"""
60. Faça um programa que leia vários números, calcule e mostre:

    (a) A soma dos números digitados
    (b) A quantidade de números digitados
    (c) A média dos números digitados
    (d) O maior número digitado
    (e) O menor número digitado
    (f) A média dos números pares

Finalize a entrada de dados caso o usuário informe o valor 0.
"""
import sys


a = 0
b = 0
c = 0
d = 0
e = sys.maxsize
f = 0
j = 0


f_c = 0
check = 0


while True:
    num = int(input('Número para sequência: '))

    if num == 0:
        print('Você saiu do programa.')
        break

    check += 1
    a += num
    b -= num
    c = a / check

    if num > d:
        d = num

    if num < e:
        e = num

    if num % 2 == 0:
        f += num
        f_c += 1
        j = f / f_c

print(f"""
A soma dos números digitados é {a}.
A quantidade de números digitados é {check}.
A média dos números digitados é {c}.
O maior número digitado é {d}.
O menor número digitado é {e}.
A média dos números pares é {j}.
""")

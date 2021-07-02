"""
61. Faça um programa que calcule o maior número palíndromo feito a partir do produto de
    dois números de 3 dígitos. Ex: O maior palíndromo feito a partir do produto de dois
    números de dois digitos é 9009 = 91 * 99.
"""
import time


total = ''
mt = 0
mtc = 0

# time start

for num in range(111, 999 + 1):
    for x_num in range(111, 999 + 1):
        calc = num * x_num
        str_num = str(calc)
        v_str_num = str_num[::-1]
        print(calc)

        if str_num == v_str_num:
            total = str_num
            mt = num
            mtc = x_num


print(f'{total} = {mt} * {mtc}')

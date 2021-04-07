"""
40. Elabore um programa que faça leitura de vários números inteiros, até que se digite um
    número negativo. O programa tem que retornar o maior eo menor número lido.
"""
check = 0
num = 0

while num > -1:
    num = int(input('Digite um número: '))
    if num >= check:
        check = num
print(f'O maior número foi {check}')

"""
Faça um programa que receba dois números e mostre o maior. Se por acaso,
os dois números forem iguais, imprima a menságem "Números iguais".
"""
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print(num1)
elif num1 == num2:
    print('Os números são iguais.')
else:
    print(num2)

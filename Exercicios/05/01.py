"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""
# Input: Números de comparação:
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

# Processamento: comparação dos valores:
if num1 > num2:
    print(f'O Primeiro número ({num1}) é maior que o segundo ({num2}).')
elif num1 == num2:
    print(f'Os números são iguais.')
else:
    print(f'O Segundo número ({num2}), é maior que o primeiro ({num1})')

"""
Faça um programa que receba a altura e o sexo de uma pessoa, calcule
e mostre seu peso ideal, ultilizando as seguintes formulas:
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 44,7
"""
sexo = str(input('Qual o seu sexo? ')).capitalize()
h = float(input('Qual a sua altura? '))

if sexo == 'Homem':
    print(f'Seu peso ideal é: {(72.7 * h) - 58}')
    print(sexo)
else:
    print(f'Seu peso ideal é: {(61.1 * h) - 44.7}')
    print(sexo)

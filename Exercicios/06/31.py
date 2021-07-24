"""
31. Faça um programa que calcule e escreva o valor de S:

s = (1 / 1) + (3 / 2) + (5 / 3) + (7 / 4) ... (99 / 50)
"""
denominador = 0
serie = 0
for numerador in range(1, 99 + 1, 2):
    denominador += 1
    calc = (numerador / denominador)
    serie += calc
print(serie)

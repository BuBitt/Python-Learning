"""
Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
"""
soma = 0
print(1)
for number in range(0, 100):
    if number > 0 and number % 3 == 0:
        print(number)
        soma += 1

    elif soma == 4:
        break

"""
51. Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996
    recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao
    dobro do ano anterior. Faça programa que determine o salário atual do funcionário.
"""
a = 1996
s = 2000

s_b = s * 1.015
s_b = round(s_b)

while a < 2021:
    a += 1

    a_d = a - 1996
    s_b *= (1 + (0.015 * 2))
print(round(s_b))

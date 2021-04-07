"""
29. Escreva um programa para calcular o valor da série, para 5 termos.

S = 0 + 1/2! +2/4! +3/6! + ...
"""
serie = 0

for n in range(1, 10 + 1):
    i = 1
    if n % 2 == 0:
        for u in range(1, n + 1):
            i *= u
        calc = (1 / i)
        serie += calc
print(serie)

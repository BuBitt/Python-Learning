"""
28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
    conforme a fórmula a seguir

E = 1 + 1/1! + 1/2! + 1/3! +... + 1/N!
"""

fac = int(input('Digite um número: '))
serie = 1

for n_loop in range(1, fac + 1):
    f = 1
    for n_fator in range(1, n_loop + 1):
        f *= n_fator
    soma = (1 / f)
    serie += soma
print(serie)

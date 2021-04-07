"""
37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) pos-
    suem a propriedade seguinte: a soma dos dois digitos de mais baixa ordem com os dois
    digitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. Por exemplo,
    para o inteiro 3025, temos que:
    30 + 25 = 55
    55² = 3025
"""


for c in range(1000, 10000):
    str_c = str(c)
    b_ordem = int(str_c[0:2])
    a_ordem = int(str_c[2:5])
    if (b_ordem + a_ordem) ** 2 == c:
        print(c)

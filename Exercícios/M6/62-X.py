"""
62. Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro,
cinco, então há 2 + 4 + 4 + 6 + 5 22 letras usadas no total. Faça um programa
que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil)
fossem escritos em palavras.
OBS: Não conte espaços ou hifens.
"""
v = 6  # * 2
t = 7
q = 9  # * 2
c = 10
o = 8  # * 3
total = - 9 * 9


numerais = [2, 4, 4, 6, 5, 4, 4, 4, 4]
teens = [3, 4, 4, 5, 8, 6, 9, 9, 7, 8]


for num in range(1, 6 + 1):

    if num == 1:
        for _, numerais_g in enumerate(numerais):
            total += numerais_g

    if num == 2:
        cent = (100 * 6) - 1  # 'centoe'
        total += cent

        for rep in range(1, 10 + 1):
            for _, dezenas in enumerate(teens):
                total += dezenas

    if num == 3:
        duz = (100 * 9) - 1  # 'duzentose'
        total += duz

        for rep in range(1, 2 + 1):
            for vint_2 in range(1, 9 + 1):
                total += v

                for _, nume in enumerate(numerais):
                    total += (v + nume)

    if num == 4:
        trez = (100 * 10) - 1  # 'trezentose'
        total += trez

        for trin_2 in range(1, 9 + 1):
            total += trin_2

            for _, nume in enumerate(numerais):
                total += (t + nume)

    if num == 5:
        quat = (100 * 12) - 1  # 'quatrocentose'
        total += quat

        for rep in range(1, 2 + 1):
            for quat_2 in range(1, 9 + 1):
                total += q

                for _, nume in enumerate(numerais):
                    total += (q + nume)

    if num == 6:
        for rep in range(1, 4 + 1):
            cinc = (100 * 11) - 1  # 'quinhentose'
            total += cinc

            for cinc_2 in range(1, 9 + 1):
                total += c

                for _, nume in enumerate(numerais):
                    total += c + nume
print(total)

"""
36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros
    100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez
    primeiros números naturais é,

                                    1² + 2² + ... +10² = 385

    O quadrado da soma dos dez primeiros números naturais é,

                                (1 + 2 + ... + 10)² = 552 = 3025

    A diferença entre a soma dos quadrados dos dez primeiros números naturais e o
    quadrado da soma é 3025-385 2640.
"""
val_quad_ind = 0
val_quad_som = 0
val_quad_calc = 0


for quadrado_ind in range(1, 10 + 1):
    val_quad_ind += quadrado_ind ** 2


for quadrado_con in range(1, 10 + 1):
    val_quad_som += quadrado_con
    val_quad_calc = val_quad_som ** 2


print(val_quad_calc - val_quad_ind)

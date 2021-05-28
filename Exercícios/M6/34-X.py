"""
34. Faça um programa que calcule o menor número divisível por cada um dos números de 1
    a 20? Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1
    a 10, sem sobrar resto.
"""


n = 1

while True:
    check = 0                                       # Como o resto tem que ser 0, basta fazer uma soma das checagens.
    for i in range(1, 21):                          # loop para construir o valor a ser checado.
        check += n % i
        print(check)# Soma das checagens.
    if check == 0:                                  # Condicional do sistema.
        print(f'O menor divisível é: {n}.')
        break
    n += 1

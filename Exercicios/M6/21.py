"""
21. Faça um programa que receba dois números. Calcule e mostre:
    - a soma dos números pares desse intervalo de números, incluindo os números digitados;
    - a multiplicação dos números impares desse intervalo, incluindo os digitados;
"""
quantidade_i = int(input('Digite o valor inicial do intervalo numérico: '))
quantidade_f = int(input('Digite o valor final do intervalo numérico: '))


soma = 0
dif = 1


for num in range(quantidade_i, quantidade_f + 1):
    if num % 2 == 0:
        soma += num

    if num % 2 == 1:
        dif *= num


print(f'A soma dos números pares é {soma}, e a multiplicação dos números impares é {dif}.')

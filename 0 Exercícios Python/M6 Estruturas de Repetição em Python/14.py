"""
14. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
    decrescente.
"""
# Versão for:
i_num = int(input('Digite um número inteiro impar: '))

for num in range(i_num, - 1, -2):
    print(num)
    if num == 1:
        print(num - 1)

# Em variação de números ímpares em range, deve-se por -2 além do de parada.

# Versão while:
w_i_num = int(input('Digite um número inteiro impar: '))
num = 2

while w_i_num > -1:
    print(w_i_num)
    w_i_num -= 2
    if w_i_num == -1:
        print(w_i_num + 1)

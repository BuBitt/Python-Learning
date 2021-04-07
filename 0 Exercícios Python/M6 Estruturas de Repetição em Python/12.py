"""
12. Faça um programa que leia um número inteiro positivo N e imprima todos os números
    naturais de 0 até N em ordem decrescente.
"""
# for
f_num = int(input('for: Digite um número inteiro positivo: '))
for num in range(f_num + 1, 0, -1):
    print(num - 1)


# while
w_num = int(input('while: Digite um número inteiro positivo: '))
while w_num >= 0:
    print(w_num)
    w_num -= 1

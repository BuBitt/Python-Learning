"""
Escreva um programa que leia um número inteiro maior do que zero e devolva,
na tela, a soma de todos os seus algarismos. Pro exemplo, ao número 251
corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior que zero,
o programa terminará com a mensagem: "Número inválido".
"""
num = str(input('Digite um número qualquer maior que 0: '))

if int(num) > 0:
    res = list(map(int, num))
    som = sum(res)
    print(f'A soma dos algarismo do número é {som}')
else:
    print('Número inválido')

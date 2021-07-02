"""
33. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem
    crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Exemplo
    Para n = 6, i = 2 e j = 3 a saida deverá ser: 0,2,3,4,6,8.
"""
n = int(input('Intervalo dos múltiplos: '))
i = int(input('Digite o valor i: '))
j = int(input('Digite o valor j: '))


for k in range(0, n + 1):
    if k % i == 0:
        print(k, end=', ')

    elif k % j == 0:
        print(k, end=', ')

    elif j % i == 0 and j % j == 0:
        print(k, end=', ')

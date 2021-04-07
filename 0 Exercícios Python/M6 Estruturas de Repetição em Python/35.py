"""
35. Faça um programa que some os números impares contidos em um intervalo definido
    pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo
    e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o
    usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve
    ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa
    termina. Exemplo de tela de saída:

    Digite o valor inicial: 5
    E valor final: 10
    Soma dos impares neste intervalo : 21
"""
val_ini = int(input('Digite o começo do intervalo: '))
val_fin = int(input('Digite o final do intervalo: '))

if val_fin > val_ini:
    impar = 0
    for soma in range(val_ini, val_fin + 1, 2):
        if soma % 2 == 1:
            print(soma)
            impar += soma
    print(impar)
else:
    print('Intervalo de valores inválido')

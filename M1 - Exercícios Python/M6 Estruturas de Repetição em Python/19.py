"""
19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
    cada um dos algarismos que compõem o número.
"""
numero_inteiro = int(input('Digite um número inteiro entre 100 e 999: '))

if 100 <= numero_inteiro <= 999:
    n_i = str(numero_inteiro)
    for num in n_i:
        print(num)

else:
    print(f'O número {numero_inteiro} não respeita os critérios do programa.')

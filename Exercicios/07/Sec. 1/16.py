"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois,
um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre
o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o
código for diferente de 1 e 2 escreva uma mensagem informando que o código é
inválido.
"""

inp = 0
vet = []

for loop in range(5):
    val = float(input('Digite um número real: '))
    vet.append(val)


while True:
    inp = int(input('''
Digite o código da ação desejada:

0 - Finalizar programa.
1 - Mostrar o vetor na ordem direta.
2 - Mostrar o vetor na ordem inversa.

>'''))

    if inp == 1:
        print('\n', vet, '\n' * 2)
        print('----------------------------------------')

    elif inp == 2:
        print('\n', vet[::-1], '\n' * 2)
        print('----------------------------------------')

    elif inp == 0:
        break

    else:
        print('\nO código digitado é inválido.\n\n')
        print('----------------------------------------')


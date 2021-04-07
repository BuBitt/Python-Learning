"""
47. Faça um programa que apresente um menu de opções para o cálculo das seguintes
    operações entre dois números:

        - adição (opção 1)
        - subtração (opção 2)
        - multiplicação (opção3)
        - divisão (opção 4).
        - saída (opção 5)

    O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do
    resultado ea volta ao menu de opções. O programa só termina quando for escolhida a
    opção de saída (opção 5).
"""
print("""
1 - adição
2 - subtração
3 - multiplicação
4 - divisão
5 - saída
""")

while True:
    menu = int(input('> '))

    if menu == 1:
        som_1 = float(input('Digite o primeiro número: '))
        som_2 = float(input('Digite o segundo número: '))
        total = som_1 + som_2
        print(f'{total}')

    elif menu == 2:
        sub_1 = float(input('Digite o primeiro número: '))
        sub_2 = float(input('Digite o segundo número: '))
        total = sub_1 - sub_2
        print(f'{total}')

    elif menu == 3:
        mult_1 = float(input('Digite o primeiro número: '))
        mult_2 = float(input('Digite o segundo número: '))
        total = mult_1 * mult_2
        print(f'{total}')

    elif menu == 4:
        div_1 = float(input('Digite o primeiro número: '))
        div_2 = float(input('Digite o segundo número: '))
        total = div_1 / div_2
        print(f'{total}')

    elif menu == 5:
        print('Você saiu do programa.')
        break

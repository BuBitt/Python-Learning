"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. escreva uma menságem de erro a opção for iválida.

Escolha a opção:

1 - Soma de 2 números.
2 - Diferença de 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser 0).
"""
opc = int(input('''
Escolha a opção:

1 - Soma de 2 números.
2 - Diferença de 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser 0).
> '''))

if opc == 1:
    print('\n> Você optou por fazer um soma: \n')
    num1 = float(input('> Digite o primeiro número: '))
    num2 = float(input('> Digite o segundo número: '))

    print(f'\n> A soma dos dois números é {num1 + num2}.')

elif opc == 2:
    print('\n> Você optou por fazer um subtração: \n')
    num1 = float(input('> Digite o primeiro número: '))
    num2 = float(input('> Digite o segundo número: '))

    if num1 > num2:
        print(f'\n> A diferença entre os dois números é {num1 - num2}.')
    else:
        print(f'\n> A diferença entre os dois números é {num2 - num1}.')

elif opc == 3:
    print('\n> Você optou por fazer um multiplicação: \n')
    num1 = float(input('> Digite o primeiro número: '))
    num2 = float(input('> Digite o segundo número: '))

    print(f'\n> O produto dos dois números é {num1 * num2}.')

elif opc == 4:
    print('\n> Você optou por fazer um multiplicação: \n')
    nume = float(input('> Digite o numerador número: '))
    deno = float(input('> Digite o denominador número: '))

    if deno != 0:
        print(f'\n> A divisão entre {nume} e {deno} é {nume / deno}.')
    else:
        print(f'\n> A divisão entre {nume} e {deno} é indefinida.')

else:
    print('> A opção escolhida é inválida.')

"""
39. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas
    pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou seja,
    medidas menores ou iguais a 0.

"""

while True:
    print('\nDigite -1 para sair')
    base = int(input('Digite o valor da base: '))
    if base != - 1:
        altura = int(input('Digite o valor da altura: '))
        if base and altura > 0:
            area = base * altura / 2
            print(f'A área do triângulo é {area}')
        else:
            print('Valor inválido \n')
    else:
        break

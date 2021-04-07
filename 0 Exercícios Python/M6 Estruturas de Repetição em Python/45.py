"""
45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice
    versa. Você deve criar um menu com as duas opções de conversão e com uma opção
    para finalizar o programa. O usuário poderá fazer quantas conversões desejar, sendo
    que o programa só será finalizado quando a opção de finalizar for escolhida.
"""
while True:
    print("""
1 - km/ para m/s
2 - m/s para km/h
3 - sair
    """)
    menu = int(input('> '))

    if menu == 1:
        kmh = float(input('Digite a velocidade em km/h: '))
        conv = kmh / 3.6
        print(f'{kmh} km/h é equivalente a {conv} ms/s.')

    elif menu == 2:
        ms = float(input('Digite a velocidade em ms/s: '))
        conv = ms * 3.6
        print(f'{ms} m/s é equivalente a {conv} km/h.')

    elif menu == 3:
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida.')

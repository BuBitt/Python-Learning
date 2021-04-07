"""
22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
    uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela,
    como resultado, a correspondente média aritmética. O número de notas com que o aluno
    pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
    introduzido um valor que não seja válido como nota de aprovação.
"""
loop = 0
media = 0
t_media = 0


while True:
    loop += 1
    val_1 = int(input('Digite a nota para média: '))

    if 10 <= val_1 < 21:
        media += val_1
        t_media = media / loop
        print(f'A média atual total é {t_media}\n')

    else:
        print(f'\nA média total é {t_media}')
        break


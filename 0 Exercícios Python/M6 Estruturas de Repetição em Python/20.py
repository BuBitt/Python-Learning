"""
20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá
    ser informado o numero de dados lidos e número de valores pares. O processo termina
    quando for digitado o número 1000.
"""
par = 0
verificador = 0

while True:
    val_lido = int(input('Digite um valor a ser lido: '))

    if val_lido != 1000:
        verificador += 1
        if val_lido % 2 == 0:
            par += 1

    else:
        break

print(f'Foram lidos {verificador} valores, em que, {par} deles são par.')

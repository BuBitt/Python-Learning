"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a taela abaixo:

|------------------------------------|
|CONSUMO    |(Km/l) | MENSAGEM       |
|menor que  |8      |Venda o carro!  |
|entre      |8 e 14 |Econômico       |
|maior que  |12     |Super Econômico |
|------------------------------------|
"""
km = float(input('Digite a distância em km: '))
litro = float(input('Digite a quantidade de litros consumidos: '))
consumo = km / litro

if consumo > 12:
    print('Super Econômico.')

elif 8 <= consumo <= 14:
    print('Econômico.')

else:
    print('Venda o Carro!')

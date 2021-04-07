"""
Faça um programa que receba altura e o peso de uma pessoa. de acordo com
a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.
"""
peso = float(input('Qual o seu peso (em kg)? '))
altura = float(input('Qual a sua altura (em cm)? '))


# Para altura menores que 120cm:
if altura < 120:
    if peso <= 60:
        print('A')
    elif 60 < peso <= 90:
        print('D')
    else:
        print('G')

# Para altura maiores que 120cm e menores que 170cm:
elif 120 <= altura <= 170:
    if peso <= 60:
        print('B')
    elif 60 < peso <= 90:
        print('E')
    else:
        print('H')

# Para alturas acima de 170cm:
elif altura > 170:
    if peso <= 60:
        print('C')
    elif 60 < peso <= 90:
        print('F')
    else:
        print('I')
else:
    print('Valor Inválido.')

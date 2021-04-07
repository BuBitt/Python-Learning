"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço
antigo calcule e escreva o preço novo, e escreva uma mensagem em função
do preço novo (de acordo com a segunda tabela).
"""
prec_i = float(input('Qual era o preço antigo: '))
prec_n = 0

# Bloco do preço antigo.
if prec_i <= 50:
    prec_5 = prec_i * 1.05
    prec_n = prec_5

elif 50 < prec_i <= 100:
    prec_10 = prec_i * 1.10
    prec_n = prec_10

else:
    prec_15 = prec_i * 1.15
    prec_n = prec_15


# Bloco do preço novo.
if prec_5 <= 80 or prec_10 <= 80 or prec_15 <= 80:
    print(f'O preço novo é R$ {prec_n}.')
    print('Barato.')

elif (80 < prec_5 <= 120 or prec_10 <= 80 and prec_10 <= 120
      or prec_15 <= 80 and prec_15 <= 120):

    print(f'O preço novo é R$ {prec_n}.')
    print('Normal.')

elif (120 < prec_5 <= 200 or prec_10 <= 120 and prec_10 <= 200
      or prec_15 <= 120 and prec_15 <= 200):

    print(f'O preço novo é R$ {prec_n}.')
    print('Caro.')

elif prec_5 > 200 or prec_10 <= 200 or prec_15 <= 200:
    print(f'O preço novo é R$ {prec_n}.')
    print('Muito Caro')

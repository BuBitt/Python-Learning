# Tabela de preços:
print('''
|-Especifiação----|-Código-|-Preço--|
|-----------------|--------|--------|
|Cachorro Quente  |   100  |  1.20  |
|Bauru Simples    |   101  |  1.30  |
|Bauru com Ovo    |   102  |  1.50  |
|Hamburger        |   103  |  1.20  |
|Cheeseburger     |   104  |  1.70  |
|Suco             |   105  |  2.20  |
|Refrigerante     |   106  |  1.00  |
|-----------------------------------|
''')

# Inputs:
prod_cod = int(input('> Código do produto: '))
quantidade = int(input('> Quantidade: '))

# Processamento e outputs:
if prod_cod == 100:
    if quantidade == 1:
        print(f'{quantidade} Cachorro-Quente é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Cachorros-Quentes são R$ {quantidade * 1.2}.')

elif prod_cod == 101:
    if quantidade == 1:
        print(f'{quantidade} Bauru Simples é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Baurus Simples são R$ {quantidade * 1.2}.')

elif prod_cod == 102:
    if quantidade == 1:
        print(f'{quantidade} Bauru com Ovo é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Baurus com Ovos são R$ {quantidade * 1.2}.')

elif prod_cod == 103:
    if quantidade == 1:
        print(f'{quantidade} Hamburger é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Hamburgers são R$ {quantidade * 1.2}.')

elif prod_cod == 104:
    if quantidade == 1:
        print(f'{quantidade} Cheeseburger é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Cheeseburger são R$ {quantidade * 1.2}.')

elif prod_cod == 105:
    if quantidade == 1:
        print(f'{quantidade} Suco é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Sucos são R$ {quantidade * 1.2}.')

elif prod_cod == 106:
    if quantidade == 1:
        print(f'{quantidade} Refrigerante é R$ {quantidade * 1.2}.')
    else:
        print(f'{quantidade} Refrigerantes são R$ {quantidade * 1.2}.')

else:
    print('Não é um código de produto válido.')

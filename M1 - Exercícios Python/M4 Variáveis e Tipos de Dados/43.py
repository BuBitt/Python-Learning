"""
Escreva um Programa de ajuda para vendedores. A partir de um valor total lido,
mostre:
    - O total a pagar com desconto de 10%;
    - O valor de cada parcela, no parcelamento de 3x sem juros;
    - A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor
      com desconto)
"""
# Input: Valor do produto vendido.
valvend = float(input('Digite o valor do produto vendido: '))

# Processamento:
#    10% do valor / 3 parcelas sem juros / comissão do vendedor.
desc10 = valvend * 0.9
parc3 = valvend / 3
comvend = desc10 * 0.05

# Output: Desconto / Parcelamento / Comissão.
print(f'''
Valor com desconto aplicado: R${desc10};
Valor individual da parcela (3x): R$ {parc3};
Comissão do vendedor: R$ {comvend}.
''')

"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada
estado possui uma taxa diferente de imposto sobre o produto (MG 7%, SP 12%,
MS 8%). Faça um rograma em que o susário entre com o valor e o estado de
destino do produto e o programa retorne o preço final do produto acrescido
do imposto do estado em que ele será vendido. Se o estado digitado não for
valido, mostrar uma mensagem de erro.
"""
valor = float(input('Digite o valor do produto R$ '))
estado = str(input('Digite a sigla do estado: '))

if estado.upper() == 'MG':
    imp = valor * 1.07
    print(f'O valor final do produto é R$ {imp}')

elif estado.upper() == 'SP':
    imp = valor * 1.12
    print(f'O valor final do produto é R$ {imp}')

elif estado.upper() == 'MS':
    imp = valor * 1.08
    print(f'O valor final do produto é R$ {imp}')

else:
    print('A sigla do estado digitado é inválida')

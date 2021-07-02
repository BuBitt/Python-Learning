"""
A importância de R$ 780 000,00 será divida entre três ganhadotes de um concurso
sendo que da quantia total:
    º O primeiro Ganhador recebrá 46%;
    º O segundo receberaá  32%;
    º O terceiro recebrá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
# Input: Digitar o valor da soma de todos os prêmios.
valt = float(input('Digite o valor da soma de todos os prêmios: '))

# Processamento:
# top = cololação no concurso.
top1 = valt * 0.46
top2 = valt * 0.32
top3 = valt - (top1 + top2)

# Output: Impressão dos resultados referentes a colocação.
print(f'''
    O primeiro Lugar receberá R$ {top1};
    o segundo R$ {top2};
    e o terceiro R$ {top3}.
    ''')

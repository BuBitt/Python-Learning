"""
Faça uma função que receba a distância em Km e a quantidade de elitros de gazolina
consumidos por um carro em um percuso, calcule o consumo em Km/l e escrva uma
mensagem de acordo com a tabela abaixo:


CONSUMO    Km/l    MENSAGEM
<           8      Venda o carro!
<>        8 e 14   Econômico!
>           12     Super econômico!
"""


def distncia_por_litro(distancia, litros):
    distancia_litro = distancia / litros
    
    if distancia_litro < 8:
        return 'Venda o Carro!'
    elif 14 < distancia_litro > 8:
        return 'Econômico!'
    return 'Super econômico!'


print(distncia_por_litro(100, 10))
print(distncia_por_litro(100, 50))
print(distncia_por_litro(100, 2))

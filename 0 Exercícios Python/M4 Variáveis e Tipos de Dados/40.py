"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa
que solicite o número de dias trabalhados pelo encanador e imprima a quantia
líquida que deverá se paga, sabendo-se que são descontados 8% para imposto de
renda.
"""
# Input: quantidade de dias trabalhados.
qtrab = int(input('Quantos dias foram trabalhados: '))

# Processamento:
# Calculo do salário total com o desconto de 8%.
calct = (qtrab * 30) * 0.92

# Output:
print(f'O seu salário seŕa de R$ {calct}')

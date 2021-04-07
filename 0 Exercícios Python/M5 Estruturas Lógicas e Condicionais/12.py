"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
"Número Inválido.". Se o número for positivo, calcular o logaritimo desse
número.
"""
import math

num = int(input('Digite um número inteiro: '))

if num < 0:
    print('Número inválido.')
else:
    lognum = math.log(num)
    print(f'O logarítimo de {num} é {lognum}.')

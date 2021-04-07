"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a
raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo
que o número é invalido.
"""
import math

# Input: Digite um número:
num = int(input('Digite um número: '))

# Processamento:
if num > 0:
    sq_num = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {sq_num}.')
else:
    print('O número é invalido')

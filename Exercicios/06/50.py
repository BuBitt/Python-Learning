"""
50. Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e
    cresce 3 centimetros por ano. Escreva um programa que calcule e imprima quantos anos
    serão necessários para que Zé seja maior que Chico.
"""
c = 1.5
z = 1.1
ano = 0

while z < c:
    c += 0.02
    z += 0.03
    ano += 1
print(ano)

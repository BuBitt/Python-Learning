"""
Leia um ângulo em radianos e apresente-o convertido em graus
R = G * pi / 180
"""
# Input: valor em Radianos.
valrad = float(input('Digite o valor em radianos: '))

# Processamento: conversão do valor em Radianos em um valor em Graus.
convgrau = (valrad * 180) / 3.14

# Output: Valor convertido de Radianos para Graus.
print(f'O valor de {valrad} Radianos é equivalente a {convgrau} Graus.')

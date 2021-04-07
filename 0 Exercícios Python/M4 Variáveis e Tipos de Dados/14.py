"""
Lei a um ângulo em graus e apresente em radianos
R = (G * pi)/180
# R = radianos
# G = ângulos
"""

# input valor do ângulo em graus.
grau = float(input('Digite o valot do ângulo em graus: '))

# Processamento: conversão do valor para radianos.
convrad = (grau * 3.14) / 180

# Output: Valor convertido em radianos.
print(f'O valor de {grau} graus é equivalente a {convrad} radianos.')

"""
F = C * (9/5) + 32
K = C - 273.15

F -> K

F = (k + 273.15) * (9/5) + 32
K = ((F - 32) / (9/5)) + 273.15
"""
# Input temperatura em Fahrenheit
tf = float(input('Digite a temperatura em Fahrenheit: '))


# Conversão Fº to Kº
tfc = ((tf - 32) / (9/5))
tfk = tfc + 273.15

# Output Fº convertido em Kº
print(f'O valor em Fº convertido em Kº é {tfk}.')

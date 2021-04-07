"""
Leia a temperatura em graus Fahrenheit e apresente-a convertida em graus
Celcius.

Formula: F  = C*(9/5) + 32
"""
tempf = float(input('Digite a temperatudo em Fahrenheit: '))
tempc = (tempf - 32)/(9/5)

print(f'A temperatura convertida em Celcius é {tempc}')

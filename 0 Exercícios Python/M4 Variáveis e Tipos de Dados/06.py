"""
Leia a temperatura em graus Celcius e apresente-a convertida em graus
fahrenheit.

Formula: F  = C*(9/5) + 32
"""
tempc = float(input('Digite uma temperatura em graus Celcius: '))
tempf = float((tempc*(9/5))+32)

print(f'A temperatura em graus Fahrenheit é {tempf} graus.')

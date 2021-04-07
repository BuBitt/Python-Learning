"""
Leia um npumero inteiro de 4 dígitos (de 1000 a 9999) e imprima
um dígito por linha.
"""
# Iinput: DIgitos em string de 1000 a 9999.
num = input('Digite um númro de 1000 a 9999: ')

# Processamento: Um dígito por linha.
num1 = num[0]
num2 = num[1]
num3 = num[2]
num4 = num[3]

# Output: Um número por linha
print(f"""
{num1}
{num2}
{num3}
{num4}
""")

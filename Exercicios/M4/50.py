"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
# Input: Receber número inteiro de segundos.
tseg = int(input('Digite o tempo em segundos: '))

# Processamento: Conversões, Slices.
# Hora
thour = tseg // (60 * 60)

# Minutos
tmin = (tseg // 60)

# Segundos
tsegg = tseg

print(f'''
{thour} Horas
{tmin} Minutos
{tsegg} Segundos
''')

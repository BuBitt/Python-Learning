"""
Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
minutos e segundos. E os converta em segundos
"""
def convert_to_seconds(hours=0, minutes=0, seconds=0):
    s_hour = hours * 60 * 60
    s_minutes = minutes * 60
    
    return seconds + s_hour + s_minutes

print(convert_to_seconds(1, 20, 30))

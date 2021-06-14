"""
Faça uma função que receba a altura e o raio de um cilindro circular e teorne o volume
do cilindro.
"""
def volume_cilindro(base, altura):
    area_base = base ** 2 * 3.141592
    return area_base * altura

print(volume_cilindro(10, 10))

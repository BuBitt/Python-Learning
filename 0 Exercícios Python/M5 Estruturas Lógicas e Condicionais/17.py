"""
Programa que calcule a área de um trapézio
"""
basemaior = float(input('Digite o valor da base maior: '))
basemenor = float(input('igite o valor da base menor: '))
altura = float(input('Digite o valor da altura: '))

areat = ((basemaior + basemenor) * altura) / 2

if basemaior > 0 and basemenor > 0:
    print(f'A área do trapézio é {areat}')
else:
    print('Os valor da base são menores ou iguais a zero, portanto iválidos.')

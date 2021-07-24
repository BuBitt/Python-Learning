"""
Receba um degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá
subir para atingir seu objetivo.
"""
# Input: Altura que deseja subir, altura do degrau.
hmax = float(input('Digite a altura, em metros, que deseja alcançar: '))
hdeg = float(input('Digite a altura, em centímetros, do degrau: '))

# Processamento: Cálculo para quantidade de degraus.
qtedeg = (hmax * 100) / hdeg

# Output: Quantos degraus são necessários subir para chegar a altura desejada.
print(f'{qtedeg}')

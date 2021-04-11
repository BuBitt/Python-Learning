"""
Receba um salário base de um funcionário. Calcule e imprima o salário a
receber, sabendo-se que esse funcionário tem uma gratificação de 5%
sobre o salário base. Alem disso, ele paga 7% de imposto sobre o
salário-base.
"""
# Input: receber o valor do salário-base do funcionário.
salbas = float(input('Digite o valor do salário-base do funcionário: '))

# Processamento: como os descontos e acrecimos são sobre o salário base
#                é possível uma operação básica sobre eles 5%. - 7% = -2%.
# salfin - salario final

salfin = salbas * 0.98

# Output: Imprimir o valor total do salário pós acrescimos e descontos.
print(f'O salário do funcionário será R$ {salfin}')

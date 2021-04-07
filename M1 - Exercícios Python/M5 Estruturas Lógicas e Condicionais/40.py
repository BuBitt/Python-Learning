custo_f = float(input('Qual o valor de fábrica? R$ '))


# Custo do distribuidor:
if custo_f <= 12000:
    val_f = custo_f * 1.05

elif 12000 < custo_f <= 25000:
    val_f = (custo_f * 1.10) + (custo_f * 0.15)

else:
    val_f = (custo_f * 1.15) + (custo_f * 0.20)


# Output:
print(f'O valor total do carro é R$ {val_f}')

val_sal = float(input('\nValor do salário R$ '))
temp_serv = int(input('Tempo de serviço em anos: '))


# Reajuste do salário:
if val_sal <= 500:
    val_r = val_sal * 1.25

elif 500 < val_sal <= 1000:
    val_r = val_sal * 1.20

elif 1000 < val_sal <= 1500:
    val_r = val_sal * 1.15

elif 1500 < val_sal <= 2000:
    val_r = val_sal * 1.10

else:
    val_r = val_sal


# Bonus por tempo de serviço:
if temp_serv < 1:
    temp_r = 0

elif 1 <= temp_serv <= 3:
    temp_r = 100

elif 4 <= temp_serv <= 6:
    temp_r = 200

elif 7 <= temp_serv <= 10:
    temp_r = 300

else:
    temp_r = 500


# Output:
print(f'O valor final do salário é R$ {val_r + temp_r}\n')

peso = float(input('\nQual o seu peso em (kg)? '))
altura = float(input('Qual a sua altura (metros)? '))

imc = peso / (altura ** 2)


if imc < 18.5:
    result = 'Abaixo do Peso'

elif 18.5 < imc <= 24.9:
    result = 'Saudável'

elif 24.9 < imc <= 29.9:
    result = 'Peso em excesso'

elif 29.9 < imc <= 34.9:
    result = 'Obesidade Grau I'

elif 34.9 < imc <= 39.9:
    result = 'Obesidade Grau II (Severa)'

else:
    result = 'Obesidade Grau III (Mórbida)'


print(f'{result}\n')

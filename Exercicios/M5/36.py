valvend = float(input('Qual o seu valor de venda mensal R$ '))

if valvend > 100_000:
    comi = 700 + (valvend * 0.16)
    print(f'O valor da sua comissão é R$ {comi} .')

elif 100_000 > valvend >= 80_000:
    comi = 650 + (valvend * 0.14)
    print(f'O valor da sua comissão é R$ {comi} .')

elif 80_000 > valvend >= 60_000:
    comi = 600 + (valvend * 0.14)
    print(f'O valor da sua comissão é R$ {comi} .')

elif 60_000 > valvend >= 40_000:
    comi = 550 + (valvend * 0.14)
    print(f'O valor da sua comissão é R$ {comi} .')

elif 40_000 > valvend >= 20_000:
    comi = 500 + (valvend * 0.14)
    print(f'O valor da sua comissão é R$ {comi} .')

elif valvend < 20_000:
    comi = 400 + (valvend * 0.14)
    print(f'O valor da sua comissão é R$ {comi} .')

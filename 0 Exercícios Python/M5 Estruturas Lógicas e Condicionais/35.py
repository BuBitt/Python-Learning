"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. note que fevereiro tem 29 dias
em anos bissextos, e 28 dias em anos não bissextos.
"""
# Inputs e variáveis globais.
data = str(input('\nDigite uma data (DD/MM/AAAA): '))

bi_sex = 0  # Operador lógico do ano bissexto.
c_mes = 0  # Operador lógico da validade do Mẽs.
val_day = 0
d = 0

# Variáveis de Datas:
s_dia = data[0:2]
dia = int(s_dia)

smes = data[3:5]
mes = int(smes)

sano = data[6:10]
ano = int(sano)


# Confirmação do ano bissexto:
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    bis = bi_sex + 1
else:
    bis = 0


# Definição dos dias de fevereiro:
if bis == 1:
    fev = 29
else:
    fev = 28


# Confirmação da validade do mẽs:
if 1 <= mes <= 12:
    conf_mes = c_mes + 1
else:
    conf_mes = c_mes + 0


# Confirmação da validade do dia:
if conf_mes == 1:
    if mes == 1:  # Janeiro
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 2:  # Fevereiro
        if 1 <= dia <= fev:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 3:  # Março
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 4:  # Abril
        if 1 <= dia <= 30:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 5:  # Maio
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 6:  # Junho
        if 1 <= dia <= 30:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 7:  # julho
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 8:  # Agosto
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 9:  # Setembro
        if 1 <= dia <= 30:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 10:  # Outubro
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 11:  # Novembro
        if 1 <= dia <= 30:
            val_day = d + 1
        else:
            val_day = 0

    elif mes == 12:  # Dezembro
        if 1 <= dia <= 31:
            val_day = d + 1
        else:
            val_day = 0
    chave = 1  # Verificação para cancelamento da resposta: (validade do dia).

else:
    print(f'{s_dia}/{smes}/{sano} é uma data inválida, o mês não existe e por \
consequência o dia também não existe.\n')
    val_day = 0
    chave = 0  # Verificação para cancelamento da resposta: (validade do dia).

if not chave == 0:
    if val_day == 1:
        print(f'{s_dia}/{smes}/{sano} é uma data válida.\n')

    elif val_day == 0 and mes == 2 and dia == 29:  # Retorno especial para fev.
        print(f'{s_dia}/{smes}/{sano} é uma data inválida, o dia não existe \
no ano {sano}.\n')

    else:
        print(f'{s_dia}/{smes}/{sano} é uma data inválida, o dia não existe \
no mês {smes}.\n')

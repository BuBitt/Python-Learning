"""
59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o
    valor do kwh, e para cada habitante entre com os seguintes dados:

    consumo do mês
    o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial).
    No final imprima o maior, o menor e a média do consumo dos habitantes;
    e por fim o total do consumo de cada categoria de consumidor.
"""
import sys


n_hab = int(input('\nQuantidade de habitantes: '))
p_kwh = float(input('Preço do kw/h: '))


# Verificadores
media = 0
maior = 0
menor = sys.maxsize
s_kwh = 0

# Quantidade de cada 'código do consumidor'.
c_res = 0
c_com = 0
c_ind = 0

# Verificadores de soma para cada tipo de consumidor.
v_res = 0
v_com = 0
v_ind = 0


for ciclo in range(1, n_hab + 1):
    q_kwh = float(input('\nConsumo do mês (kw/h): '))

    while True:
        c_cod = int(input("""Código do consumidor:
1 - Residencial | 2 - Comercial | 3 - Industrial
> """))
        if c_cod < 3 and c_cod < 1:
            print(f'     * Código do consumidor inválido. *\n')

        elif c_cod == 1:
            c_res += 1
            v_res += q_kwh
            break

        elif c_cod == 2:
            c_com += 1
            v_com += q_kwh
            break

        elif c_cod == 3:
            c_ind += 1
            v_ind += q_kwh
            break

    if q_kwh > maior:
        maior = q_kwh

    if q_kwh < menor:
        menor = q_kwh

    s_kwh += q_kwh
    media = s_kwh / ciclo
print(f"""
- A média de consumo foi {media} kw/h / R$ {media * p_kwh}.
- O maior consumo foi {maior} kw/h / R$ {maior * p_kwh}.
- O menor consumo foi {menor} kw/h / R$ {menor * p_kwh}.
- A quantidade de consumidores residenciais é {c_res} e o consumo total {v_res} kw/h / R$ {v_res * p_kwh}.
- A quantidade de consumidores comerciais é {c_com} e o consumo total {v_com} kw/h / R$ {v_com * p_kwh}.
- A quantidade de consumidores industriais é {c_ind} e o consumo total {v_ind} kw/h / R$ {v_ind * p_kwh}.
""")

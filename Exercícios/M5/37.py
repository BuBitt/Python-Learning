"""
1ª e 2ª hora - R$ 1,00
3ª e 4ª hora - 1,40
5ª hora e seguintes - R$ 2,00

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste
modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo
que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao
parque e partida deste são apresentados na forma de pares de inteiros,
representando horas e minutos. Por exemplo, o par 12 50 representará
"dez para uma tarde". Pretende-se criar um programa que, lidos pelo teclado os
momentos de chegada e de partida, escreva na tela o preço cobrado pelo
estacionamento. Admite-se que a chegada e a partida se dão com intervalo não
superior a 24 horas. Portanto, se uma dada hora de chegada e à partida isso não
é uma situação de erro, antes significará que a partida ocorreu no dia seguinte
ao da chegada.
"""
# Inputs da entrada:
s_entrada = str(input('Hora de chegada (12:00): '))  # input da entrada.

h_entrada = int(s_entrada[0:2])  # Conversão da hora da entrada.
min_entrada = int(s_entrada[3:5])  # Conversão dos minutos da entrada.


# Inputs da saída:
s_saida = str(input('Hora de saída (12:00): '))  # input da saída.

h_saida = int(s_saida[0:2])  # Conversão da hora da saída.
min_saida = int(s_saida[3:5])  # Conversão dos minutos da saída.


# Entrada: Conversão dos minutos em horas:
if 1 <= min_entrada < 61:
    if min_entrada % 60 != 0:
        h_entrada += 1
    else:
        h_entrada += 0

# Saída: Conversão dos minutos em horas:
if 1 <= min_saida < 61:
    if min_saida % 60 != 0:
        h_saida += 1
    else:
        h_saida += 0

# Diferença de horas entre Entrada e Saída:
total = h_saida - h_entrada

# Cálculo para quando a hora de saída for menor que a de entrada:
if total < 0:
    total += + 24

# Output:
if 1 >= total <= 2:  # Situação 1
    print(f'O valor do estacionamento foi R$ {total}')
elif 2 < total <= 4:  # Situação 2
    print(f'O valor do estacionamento foi R$ {total * 1.40}')
elif total >= 5:  # Situação 3
    print(f'O valor do estacionamento foi R$ {total * 2.00}')
else:  # Situação 4
    print(f'O Veículo não permaneceu no estacionamento.')

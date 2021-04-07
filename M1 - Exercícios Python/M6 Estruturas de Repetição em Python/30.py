"""
30. Faça programas para calcular as seguintes sequências:

1 + 2 + 3 + 4 + 5 +.. + n
1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
1 + 3 + 5 + 7 + ... + (2n - 1)
"""
n = int(input('Digite um número: '))


# Sequência 1:
soma_1 = 0
for seq_1 in range(1, n + 1):
    soma_1 += seq_1
print(f'Resultado da sequência 1: {soma_1}')


# Sequência 2:
soma_2 = 0
for seq_2 in range(1, n * 2, 2):
    calc = (seq_2 - (seq_2 + 1))
    soma_2 += calc
print(f'Resultado da sequência 2: {soma_2}')


# Sequência 3:
soma_3 = 0
for seq_3 in range(1, 2 * n):
    soma_3 += seq_3
print(f'Resultado da sequência 3: {soma_3}')

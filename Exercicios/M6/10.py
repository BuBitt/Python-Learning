"""
10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""
s_num = 0
for num in range(0, 101, 2):
    s_num += num

print(f'O Valor da soma dos 50 primeiros números pares é {s_num}.\n')

s_t_pa = int(((2 + 100) * 50) / 2)
print(s_t_pa)

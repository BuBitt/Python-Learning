"""
58. Faça um programa que some os números primos existentes entre a e b, onde a e b são
    números informados pelo usuário.
"""
p_soma = 0
ini = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o final do intervalo: '))

for primo in range(ini, fim + 1):
    if primo == 1:
        continue

    elif primo == 2 or primo == 3 or primo == 5 or primo == 7:
        p_soma += primo

    elif not (primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0):
        p_soma += primo
print(p_soma)

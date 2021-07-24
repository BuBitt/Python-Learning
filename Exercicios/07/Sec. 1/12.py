"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores
lidos juntamente com o maior, o menor e a média dos valores.
"""
num = []
media = 0

for loop in range(1, 6):
    dn = int(input('Digite um número: '))
    num.append(dn)
    media += dn

print(f'O menor número é {min(num)}, o maior {max(num)} e a média é {media / 5}')



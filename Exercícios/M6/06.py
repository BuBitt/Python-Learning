"""
6. Faça um programa que leia 10 inteiros e imprima sua média.
"""
f_media = 0

for num in range(0, 10):
    media = int(input(f'{num+1} - Digite um número: '))
    s_media = media / 10
    f_media += s_media

print(f_media)

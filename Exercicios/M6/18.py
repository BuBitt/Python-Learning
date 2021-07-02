print("""
18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
    quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser
    fornecida pelo usuário.
""")
qte_num = int(input('Digite quantas vezes o loop vai rodar: '))
maior = -2 ** 1003
verificador = 0


for num in range(qte_num):
    inp_loop = int(input('Digite um número inteiro positivo: '))  # inp_loop = input loop
    if inp_loop > maior:
        maior = inp_loop
    if inp_loop == maior:   
        verificador += 1


if verificador > 1:
    vez = 'vezes'
else:
    vez = 'vez'

print(f'O maior número digitado foi {maior}, e ele foi digitado {verificador} {vez}.')

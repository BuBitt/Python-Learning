"""
O Bloco with

Passo para se trabalhar cpm arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivos
# 3 - Fechamos o arquivo
"""
# O bloco with - Forma pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

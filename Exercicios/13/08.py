"""
Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo
conteúdo, mas com todas as letras minúsculas convertiras para maiúsculas. Os nomes
dos arquivos serão dornecidos, via teclado, pelo usuário. A função que converte
minúsculas para maiúsculas é upper(). Ela é aplicada em cada caracter da string.
"""
import os


def maiusc(arq_in, arq_out):
    try:
        with open(arq_in) as arq_i:
            content = [arq_i.read()]
            with open(arq_out + '.txt', '+w') as arq_o:
                arq_o.write(content[0].upper())
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')
    


path_1 = input('Digite o caminho do arquivo a ser copiado: ')
path_2 = input('Digite o nome do arquivo gerado: ')
maiusc(path_1, path_2)

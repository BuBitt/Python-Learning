import os


def get_numbers(path):
    with open(path) as arq:
        lines = arq.readlines().copy()
        palavras = ' '.join(lines).lower()
        characters = list(palavras)
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        lixo = len(list(filter((lambda x: x == ' ' or x == '\n'), characters)))
        print(f'O arquivo {path} têm {len(characters) - lixo} caracteres')
        print(f'O arquivo {path} têm {len(palavras.split())} palavras.')
        print(f'O arquivo {path} têm {len(lines)} linhas.')
        for letra in alfabeto:
            print(f'* {letra.upper()}: {palavras.lower().count(letra)} vezes.')


get_numbers(os.path.join('arquivos', 'arq.txt'))
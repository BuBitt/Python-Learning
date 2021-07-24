import os


def alfabeto(path):
    with open(path) as arq:
        lines = arq.readlines()
        lines_join = ''.join(lines)
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        for i, l in enumerate(list(alfabeto)):
            print(f'A letra {l.upper()} aparece {lines_join.lower().count(l)} vezes no texto.')


print(alfabeto(os.path.join('arquivos', 'arq.txt')))

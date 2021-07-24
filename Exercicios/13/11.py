import os


def conta_palavra(path, word):
    with open(path) as arq:
        print(arq.read()
                 .lower()
                 .count(word.lower())
        )


arquivo = input('Digite o nome do arquivo: ')
word = input('Digite a palavra que deseja procurar: ')
conta_palavra(os.path.join('arquivos', arquivo + '.txt'), word)

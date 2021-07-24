import os


def qte_vogais(path):
    with open(path) as arq:
        lines = arq.readlines()
        vogais = 0
        total = 0
        for i, v in enumerate(lines):
            for letter in v:
                if letter != ' ':
                    total += 1
                if (
                    letter == 'a' or
                    letter == 'e' or
                    letter == 'i' or
                    letter == 'o' or
                    letter == 'u'
                ):
                    vogais += 1
        print(f'O total de consoantes é {total - vogais}')
        print(f'O total de vogais é {vogais}')


print(qte_vogais(os.path.join('arquivos', 'arq.txt')))

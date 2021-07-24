import os


def conta_vogal(path):
    vogais = 0
    with open(path) as arq:
        lines = arq.readlines()
        for i, v in enumerate(lines):
            vogais += v.lower().count('a')
            vogais += v.lower().count('e')
            vogais += v.lower().count('i')
            vogais += v.lower().count('o')
            vogais += v.lower().count('u')

    return vogais


if __name__ == '__main__':
    path = os.path.join('arquivos', 'arq.txt')
    print(conta_vogal(path))

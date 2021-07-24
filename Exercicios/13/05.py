import os


def find_character(path, character):
    with open(path) as arq:
        lines = arq.readlines()
        count = 0
        for i, v in enumerate(lines):
            count += v.count(character)
        return count


print(find_character(os.path.join('arquivos', 'arq.txt'), 'a'))

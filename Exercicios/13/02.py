import os


def count_line(path):
    with open(path, 'r') as arq:
        lines = arq.readlines()
        print(len(lines) + 1)


if __name__ == "__main__":
    path = os.path.join('arquivos', 'arq.txt')
    count_line(path)

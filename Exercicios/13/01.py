import os


dire = os.path.join('arquivos')
print(dire)


def cria(directory, arq_name):
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, arq_name), '+a') as arq:
        while 1:
            char = input('Digite algo: ')
            if char != '0':
                arq.write(char)
                arq.write('\n')
            else:
                break

    with open(os.path.join(directory, arq_name)) as arq:
        print(arq.readlines())


if __name__ == '__main__':
    cria(dire, 'arq.txt')

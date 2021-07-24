import os


def terceiro(path_1, path_2, name_3):
    with open(path_1) as arq_1:
        with open(path_2) as arq_2:
            with open(name_3 + '.txt', 'a') as arq_final:
                arq_final.write(arq_1.read())
                arq_final.write('\n')
                arq_final.write(arq_2.read())


name = input('digite o nome do arquivo gerado: ')
terceiro('arquivos/arq.txt', 'teste_08.txt', name)

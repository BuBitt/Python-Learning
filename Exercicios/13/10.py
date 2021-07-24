import os


def cidades(c_in, c_out):
    maior = 0
    with open(c_in) as cin:
        with open(c_out, 'w') as cout:
            lines = cin.readlines().copy()
            for i, v in enumerate(lines):
                lines[i] = v.split()
                if '\n' in lines[i][1]:
                    lines[i][1].replace('\n', '')
                if int(lines[i][1]) > maior:
                    maior = int(lines[i][1])
                    cout.write(' '.join(lines[i]))
            print(lines)


cidades('cidades.txt', 'out.txt')

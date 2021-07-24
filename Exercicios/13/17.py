def matriz(linhas, colunas):
    matriz = []
    for i in range(int(linhas)):
        temp = []
        for j in range(int(colunas)):
            temp.append('1')
        matriz.append(temp)
    return matriz


def gerador(path_in, path_out):
    with open(path_in) as arq_in:
        lines = [lines.replace('\n', '').split(' ') for lines in arq_in.readlines()]
        indices = [line for i, line in enumerate(lines) if i > 0]
        matrix = matriz(lines[0][0], lines[0][1])
        for i, line in enumerate(indices):
            matrix[int(line[0])][int(line[1])] = '0'

        with open(path_out, 'w') as arq_out:
            for i in matrix:
                count = 0
                for j in i:
                    count += 1
                    if count == int(lines[0][1]):
                        arq_out.write(f' {j}\n')
                    else:
                        arq_out.write(f' {j}')

            return print(f'Matriz de {lines[0][0]} x {lines[0][1]} gerada, com {lines[0][2]} anulações.')


gerador('17.txt', '17out.txt')

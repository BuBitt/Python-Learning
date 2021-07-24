from datetime import datetime


def arquivo(path_1, path_2):
    data = datetime.today().strftime('%d-%m-%Y')

    dia = int(data[0:2])
    mes = int(data.replace('-', '')[2:4])
    ano = int(data.replace('-', '')[4:8])

    completo = []
    idades = []

    with open(path_1) as f:
        all = f.readlines()

        for i in all:
            completo.append(list(i.replace('\n', '').split(',')))

        for i in completo:
            f_dia = int(i[1][0:2])
            f_mes = int(i[1][2:4])
            f_ano = int(i[1][4:8])
            final = ano - f_ano

            if mes == f_mes:
                if dia < f_dia:
                    final -= 1
                    idades.append(final)
                    continue
            else:
                if mes < f_mes:
                    final -= 1
                    idades.append(final)
                    continue

            idades.append(final)

        with open(path_2, 'w') as q:
            index = 0
            for i in completo:
                q.write(f'{i[0]} têm {idades[index]} anos.\n')
                index += 1


arquivo('14in.txt', '14out.txt')

import os
from datetime import datetime


def verif(ano, path_in, path_out):
    with open(path_in) as a_in:
        lines = [line.replace('\n', '').split(',') for line in a_in.readlines()]

        with open(path_out, 'w') as a_out:
            for line in lines:
                if ano - int(line[1]) < 18:
                    a_out.write(f'{line[0].title()} é menor de idade.\n')
                elif ano - int(line[1]) == 18:
                    a_out.write(f'{line[0].title()} está entrando na maior idade.\n')
                else:
                    a_out.write(f'{line[0].title()} é maior de idade.\n')


ano = int(datetime.today().strftime('%Y'))
verif(ano, '15.txt', '15out.txt')

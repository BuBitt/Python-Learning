def converter(val_dec, path_out):
    with open(path_out, 'w') as arq:
        for num in val_dec:
            arq.write(f'{bin(num)[2:]}\n')


lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
converter(lista, '16.txt')

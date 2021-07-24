def get_notas(path_in, path_out):
    try:
        print('Organizando nomes e notas.')
        with open(path_in) as arq_in:
            lines = [line.replace('\n', '').split(':') for line in arq_in.readlines()]
            nomes = []
            notas = []
            
            for line in lines:
                nomes.append(line[0])
                notas.append(int(line[1]))
                
            for i, nome in enumerate(nomes):
                if len(nome) > 41:
                    raise ValueError(f"O nome nome '{nome}' na linha '{i + 1}' tem mais de 40 caracteres.")
    
            with open(path_out, 'w') as arq_out:
                for i, nome in enumerate(nomes):
                    arq_out.write(f'{nome}{"." * (39 - len(nome))}{notas[i]}\n')

            print('Feito!')

    except ValueError as e:
        print(e)

get_notas('20in.txt', '20out.txt')

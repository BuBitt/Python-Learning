def maior_nota(path):
    with open(path) as arq:
        nota = 0
        nome = ''
        lines = [line.replace('\n', '').split(' ') for line in arq.readlines()]

        for line in lines:
            if nota < int(line[3]):
                nota = int(line[3])
                nome = line[1]
        
        return nome, nota                    

print(maior_nota('19in.txt'))

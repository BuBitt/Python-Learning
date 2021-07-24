import os


def criar(path):
    while 1:
        try:
            nome = input('Digite o nome: ')
            telefone = input('Digite o telefone: ')
            if telefone == '0':
                break

            if not telefone.isdigit():
                raise ValueError('* !!!O telefone precisa deve conter apenas números')

        except ValueError as msg_error:
            print(msg_error)
            pass
        
        else:
            with open(f'{path}.txt', '+a') as arq:
                arq.write(f'nome: {nome}, telefone: {telefone}\n')
            pass


arquivo = input('Digite um nome para o arquivo: ')
criar(os.path.join(arquivo))

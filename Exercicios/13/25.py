"""
25. Faça um programa gerenciar uma agenda de contatos. Para cada contato armazene o
nome, o telefone e o aniversário (dia e mês). O programa deve permitir

(a) inserir contato
(b) remover contato
(c) pesquisar um contato pelo nome
(d) listar todos os contatos
(e) listar os contatos cujo nome inicia com uma dada letra
(f) imprimir os aniversariantes do mês.

Sempre que o programa for encerrado, os contatos devem ser armazenados em um
arquivo binário. Quando o programa iniciar, os contatos devem ser inicializados com os
dados contidos neste arquivo binário.
"""
import datetime
import time
import re
import os


# convertendo e traduzindo binários
def w_contatos(path_out, array_contatos):
    with open(path_out, 'wb') as bin_db:
        os.chdir(os.getcwd())
        for i, contato in enumerate(array_contatos):
            nome = contato[0].encode('ascii')
            tele = contato[1].encode('ascii')
            aniv = contato[2].encode('ascii')
            # id_contato = contato[3].encode('ascii')
            sep_interno = ','.encode('ascii')
            sep_externo = '|'.encode('ascii')

            bin_db.write(nome)
            bin_db.write(sep_interno)
            bin_db.write(tele)
            bin_db.write(sep_interno)
            bin_db.write(aniv)
            # bin_db.write(sep_interno)
            # bin_db.write(id_contato)
            if not i == len(array_contatos) - 1:
                bin_db.write(sep_externo)


def r_contatos(path_in):
    with open(path_in) as bin_db:
        os.chdir(os.getcwd())
        contatos = bin_db.read().split('|')
        contatos = [contato.split(',') for contato in contatos]
        return contatos


# Tratamento da data-base

# Inserir novo contato
def inserir_contato(array_contatos):
    nome = input('\nDigite o nome do contato: ')
    while 1:
        try:
            telefone = input(f'Digite o telefone de {nome} (DD000000000): ')
            if len(telefone) != 11:
                raise ValueError('\n(!) Número inválido (!)\n')

        except ValueError as err:
            print(err)
            pass

        else:
            break

    while 1:
        try:
            aniversario = input(f'Digite a data de aniversário de {nome} (DDMMAAAA): ')
            if len(aniversario) != 8:
                raise ValueError('\n(!) Data inválida inválido (!)\n')

        except ValueError as err:
            print(err)
            pass

        else:
            break

    id_contato = str(len(array_contatos))
    contato = [nome, telefone, aniversario, id_contato]
    array_contatos.append(contato)

    print(f'\n(!) O contato "{contato[0]}" foi Adicionado (!)')
    print("=" * 84)
    time.sleep(1)


# Remover contato pelo ID
def remove_contato(array_contatos):
    while 1:
        try:
            id_contato = int(input('\nDigite o id do contato que deseja remover: '))

        except ValueError:
            print('\n(!) Id inválido (!)\n')
            pass

        else:
            break

    print(f'(!) O contato "{array_contatos[id_contato][0]}" foi removido.')
    while 1:
        try:
            array_contatos.pop(id_contato)
        except IndexError:
            print('\n(!) Id não existe nos contatos (!)\n')
            pass
        else:
            print("=" * 84)
            time.sleep(1)
            break


# Pesquisar contato pelo nome
def achar_palavra(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def pesquisar_contato(array_contatos):
    nome = input('Digite o nome que deseja procurar: ')
    encontrados = []
    enc = False

    for contato in array_contatos:
        nome_contato = contato[0]

        if achar_palavra(nome)(nome_contato) is not None:
            encontrados.append(contato)
            enc = True
    if enc:
        print(f'\n(!) TABELA DE CONTATOS COM A PALAVRA "{nome}" (!)\n')
        time.sleep(0.5)
        return listar_contatos(encontrados)
    else:
        print('\n(!) Palavra não encontrada nos nomes (!)')
        print('"=" * 84')
        time.sleep(1)


# Cria tabela de contatos
def listar_contatos(array_contatos):
    # Cabeçalho da tabela
    print(f'+{"-" * 6}+{"-" * 40}+{"-" * 17}+{"-" * 16}+')
    print(f'|  id  |  NOME{" " * 34}|  TELEFONE       |  ANIVERSÁRIO   |')
    print(f'+{"-" * 6}+{"-" * 40}+{"-" * 17}+{"-" * 16}+')

    for i, contato in enumerate(array_contatos):
        # id_contato index
        id_contato = i

        if not int(id_contato) < 10:
            id_contato = i
        else:
            id_contato = '0' + str(id_contato)

        # id contato no-index
        """id_contato = contato[3]
        
        if not int(id_contato) < 10:
            id_contato = contato[3]
        else:
            id_contato = '0' + id_contato"""

        # Nome
        nome = contato[0][0:39]
        nome = nome + " " * (39 - len(nome))

        # Telefone
        tel = str(contato[1])
        tel = "(" + tel[0:2] + ") " + tel[2:7] + "-" + tel[7::]

        # Aniversário
        ani = str(contato[2])
        ani = ani[0:2] + "/" + ani[2:4] + "/" + ani[4:]

        # Saída para a tabela
        print(f'|  {id_contato}  | {nome}| {tel} |   {ani}   |')
    print(f'+{"-" * 6}+{"-" * 40}+{"-" * 17}+{"-" * 16}+')


# Procura e gera lista com nomes que começam com a letra determinada
def lista_por_letra(array_contatos):
    while 1:
        try:
            letra = input('Digite uma letra para procurar: ')
            if len(letra) != 1:
                raise ValueError('Você deve digitar apenas uma letra.')

        except ValueError as err:
            print(err)
            pass

        else:
            break

    encontrados = []
    for contato in array_contatos:
        p_letra_array = contato[0][0]
        if letra == p_letra_array:
            encontrados.append(contato)

    if len(encontrados) > 0:
        print(f'(!) IMPRIMINDO TABELA DOS CONTATOS COM INÍCIO "{letra.upper()}" (!)\n')
        time.sleep(0.5)
        return listar_contatos(encontrados)
    else:
        print('(!) Primeira letra não encontrada nos nomes (!)')
        print("=" * 84)
        time.sleep(1)


# Imprimir os aniversários do dia
def imprimir_aniversarios(array_contatos):
    encontrados = []

    current_time = datetime.datetime.now()
    mes_atual = current_time.month
    dia_atual = current_time.day

    for contato in array_contatos:
        mes_contato = int(contato[2][2:4])
        dia_contato = int(contato[2][0:2])

        if mes_atual == mes_contato:
            if dia_atual == dia_contato:
                encontrados.append(contato)

    if len(encontrados) > 0:
        print('\n(!) IMPRIMINDO TABELA DE ANIVERSARIANTES DO DIA (!)\n')
        time.sleep(0.5)
        return listar_contatos(encontrados)

    else:
        print('(!) Não há nenhum aniversariante hoje (!)')
        print("=" * 84)
        time.sleep(1)


def menu():
    array_contatos = r_contatos('25out.bin').copy()
    print('\n(!) AS MODIFICAÇÕES SERÃO VALIDADAS SOMENTE APÓS SAIR (!)')

    while 1:
        print("""
(a) Inserir contato
(b) Remover contato
(c) Pesquisar um contato pelo nome
(d) Listar todos os contatos
(e) Listar os contatos cujo nome inicia com uma dada letra
(f) Imprimir os aniversários do mês

(s) SAIR""")
        print("=" * 84)
        try:
            opc = input('> ').lower()

            if len(opc) > 1:
                raise ValueError('\n(!) A opção pode conter apenas UMA letra.')

            if opc == 's':
                w_contatos('25out.bin', array_contatos)
                break

            # Inserir contato
            if opc == 'a':
                inserir_contato(array_contatos)
                continue

            # Remover contato
            if opc == 'b':
                remove_contato(array_contatos)
                continue

            # Pesquisar um contato pelo nome
            if opc == 'c':
                pesquisar_contato(array_contatos)
                continue

            # Listar todos os contatos
            if opc == 'd':
                listar_contatos(array_contatos)
                continue

            # Listar os contatos cujo nome inicia com uma dada letra
            if opc == 'e':
                lista_por_letra(array_contatos)
                continue

            # Imprimir os aniversários do mês
            if opc == 'f':
                imprimir_aniversarios(array_contatos)
                continue

            else:
                raise ValueError('(!) O valor Digitado é inválido.')

        except ValueError as err:
            print(err)
            print("=" * 84)
            time.sleep(1)
            pass


def populando_out():
    array_contatos = []

    for i in range(50):
        id_contato = str(i)
        nome = 'Testando Nome Composto'
        telefone = '87996047768'
        data_nas = '26052000'
        local = [nome, telefone, data_nas, id_contato]
        array_contatos.append(local)
        print(array_contatos)

    w_contatos('25out.bin', array_contatos)


def main(val=1):
    if val == 1:
        menu()
    else:
        populando_out()


if __name__ == '__main__':
    main()

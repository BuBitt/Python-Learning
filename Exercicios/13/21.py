"""
Crie um programa que receba como entrada o número de alunos de uma disciplina. Aloque dinamicamente
em uma estrutura para armazenas informações a respeito desse alunos: nome do aluno e sua nota final.
Use nomes com no máximo 40 caracteres. Em seguida, salve os dados dos alunos em um arquivo binário.
Por fim, leia o arquivo e mostre o nome do aluno a maior nota.
"""


def bin_write(path_out, iterable_contents):
    """Converte para binário os valores passados em 'input_notas()'"""
    
    with open(path_out, 'wb') as arq_out:
        for _, content in enumerate(iterable_contents):

            # Converte os valores a serem escritos para binário
            b_nome = bytearray(content[0].encode('UTF-8'))
            b_nota = bytearray(content[1].encode('UTF-8'))
            b_sep_nota = bytearray(':'.encode('UTF-8'))
            b_sep_nome = bytearray('|'.encode('UTF-8'))

            # Escreve os valores
            arq_out.write(b_sep_nome)
            arq_out.write(b_nome)
            arq_out.write(b_sep_nota)
            arq_out.write(b_nota)
            arq_out.write(b_sep_nome)


def bin_translate(s):
    return s.decode('UTF-8')


def input_notas(path_in, path_out):
    """Função para lidar com os inputs de nome e nota."""
    
    with open(path_in) as arq_in:
        qte_alunos = int(arq_in.readline().replace('\n',''))
        nomes = []
        notas = []
        
        print(f'Serão adicionados um total de {qte_alunos} alunos:')
        for i in range(qte_alunos):
            while 1:
                try:
                    aluno = input('\nDigite o nome do aluno: ').strip()
                    if len(aluno) > 40:
                        raise ValueError('O nome não pode possuir mais de 40 caracteres.')

                    nota = input('Digite a nota do aluno [0-10]: ')
                    if not nota.isdigit():
                        raise ValueError('A digitada precisa ser um número.')
                    if int(nota) > 10:
                        raise ValueError('A nota precisa estar entre 0 e 10.')
                
                except ValueError as err:
                    print(err)
                    pass
                
                else:
                    nomes.append(aluno)
                    notas.append(nota)
                    break
        
        nomes = tuple(nomes)
        notas = tuple(notas)
        return_zip = tuple(zip(nomes, notas))
        
        bin_write(path_out, return_zip)


def maior_nota(path_bin, path_in):
    input_notas(path_in, path_bin)
    
    maior = 0
    nome = ''
    with open(path_bin, 'rb') as arq_in:

        notas = tuple(filter(None, tuple(arq_in.read().decode('UTF-8').split('|'))))
        
        for nt in notas:
            nt = nt.split(':')
            num_atual = int(nt[1])
            
            if num_atual > maior:
                maior = num_atual
                nome = nt[0]


    print(f'\n\nO Aluno de maior nota é {nome.title()}, com nota {maior}.\n')


def main():
    maior_nota('21out.bin', '21in.txt')


main()

"""
Modo de abertura de arquivos

r - Abre para leitura - padrão
w - Abre para escrita - Sobrescreve caso o arquivo já existe, e o cria caso não exista
x - Abre para escrita somente se o arquivo não existir.
a - Abre para escrita, mas não sobrecreve, apenas adiciona o texto ao já existene aoo final do arquivo.
    com o modo 'a', não controlamos o cursor.
+ - Abre para o modo de atualização (leitura/escrita)

https://docs.python.org/3/library/functions.html#open
"""
# teste
try:
    with open('texto.txt', 'x') as aq:
        aq.write('teste de conteúdo.\n')
except FileExistsError:
    print('O arquivo já existe')


# Exemplo a de 'a'
with open('texto.txt', 'a') as aq:
    while 1:
        fruta = input('Digite o nome de uma fruta: ')
        if fruta != 'sair':
            aq.write(fruta)
            aq.write('\n')
        else:
            break


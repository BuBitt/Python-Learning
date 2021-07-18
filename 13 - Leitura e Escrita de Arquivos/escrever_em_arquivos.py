"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura não podemos realizar escrita nele. Da mesma forma, se abrirmos para escrita, não
podemos lê-lo, somente escrever, e vice-versa.
"""

# Exemplo de escrita - modo 'w' - write (escrita)
with open('texto.txt', 'r') as arquivo:
    print(arquivo.readlines())


with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil 1\n')
    arquivo.write('+++++++++++++++++++++++++++++++++++++++++\n')
    arquivo.write('-----------------------------------------\n')
    arquivo.write('=========================================')


with open('texto.txt', 'r') as arquivo:
    print(arquivo.readlines())


# OBS: Abrindo o arquivo para escrita todo o conteúdo deste arquivo será perido, se o arquivo não exitir
#      ele será criado.

with open('frutas.txt', 'w') as arq:
    while 1:
        fruta = input('Digite uma fruta: ')
        if fruta != 'sair':
            arq.write(fruta)
            arq.write('\n')
        else:
            break

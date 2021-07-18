"""
Leitura de arquivos

Para ler o conteúdo de um aruivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> a forma mais simples de utilização, nós passamos apenas um parâmetro de entrada
que neste caso é o nome do arquivo a ser lido. Essa função retorna uma __io.TextIOWrapper
e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir,
ou então teremos FileNotFoundError

<_io.TextIOWrapper name='./13 - Leitura e Escrita de Arquivos/txt.txt' mode='r' encoding='UTF-8'>

mode r -> Modo de leitura. r -> read() -> ler
"""

arquivo = open('./13 - Leitura e Escrita de Arquivos/texto.txt')
# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a dunção read()

ret = arquivo.read()
print(type(ret))

print(ret)

# OBS: O Python, utiliza um um recurso para trabalhar com um arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# A função raed() lê todo o conteúdo do arquivo.

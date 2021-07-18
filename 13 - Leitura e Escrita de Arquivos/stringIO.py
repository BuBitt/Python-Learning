"""
String IO

ATENÇÃO! Para ler ou escrever addos em arquivos do sistema operacional o software precisa de
permissão de leitura para ler o arquivo, permissão de escrita para ler o arquivo.

stringIO -> utilizado para ler e crar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO


msg = 'Teste de mansagem string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois.
arq = StringIO(msg)
# arquivo = open('arquivo.txt', 'w')
print(arq.read())

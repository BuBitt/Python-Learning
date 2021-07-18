"""
Sistemas de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer
uso do modulo os.

os -> Operating System - Sistema Operacional
"""
# Fazer import
import os


# getcwd() -> Pega o current work directory - diretório de trabalho corrente
# retona o path (caminho) absoluto
print(os.getcwd())                  # Diretório atual


# Para mudar o diretório, podemos utilizar o chdir()
# os.chdir('..')
# print(os.getcwd())


# Para saber qual sistema de arquivos:
print(os.name)
print(os.uname())


# diretórios multiplataforma
dir = os.getcwd()

# Veja que o os.path.join() recebe 2 ou mais parâmetros, o diretorio atual e as junções.
res = os.path.join(dir, 'teste')    # junta os jois parâmetros
os.chdir(res)                       # Muda o diretório atual para o dejesado
print(os.getcwd())                  # Diretório atual
print(os.listdir())                 # Lista arquivos em uma lista python.
print(len(os.listdir(dir)))         # Quantidade de arquivos listados.


# Podemos listar arquivos e diretórios com mais detalhes com scandir()
scanner = os.scandir()              # Abre o scandir()
arquivos = list(os.scandir())       # Listando diretórios

print(arquivos)
# print(dir(arquivos[0]))

print(arquivos[0].inode())          # Numeração do objeto na arvore de diretórios.
print(arquivos[0].is_dir())         # É um diretório?
print(arquivos[0].is_file())        # É um arquivo?
print(arquivos[0].is_symlink())     # É um link simbólico?
print(arquivos[0].name)             # Nome do arquivo
print(arquivos[0].path)             # Caminho até o arquivo
print(arquivos[0].stat())           # Estatisticas: tamanho entre outros.

# Quando utilizamos a função scandir() nós precisamos fechá-la, assim como quando abrimos um arquivo.
scanner.close()                     # Fehcar o scandir()

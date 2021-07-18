"""
Sistema de Arquivos - Manipulação
"""
import tempfile
import os

# Diretório

# Descobrindo se um arquivo ou diretório existe
# Path relativo
print(os.path.exists('frutas.txt'))              # True
print(os.path.exists('teste/teste.py'))          # False
print(os.path.exists('false.txt'))               # False
print(os.path.exists('teste/tes.py'))            # True

# Path absoluto
print(os.path.exists('/etc'))                    # True


# Criando arquivos
# Formas não recomendadas:

# Forma 1
open('teste_1.txt', 'w').close()

# Forma 2
open('teste_2.txt', 'a').close()

# Forma 3
with open('teste_3.txt', 'w') as target:
    pass

# Forma recomendada:
os.mknod('criacao-recomendada.txt')
os.mknod('/home/bruno/Documents/teste.txt')

# OBS: Se você estiver utilizando no MacOS, pode haver um PermissionError
# OBS: Criando um arquivo via mknod() se o arquivo ja existir haverá um erro

# Criando diretório:
os.mkdir('teste')

# OBS: A função mkdir() cria um diretório se este não existir, caso exista, teremos FileExistsErros

# Criando multiplos diretórios e ignorando caso já existam diretórios com o mesmo nome.
os.makedirs('teste_m/teste_m/teste', exist_ok=True)

# Renomear arquivos e diretórios
os.rename('teste', 'teste_rename_2')
# OBS: Se o diretório não existir teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos OSError


# deleção -> ao deletarmos um arquivo eles não vão para lixeira, eles somem
os.remove('testedel.txt')

# Removendo diretórios vazio
os.rmdir('diretorio')

# Removendo uma árvore de diretórios
for arquivo in os.scandir('teste_rename'):
    print(f'- {arquivo.name}', arquivo.path)
    if arquivo.is_dir():
        os.rmdir(arquivo.path)


# Trabalhando com arquivos temporarios
with tempfile.TemporaryDirectory() as tmp:
    print(f'Creiei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arq:
        arq.write('Testando arquivos temporários\n')
    input()


# Estamos criando um diretório temporário, abrindo o mesmo e dentro ele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporário 'vivos' dentro dos blocos with.

# OBS: Possivelmente, o código acima não irá funcionar se você esticver utilizando
# o windows. por conta desse sistema trabalhar de forma diferente com arquivos temporários.


# Criando um arquivo temporários
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Testando inscricao em binarios\n')
    tmp.seek(0)
    print(tmp.read())

# Em arquivos temporario só conseguimos escrever bits. Por isso, usamos b antes da string
# https://docs.python.org/3/library/os.html?highlight=os#module-os

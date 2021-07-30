"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.
"""
arquivo = open('texto.txt')

arquivo.seek(0)
print(arquivo.read())


# seek() -> É utilizada para a movimentação do cursor pelo aquivo. Ela recebe um parâmetro que indica
# onde queremos colocar o cursor

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)  # seek(0)
print(arquivo.read())

arquivo.seek(600)
print(arquivo.read())

# readline()
ret = arquivo.readline() * 5

print(ret)

print(ret.split(' '))


# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: quando abrimos um arquivo com a função open() é criada uma conexão ebtre o arquivos
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos dechar a conexão. Para isso utilizamos a função close()

para trabalhar com arquivos:

# 1 - Abrir arquivo;

# 2 - Trabalhar no arquivo;

# 3 - Fechar o arquivo.


# 1 - Abrindo arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhando no arquivo
print(arquivo.read())
print(arquivo.closed)

# 3 - Fechar arquivo
arquivo.close()


print(arquivo.closed)

# Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError


arquivo = open('texto.txt')

# Com a função read podemos limitar a quandidade de caracteres lidos no arquivo.
print(arquivo.read(50))

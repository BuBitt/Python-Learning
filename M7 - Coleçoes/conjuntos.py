"""
Conjuntos:
---------------------------------------------------------------------------------------

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntos
  da matemática.

- No Python os conjuntos são chamados de Sets

---------------------------------------------------------------------------------------

# Definindo um conjunto:


# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erros e não fará parte do conjunto.


# Froma 2:  # Mais comum

s = {1, 2, 3, 4, 5, 5, 6, 2, 3}
print(s)
print(type(s))


# Podemos verificar se determinado elemento está contido em determinado conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('não tem o 3')

---------------------------------------------------------------------------------------

# Importante lembrar que, além de não termos valores duplicados não temos ordem


# Listas aceitam valores duplicados, então temos 10 elementos.
lista = [99, 23, 23132, 12, 123, 123, 11, 12]
print(lista)
print(len(lista))


# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 23, 23132, 12, 123, 123, 11, 12)
print(tupla)
print(len(tupla))


# Dicionários não aceitam chaves duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 23, 23132, 12, 123, 123, 11, 12], 'dict')
print(dicionario)
print(len(dicionario))


# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjuntos = {99, 23, 23132, 12, 123, 123, 11, 12}
print(conjuntos)
print(len(conjuntos))

---------------------------------------------------------------------------------------

# Assim como todo outro conjunto Python, podemos colocar to dos os tipos de dados misturados em sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))


# Podemos iterar em um set normalmente:
for valor in s:
    print(valor)

---------------------------------------------------------------------------------------

# Usos interessantes com sets:

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informaram
# manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))  # Quantidade de pessoas que vieram.

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# o que você faria?

print(len(set(cidades)))

---------------------------------------------------------------------------------------

# Adicionando elementos em um conjunto:


s = {1, 2, 3}
print(s)


s.add(4)
print(s)


s.add(4)  # Simplesmente é ignorado e não é adicionado.
print(s)

---------------------------------------------------------------------------------------

# Remover elementos em um conjunto:

s = {1, 2, 3}
print(s)


# Forma 1
s.remove(3)  # Não é índice, informamos o valor a ser removido.
print(s)
# OBS: Caso o valor não seja encontrado, será gerado o erro KeyError. Nenhum valor é retornado.


# Forma 2
s.discard(2)
print(s)
# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Erros:
# s.remove(22)
# print(s)

---------------------------------------------------------------------------------------

s = {1, 2, 3}
print(s)

# Copiando um conjunto para outro:

# Deep Copy
novo_conjunto = s.copy()
print(novo_conjunto)
print(s)


# Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)

---------------------------------------------------------------------------------------

# Podemos remover todos os itens de um conjunto


s = {1, 2, 3}
print(s)

s.clear()
print(s)

---------------------------------------------------------------------------------------

# Métodos matemáticos de conjuntos

# Imagine que temos 2 conjuntos: Um contendo estudantes do curso python e um
# contendo estudantes do curso de Java

estudantes_python = {'Bruno', 'Pedro', 'Well', 'Marília', 'Alguém Aí'}
estudantes_java = {'Bruno', 'Pedro', 'Well'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos


# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)


# Forma 2 - Utilizando o Caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

---------------------------------------------------------------------------------------

# Gerar um conjunto de estudantes que estudam ambos os cursos


estudantes_python = {'Bruno', 'Pedro', 'Well', 'Marília', 'Alguém Aí'}
estudantes_java = {'Bruno', 'Pedro', 'Well'}


# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)


# Forma 2 - &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

---------------------------------------------------------------------------------------

# Gerar um conjuto de estudantes que não estão no outro curso


estudantes_python = {'Bruno', 'Pedro', 'Well', 'Marília', 'Alguém Aí'}
estudantes_java = {'Bruno', 'Pedro', 'Well', 'Mõnica Away'}

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

---------------------------------------------------------------------------------------

# Soma*, Valor Máximo, Valor Mínimo, Tamanho
# * Se os valores forem todos inteiros ou reais


s = {1, 2, 3, 4, 5, 6}

print(sum(s))  # Soma
print(max(s))  # Número Máximo
print(max(s))  # Número Minimo
print(len(s))  # Tamanho


---------------------------------------------------------------------------------------
"""

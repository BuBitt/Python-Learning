"""
Listas:

Listas em python funcionam como vetores ou matrizes, ou seja, arrays em outras linguagens, com a
diferença de serem DINÂMICO e também podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
      Ou seja, nestas linguagens se você criar um arrays de tipo int e com tamanho 5, este array
      será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

já em Python:
    - Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando
      elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de
      dado;

OBS: Listas são mutáveis, ou seja, elas podem mudar constantemente.
-------------------------------------------------------------------------------------------------------
lista1 = [1, 99, 4, 24, 54, 45, 65, 75, 34, 342, 23, 2342, 34, 234, 239]

lista2 = ['B', 'r', 'u', 'n', 'o', 'B', 'i', 't', 'u']

lista3 = []

lista4 = list(range(11))

lista5 = list('José Lopes')
-------------------------------------------------------------------------------------------------------

As listas em Python são representadas por colchetes: []
# Podemos facilmente checar se determinado valor estar contido na lista.
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')


# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)


# Podemos facilmente conta o número de ocorrências de um valor em uma lista
print(lista1.count(34))
print(lista5.count('r'))


# Adicionar elementos em Listas
# Para adicionar elementos ou valores em listas, utilizamos a função append()
print(lista1)
lista1.append(42)
print(lista1)


# OBS: Com append nós só conseguimos adicionar 1 elemento por vez
# lista1.append(1, 2, 3)  # Erro
lista1.append([8, 3, 1])  # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
    print(lista1)
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional a lista
print(lista1)


# Podemos inserir um novo elemento na lista informando a posição do indice:
# Não substitui o valor inicial. O mesmo será deslocado para a direita na lista.
lista1.insert(2, 'Novo valor')
print(lista1)


# Podemos Facilmente juntar duas listas:
# lista1.extend(lista2)
# lista1 += lista2
# lista6 = lista1 + lista2
print(lista6)


# Podemos facilmente inverter listas:
# Forma 1:
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2:
print(lista1[::-1])
print(lista2[::-1])


# Copiar uma lista
lista6 = lista2.copy()
print(lista6)


# Contagem dos elementos existentes dentro de uma lista:
print(len(lista1))


# Podemos facilmente remover o ultimo elemento de uma lista:
# OBS: A função .pop() também retorna o ultimo elemento removido;
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice:
# OBS: Os elementos á direita são deslocados para a esquerda;
# OBS: Se não houver elemento no índice informado teremos um index error.
lista5.pop(2)
print(lista5)


# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista:
# Exemplo 1:
# OBS: Por padrão, o split() separa os elementos da lista pelo ESPAÇO entre elas
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2:
# Quando ',' está dentro do parenteses do split(), alista é criada com a virgula como divisor
curso = 'Programação, em, python:, essencial'
print(curso)
curso = curso.split(',')
print(curso)


# Convertendo uma lista em uma string:
lista6 = ['Programação', 'em', 'python:', 'essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista 6, coloca ' ' entre os elementos e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)


# Podemos realmente colocar qualquer tipo de dado em uma string inclusive misturando-os
lista6 = [1, 1.2, True, 'Geek', 'd', [1, 2, 3], 136817264781264]
print(lista6)
print(type(lista6))


# Iterando sobre listas:
# Exemplo 1:
soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 - Utilizando while:
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "Sair" para sair.')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Utilizando Variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento está ligado ao início da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
print(cores[-4]) # Erro, pois não existe índice [-5].

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar índice em um for:
for indice, cor in enumerate(cores):
    print(indice, cor)


# Listas aceitam repetições
lista = []

lista.append(33)
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)


#  Métodos não tão importantes, porém úteis
# ------------------------------------------
# Encontrar o índice de um elemento na lista
numeros = [5, 6, 5, 7, 8, 9, 10]

# Em qual indice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# print(numeros.index(19))  # Gera value error

# OBS: Caso não tenha este elemento na lista, será apresentado ValueError

# OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range(), ou seja, qual índice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do índice 1
print(numeros.index(5, 2))  # buscando a partir do índice 1
print(numeros.index(5, 3))  # buscando a partir do índice 1
print(numeros.index(5, 4))  # buscando a partir do índice 1
# OBS: Caso não tenha este elemento na lista, será apresentado ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o índice 8 entre 3 e 6


# Revisão slicing
# lista[inicio:fim:passo]
# range(inicio, fim, passo)

# Trabalhando com slice de listas com o parâmetro 'inicio'
lista = [1, 2, 3, 4]

print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[::])  # Pegando todos os elementos da lista

# Trabalhando com slice de listas com o parâmetro 'fim'
print(lista[:2])    # Começa em 0, pega até o índice 2 - 1
print(lista[:4])    # Começa em 0, pega até o índice 4 - 1
print(lista[1:3])   # Começa em 1, pega até o índice 3 - 1

# Trabalhando com slice de listas com o parâmetro 'passo'
print(lista[1::2])    # Começa em 1, vai até o final de 2 em 2
print(lista[::2])     # Começa em 0, vai até o final de 2 em 2
print(lista[1::-1])   # Começa em 1, vai do final até o começo de 1 em 1


# Invertendo valores em uma lista:
nomes = ['Joca', 'Pedro', 'Marília']
nomes[0], nomes[1] = nomes[1], nomes[0]

nomes.reverse()
print(nomes)


# Como realizar soma*, procurar valor máximo*, valor mínimo* e tamanho de uma lista
# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista


# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista, type(lista))

tupla = tuple(lista)
print(tupla, type(tupla))


# Desempacotamento de listas:
# Transformar uma lista em tupla
lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber
# os dados, teremos ValueError


# Copiando um lista uma lista para outra (Deep Copy e Shallow Copy)
# Forma 1 (Deep Copy):

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(nova)

# Veja que ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista não afeta a outra, isso em Python
# é chamado de Deep Copy (Cópia Profunda)

# Forma 2 (Shallow Copy):
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que foi utilizado a copia via atribuição e copiamos os dados da lista para a nova lista,
# mas após realizar modificação em uma das listas, essa modificação foi refletida na outra lista.
# Em Python, isso é chamado de shallow copy.
"""

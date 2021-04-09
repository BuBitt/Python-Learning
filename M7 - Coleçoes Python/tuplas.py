"""
Tuplas (tuple):
--------------------------------------------------------------------------------------------------
Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por parenteses ();
2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla ela não muda. Toda
    operação em um tupla gera uma nova tupla.
--------------------------------------------------------------------------------------------------

# CUIDADO 1: As Tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1, type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2, type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4)                    # Não é uma tupla.
print(tupla3, type(tupla3))

tupla4 = (4,)                   # Isso é uma tupla.
print(tupla4, type(tupla4))

tupla5 = 4,
print(tupla5, type(tupla5))
# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parenteses

(4) -> Não é tupla.
(4,) > É tupla.
4, > É tupla.

--------------------------------------------------------------------------------------------------

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla, type(tupla))

--------------------------------------------------------------------------------------------------

# Desempacotamento de tupla
tupla = ('Escola Técnica Estadual', 'Programação em Python: Essencial')
escola, curso = tupla

print(escola)
print(curso)
# Gera ValueError se colocarmos um número diferente de elementos para desempacotar

--------------------------------------------------------------------------------------------------

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato
  das tuplas serem imutáveis

--------------------------------------------------------------------------------------------------

# Soma*, Valor máximo*, Valor Mínimo*, e Tamanho
# * Se os valores forem todos inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))  # Soma
print(max(tupla))  # Maior Número
print(min(tupla))  # Menor Número
print(len(tupla))  # Tamanho da tupla

--------------------------------------------------------------------------------------------------

# Concatenação de tuplas:
tupla1 = (1, 2, 3,)
print(tupla1)

tupla2 = (4, 5, 6,)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)


tupla1 += tupla2  # Tuplas são imutáveis, mas podemos reescrever seus valores.
print(tupla1)

--------------------------------------------------------------------------------------------------

# Verificar se determinado elemento está contido na tupla
tupla1 = (1, 2, 3)
print(1 in tupla1)

--------------------------------------------------------------------------------------------------

# Iterando sobre uma tupla
tupla1 = (1, 2, 3)

for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

--------------------------------------------------------------------------------------------------

# Contando elementos dentro de uma tupla:
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Escola Técnica')
print(escola)
print(escola.count('a'))

--------------------------------------------------------------------------------------------------

# Dicas na utilização de tuplas:

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla também é semelhante as listas
print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

--------------------------------------------------------------------------------------------------

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# Identificamos em qual índice está na tupla

print(meses.index('Junho'))     # Identifica o primeiro;
print(meses.index('Junho', 6))  # A partir de um certo index.

# OBS: Caso o elemento não exista, será gerado erro ValueError.

--------------------------------------------------------------------------------------------------

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# Slicing

# tupla[inicio:fim:passo]

print(meses[::])
print(meses[5::])
print(meses[5:8:])
print(meses[5::-1])

--------------------------------------------------------------------------------------------------

# Por que utilizar tuplas?

# - tuplas são mais rápidas do que listas
# - tuplas deixam seu código mais seguro

# - Isso por que trabalhar com elementos imutáveis traz segurança para o código

--------------------------------------------------------------------------------------------------

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o prblema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova += outra
print(nova)
print(tupla)

--------------------------------------------------------------------------------------------------
"""

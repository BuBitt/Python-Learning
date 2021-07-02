"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais:
    - Variáveis globais sao reconhecidas, ou seja, seu escopo compreende todo
    o programa.


2 - Variáveis Locais:
    - Variáveis locais sao reconhecidas apenas no bloco onde foram declaradas,
    ou seja, seu escopo está limitado ao bloco onde foi declarada.


Para declarar variáveis em Python fazemos:
nome_da_variável = valor_da_variável



Python é uma linguagem de tipagem dinâmica, isso significa que
ao declararmos uma variável, nós nao colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor a ela.

Exemplo em C:
int numero = 42

Exemplo em Java:
int numero = 42
"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))


# A variável novo está declarada localmente dentro do bloco 'if', portanto é
# local.
numero = 2

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)

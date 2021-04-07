"""
Loop -> Estruturas de repetição.
For - > Uma dessas estruturas.

# C ou Java
for(int i = 0; i < 10; i++){
    //execução do loop
}

# Python
for item in interval:
    //execução do loop



Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos iteráveis:
- String
    nome = 'geek university'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    Numeros = range(1, 10)
|-------------------------------------------------------------------------|


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]  # Temos que transformar em uma lista
numeros = range(1, 10)


# Exemplo de for 1 (iterando sobre uma string):
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista):
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range):
--------------------------------------------------
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive (incluído).

incluído: 1, 2, 3, 4, 5, 6, 7, 8, 9.
não incluído: 10.
--------------------------------------------------
for numero in range(1, 10):
    print(numero)
--------------------------------------------------
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]  # Temos que transformar em uma lista
numeros = range(1, 10)

Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

--------------------------------------------------
for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor podemos descarta-lo usando um underline (_)
--------------------------------------------------

for valor in enumerate(nome):
    print(valor[0])

for n in range(1, qte + 1):
    print(f'Imprimindo {n}')
--------------------------------------------------

qte = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qte + 1):
    num = int(input(f'Informe o {n}/{qte} valor:'))
    soma = soma + num
print(f'A soma é {soma}')
---------------------------------------------------

nome = 'Geek University'

for letra in nome:
    print(letra, end='')
"""

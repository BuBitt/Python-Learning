"""
Ranges:

- Precisamos conhecer o loop for para usar os ranges.
- precisamos conhecer o range para trabalhar melhor com os loops fo.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.


Formas gerais:

# Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo forma 1
for num in range(11):
    print(num)


# Forma 2
range(valor_de_inicio, valor_de_parada)

# Exemplo forma 2
for num in range(0, 11):
    print(num)


# Forma 3
range(valor_de_início, valor_de_parada, passo)

OBS: Passo especificado pelo usuário. Passo é de quantos em quantos números o programa conta.

# Exemplo forma 3
for num in range(0, 11, 2):
    print(num)


# Forma 4 (inversa/Decrescente)
range(valor_inicio, valor_de_parada, passo)

# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)

"""

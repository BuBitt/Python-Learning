"""
------------------------------------------------------------------------------------

Mapas -> Conhecidos em Python como dicionários.

Dicionários em python são representados por chaves {}

------------------------------------------------------------------------------------

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)


# Iterar sobre dicionários:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

------------------------------------------------------------------------------------

# Acessando Valores:

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

------------------------------------------------------------------------------------

# Acessando Valores:

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita.values())

for valor in receita.values():
    print(valor)

------------------------------------------------------------------------------------

# Desempacotamento de dicionários:  # tuplas

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

------------------------------------------------------------------------------------

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho:
# * Se os valores forem todos inteiros ou reais

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

------------------------------------------------------------------------------------
"""

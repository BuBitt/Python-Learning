"""
Dicionários:
------------------------------------------------------------------------------------

OBS: Em algumas linguagens de programação, os dicionários python são conhecido spor mapas,

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))


OBS: Sobre dicionários
     - have e valor são separados por dois pontos 'chave:valor';
     - Tanto chave quanto valor podem ser qualquer tipo de dado;
     - podemos misturar tipos de dados;


------------------------------------------------------------------------------------

# Criação de dicionários:

# Forma 1 (mais comums):
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ir': 'Ireland'}

print(paises)
print(type(paises))

# Forma 2 (menos comum):
paises = dict(br='Brasil', eua='Estados Unidos', ir='Ireland')
print(paises)
print(type(paises))

------------------------------------------------------------------------------------

# Acessando elementos

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ir': 'Ireland'}

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['ir'])
# print(paises['ru'])    # Caso fizermos uma indexação que com uma chave inexistente será retornado keyError

# Acessando via get - recomendado

print(paises.get('br'))
print(paises.get('ru'))  # Retorna tipo none

------------------------------------------------------------------------------------

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ir': 'Ireland'}

pais = paises.get('ru')

# Caso o get não encontre o objeto com a chave informada, será retornado o valor None
# e não será gerado KeyError

if pais:
    print(f'Encontrei o país {pais}.')
else:
    print(f'Não encontrei o páis.')

------------------------------------------------------------------------------------

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ir': 'Ireland'}

pais = paises.get('ru', 'Não encontrado')

# Podemos definir um valor padrão para caso não entremos o valor com a chave informada.

print(f'Encontrei o país {pais}.')


------------------------------------------------------------------------------------

# Podemos ferificar se determinada chave se encotnra em um dicionário

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ir': 'Ireland'}

print('br' in paises)
print('Estados Unidos' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

------------------------------------------------------------------------------------

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive
# listas, tupla dicioário, como chaves do dicionário.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))


------------------------------------------------------------------------------------

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))


# Forma 1 - mais comum:

receita['abr'] = 350

print(receita)


# Forma 2 :

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500})

print(receita)


# Forma 1 - mais comum:

receita['mai'] = 550

print(receita)

# Forma 2:

receita.update('mai': 600)
print(receita)

# CONCLUSÃO 1: A forma de adicionar nonvos elementos ou atualizar dados em um dicionário
# é a mesma.

# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

------------------------------------------------------------------------------------

# Remover dados de um dicionário:

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1:
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre nenhum elemento, um KeyError é retornado
# OBS 2: Ao remover um objeto, o valor deste objeto é sempre retornado.

# Forma 2:

del receita['fev']
print(receita)

# Se a chave não existir, será gerado keyError
# OBS: Neste caso o valor removido não é retornado

------------------------------------------------------------------------------------

# 1 - Proderíamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos Utilizar um tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'PS4', 'Quantidade': 1, 'Preço': 2300.00}
produto1 = {'nome': 'GOW', 'Quantidade': 1, 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removes produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

------------------------------------------------------------------------------------

# Métodos de dicionários:

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))


# Limpar o Dicionário (Zerar Dados)

d.clear()
print(d)


# Copiando um dicionário para outro:

# Forma 1:  # Deep Copy
novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)


# Froma 2:  # Shallow Copy

novo = d

print(novo)

novo['d']= 4

print(d)
print(novo)

------------------------------------------------------------------------------------

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método .fromkeys() recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do itrável, uma chave e irá atribuir a esta chave o
# valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

# Em dicionários python não remos repetição de chave.

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

------------------------------------------------------------------------------------
"""

"""
# Recebendo dados do usuário

input() -> //Todo dado recebido via input é tipo sting
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Jaca'
- Aspas duplas -> "Jaca"
- Aspas simples triplas -> '''Jaca'''
"""
# Aspas duplas triplas -> """Jaca"""

# print("Qual é o seu nome? ")
nome = input('Qual o seu nome? ')    # Input -> Entrada

# Exemplo de print antigo python 2.x
# print('seja bem vindo(a) %s' % nome)

# Ex de print a partir da versao python 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo da 'forma mais atual' python 3.9
print(f'Seja bem vindo(a) {nome}')


# print('Qual a sua idade? ')
idade = int(input('Qual a sua idade? '))

# Processamentos

# Saída de dados
# Exemplo de print antigo python 2.x
# print('A %s tem %s anos' % (nome, idade))

"""
# in(idade) => cast

Cast é a conversao de um tipo de dado para outro
"""
print(f'O {nome} nasceu em {2021 - idade}!')

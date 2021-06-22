"""
Tipo Float

Tipo real, decimal

Casas decimais

O separador das casas decimais é o ponto e nao a virgula.
"""

# Errado
valor = 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atrubuiçao
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros nós perdemos precisao.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j

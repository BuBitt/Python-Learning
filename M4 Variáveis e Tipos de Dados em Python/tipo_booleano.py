"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Flso

True -> Verdadeiro
False -> Falso

SEMPRE COM A INICIAL MAIÚSCULA

"""
ativo = False

print(ativo)

"""
Operaçoes Básicas
"""
# Negaçao (not):
"""
Fazendo a negaçao, se o valor booleano for verdadeiro o resultado será falado,
se for falso o resultado será verdadeiro, ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operaçao binária, ou seja, depende de dois valores.
Ou um ou outro é verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operaço binária, ou seja, depende de dois valores. Ambos os
valores devem ser Verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> True
"""

"""
Estruturas lógicas: and (e), or (ou), not (não), is (é).

Operadores unários (dependem de um valor):
    - not
Operadores binários (dependem de 2 valores):
    - and, or, is
________________________________________________________________________

Regras de Funcionamento:


- Para o "and", ambos os valores precisam ser True.

- para o "or", um ou outro valor precisa ser True.

- Para o "not", o valor do booleano é invertido, ou seja, se for True, vira
  False, se for False vira True.

- Para o "is", o valor pe comparado com um segundo valor.
"""
ativo = True
logado = True

# and
if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Pro favor, cheque seu e-mail.')

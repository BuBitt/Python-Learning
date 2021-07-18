"""
Teste de inputs e erros
"""

def teste(a,b):
    stop = 1
    while stop:
        try:
            stop = 0
            return int(a) * int(b)
        except ValueError:
            print('O valor digitado deve ser um número.')


a = input('Digite um número: ')
b = input('Digite um número: ')

print(teste(a, b))

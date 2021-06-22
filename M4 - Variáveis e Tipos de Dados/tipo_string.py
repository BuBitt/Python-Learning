"""
Tipo String

Em python um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'Uma String', '234', 'a', 'true', '42.3'
- Estiver entre aspas dupas -> "Uma String", "234", "a", "true", "42.3"
- EStiver entre aspas simples triplas -> '''Uma String''', '''234''', '''a''',
  '''true''', '''42.3'''
"""
# Estiver entre aspas dulpas triplas -> """Uma String""", """234""", """a""",
# """true""", """42.3"""

nome = 'jaca'
print(nome)
print(type(nome))

nome = "jaca"
print(nome)
print(type(nome))

nome = '''jaca'''
print(nome)
print(type(nome))

nome = """jaca"""
print(nome)
print(type(nome))

nome = "Jaca \" Norte"
print(nome)

nome = 'Jaca Norte'
print(nome.upper())

nome = 'JACA SUL'
print(nome.lower())

nome = 'Ualalau bb'
print(nome.split())

# Slice de string \ Começa no 0, com uma regra de -1 para a palavra final
# [ 0,   1,   2,   3,   4,   5,   6,   7 ]
# ['J', 'A', 'C', 'A', ' ', 'S', 'U', 'L']

nome = 'jaca sul'
print(nome[0:4])
print(nome[5:9])

# [   0,     1  ]
# ['jaca', 'sul']
print(nome.split()[0])
print(nome.split()[1])

nome = 'Jaca Central'
"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta
"""
# Inversao da string
print(nome[::-1])

print(nome.replace('a', 'C'))

texto = 'socorram me subino onibus em marrocos'  # Palindromo
print(texto)
print(texto[::-1])

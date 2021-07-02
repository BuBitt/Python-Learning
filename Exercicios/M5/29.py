"""
Faça uma prova de matemática para crianças que estão aprendendo a somar
números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde
a e b são números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno,
e mostre para ele as perguntas e as respostas corretas, além de quantas vezes
o aluno acertou.
"""
import random


print('\n---------------------Perguntas----------------------')
# Geração das perguntas:

quest_1_1 = random.randrange(1, 100)  # Pergunta 1
quest_1_2 = random.randrange(1, 100)
resp1 = int(input(f'\n1 - Qual o resultado da operação \
({quest_1_1} + {quest_1_2})? '))

quest_2_1 = random.randrange(1, 100)  # Pergunta 2
quest_2_2 = random.randrange(1, 100)
resp2 = int(input(f'2 - Qual o resultado da operação \
({quest_2_1} + {quest_2_2})? '))

quest_3_1 = random.randrange(1, 100)  # Pergunta 3
quest_3_2 = random.randrange(1, 100)
resp3 = int(input(f'3 - Qual o resultado da operação \
({quest_3_1} + {quest_3_2})? '))

quest_4_1 = random.randrange(1, 100)  # Pergunta 4
quest_4_2 = random.randrange(1, 100)
resp4 = int(input(f'4 - Qual o resultado da operação \
({quest_4_1} + {quest_4_2})? '))

quest_5_1 = random.randrange(1, 100)  # Pergunta 5
quest_5_2 = random.randrange(1, 100)
resp5 = int(input(f'5 - Qual o resultado da operação \
({quest_5_1} + {quest_5_2})? '))
print('\n-------------------Acertos/Erros--------------------')


# Verificação de erros:

# Referente a pergunta 1
if quest_1_1 + quest_1_2 == resp1:
    q1 = 1  # verificador de acerto
else:
    q1 = 0  # verificador de erro

# Referente a pergunta 2
if quest_2_1 + quest_2_2 == resp2:
    q2 = 1  # verificador de acerto
else:
    q2 = 0  # verificador de erro

# Referente a pergunta 3
if quest_3_1 + quest_3_2 == resp3:
    q3 = 1  # verificador de acerto
else:
    q3 = 0  # verificador de erro

# Referente a pergunta 4
if quest_4_1 + quest_4_2 == resp4:
    q4 = 1  # verificador de acerto
else:
    q4 = 0  # verificador de erro

# Referente a pergunta 5
if quest_5_1 + quest_5_2 == resp5:
    q5 = 1  # verificador de acerto
else:
    q5 = 0  # verificador de erro

print(f'''
\nVocê acertou: {q1+q2+q3+q4+q5} Questões.
Vocẽ errou: {5 - (q1+q2+q3+q4+q5)} Questões.
''')

print('\n---------------------Correção-----------------------\n')


# Exibindo Erros e acertos:

# Referente a pergunta 1
if quest_1_1 + quest_1_2 == resp1:
    print(f'\n1 - Você acertou a 1ª pergunta: \
{quest_1_1} + {quest_1_2} = {quest_1_1 + quest_1_2}.')
    q1 = 1  # verificador de acerto
else:
    print(f'1 - Você errou a 1ª pergunta: \
{quest_1_1} + {quest_1_2} = {quest_1_1 + quest_1_2}.')
    q1 = 0  # verificador de erro


# Referente a pergunta 2:
if quest_2_1 + quest_2_2 == resp2:
    print(f'2 - Você acertou a 2ª pergunta: \
{quest_2_1} + {quest_2_2} = {quest_2_1 + quest_2_2}.')
else:
    print(f'2 - Você errou a 2ª pergunta: \
{quest_2_1} + {quest_2_2} = {quest_2_1 + quest_2_2}.')


# Referente a pergunta 3:
if quest_3_1 + quest_3_2 == resp3:
    print(f'3 - Você acertou a 3ª pergunta: \
{quest_3_1} + {quest_3_2} = {quest_3_1 + quest_3_2}.')
else:
    print(f'3 - Você errou a 3ª pergunta: \
{quest_3_1} + {quest_3_2} = {quest_3_1 + quest_3_2}.')


# Referente a pergunta 4:
if quest_4_1 + quest_4_2 == resp4:
    print(f'4 - Você acertou a 4ª pergunta: \
{quest_4_1} + {quest_4_2} = {quest_4_1 + quest_4_2}.')
else:
    print(f'4 - Você errou a 4ª pergunta: \
{quest_4_1} + {quest_4_2} = {quest_4_1 + quest_4_2}.')


# Referente a pergunta 5:
if quest_5_1 + quest_5_2 == resp5:
    print(f'5 - Você acertou a 5ª pergunta: \
{quest_5_1} + {quest_5_2} = {quest_5_1 + quest_5_2}.')
else:
    print(f'5 - Você errou a 5ª pergunta: \
{quest_5_1} + {quest_5_2} = {quest_5_1 + quest_5_2}.\n')

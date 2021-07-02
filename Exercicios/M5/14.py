"""
A nota final de um estudante é calculada a partir de três notas atribuídas
entre o interavalo de 0 a 10, respectivamente, a um trabalho de laboratório,
a uma avaliação semestral e a um exame final. A média das três notas mencionada
anteriormente obedece aos pesos:

    - Trabalho de laboratório: 2;
    - Avaliação semestral: 3;
    - Exame final: 5.

De acordo com o resultado, mostre na tela se o aluno está reprovado
(média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado.
faça todas as verificações necessárias.
"""
nota1 = float(input('Digite a nota de Trabalho de Laboratório (0 a 10): '))
nota2 = float(input('Digite a nota da Avaliação Semetral (0 a 10): '))
nota3 = float(input('Digite a nota do Exame Final (0 a 10): '))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

if media >= 5:
    print(f'O aluno foi aprovado com a nota {media}')
elif media >= 3 and media <= 4.9:
    print(f'O aluno está de recuperação com a nota {media}')
else:
    print(f'O aluno foi reprovado com a nota {media}')

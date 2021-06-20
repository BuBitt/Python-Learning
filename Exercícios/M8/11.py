"""
Elabore uma função que receba três notas de um aluno como parâmetro e uma letra.
Se a letra for A, a função deverá calcular a média aritmética das notas do aluno;
Se for P, deverá calcular a média ponderada com pesos 5, 3, 2.
"""


def media(nota_1, nota_2, nota_3, letra):
    if letra == 'A':
        return (nota_1 + nota_2 + nota_3) / 2
    elif letra == 'P':
        return (nota_1 * 5 + nota_2 * 3 + nota_3 * 2) / 10
    return f"A letra {letra} é inválida."


print(media(10, 10, 10, 'A'))
print(media(10, 10, 10, 'P'))
print(media(10, 10, 10, 'B'))

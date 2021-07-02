"""
Crie um programa que receba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:

    (a) Determinar se eles formam um triângulo, sabendo que:
        - O comprimento de cada lado de um triângulo é menor do que a soma dos outros
          dois lados.
    
    (b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo.
        Sabendo que:
        
        - Chama-se equilatero o triângulo que tem 3 lados iguais;
        - Denominam-se isósceles o triângulo que tem o comprimento de dois lados
            iguais;
        - Recebe o nome de escaleno o triângulo que tem 3 lados diferentes.
"""
a = 10
b = 10
c = 15


def check_triangulo(lado_a, lado_b, lado_c):
    if lado_a < lado_b + lado_c:
        return True

    elif lado_b < lado_a + lado_c:
        return True

    elif lado_c < lado_b + lado_a:
        return True

    return False


def tipo_de_triangulo(lado_a, lado_b, lado_c):
    check_a = False
    check_b = False
    check_c = False

    # Checagem de triângulo isósceles:
    if lado_a == lado_b and lado_b != lado_c or lado_a == lado_c and lado_b != lado_c:
        check_a = True

    elif lado_c == lado_b and lado_b != lado_a or lado_c == lado_a and lado_b != lado_a:
        check_b = True

    elif lado_c == lado_a and lado_b != lado_a:
        check_c = True

    # Retorno da função:
    if lado_a == lado_c == lado_b:
        return '\nEste triângulo é equilátero'

    elif check_a or check_b or check_c:
        return '\nEste triângulo é isósceles.'

    return '\nEste triângulo é escaleno.'


if check_triangulo(a, b, c):
    print(tipo_de_triangulo(a, b, c))
else:
    print('Não é um triângulo.')

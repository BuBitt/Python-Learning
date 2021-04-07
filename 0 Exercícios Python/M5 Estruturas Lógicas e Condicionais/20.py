"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de
um triângulo e, se é um escaleno, equilátero ou isoceles, considerando os
seguintes conceitos:

    - O comprimento de cada lado de um triângulo é menor do que a soma
      dos outros dois lados;
    - Cahama-se equilátero o triângulo que tem três lados iguais;
    - Denominam-se isóceles o triângulo que tem o comprimento dois lado iguais;
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
print('Digite o valor de cada lado a seguir:\n')
a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('\nÉ um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('\nÉ um triângulo isóceles.')
    else:
        print('\nÉ um triângulo escaleno.')
else:
    print('\nOs lados não formam um triângulo')

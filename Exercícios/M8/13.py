"""
Faça uma função que receba dois valores numéricos e um símbolo. Este simbolo representará
a operação que se deseja efetuar com os números. Se o símbolo for + deverá somar, se for
-, sbtrair, se for * , multiplicar e se for /, dividir.
"""


def calculadora(numero_1, numero_2, simbolo):
    if simbolo == '+':
        return numero_1 + numero_2
    
    elif simbolo == '-':
        return numero_1 - numero_2

    elif simbolo == '*':
        return numero_1 * numero_2

    elif simbolo == '/':
        return numero_1 / numero_2


print(calculadora(40, 50 , '+'))
print(calculadora(40, 50 , '-'))
print(calculadora(40, 50 , '*'))
print(calculadora(40, 50 , '/'))

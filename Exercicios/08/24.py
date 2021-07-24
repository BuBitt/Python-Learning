"""
Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por Exemplo, a
saída para n=6 seria:

                                         *
                                        ***
                                       *****
                                      *******
                                     *********
                                    ***********
"""
def gera_triangulo(n=6):
    for colum in range(1, n+1):

        line = colum * 2 -1
        print((n - colum) * " ", end="")
        print("*"*line, end="")

        print()


n = int(input("Digite um número: "))
gera_triangulo(n)

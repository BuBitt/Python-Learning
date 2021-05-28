def criar_matriz(matriz, ordem):
    for i in range(ordem):
        matriz.append([0] * ordem)


def ler_matriz(matriz, ordem):
    for i in range(ordem):
        for j in range(ordem):
            print('Elemento [', i + 1, '][', j + 1, ']: ', sep='', end='')
            matriz[i][j] = int(input())


def imprimir_matriz(matriz, ordem):
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end=' ')
        print()


def soma_linhas(matriz, ordem, somaLinhaFrente, somaLinhaAnterior, count, ligar):
    somaGL = 0
    for i in range(ordem):
        for j in range(ordem):
            if i == count:
                somaLinhaFrente = somaLinhaFrente + matriz[i][j]
        if ligar:
            somaLinhaAnterior = somaLinhaFrente
            ligar = False
        if somaLinhaFrente != somaLinhaAnterior:
            return False
        count = count + 1
        somaLinhaAnterior = somaLinhaFrente
        somaLinhaFrente = 0
    somaGL = somaLinhaAnterior
    return somaGL


def soma_colunas(matriz, ordem, somaColunaFrente, somaColunaAnterior, count, ligar, stop):
    somaGC = 0
    while stop != 0:
        for i in range(ordem):
            for j in range(ordem):
                if j == count:
                    somaColunaFrente = somaColunaFrente + matriz[i][j]
        if ligar:
            somaColunaAnterior = somaColunaFrente
            ligar = False
        if somaColunaFrente != somaColunaAnterior:
            return False
        count = count + 1
        somaColunaAnterior = somaColunaFrente
        somaColunaFrente = 0
        stop = stop - 1
    somaGC = somaColunaAnterior
    return somaGC


def soma_diagonal(matriz, ordem, somaDiagonalPrincipal, somaDiagonalSecundaria):
    somaGD = 0
    for i in range(ordem):
        for j in range(ordem):
            if i == j:
                somaDiagonalPrincipal = somaDiagonalPrincipal + matriz[i][j]
    for i in range(ordem):
        for j in range(ordem):
            if i + j == ordem - 1:
                somaDiagonalSecundaria = somaDiagonalSecundaria + matriz[i][j]
    if somaDiagonalPrincipal != somaDiagonalSecundaria:
        return False
    somaGD = somaDiagonalPrincipal
    return somaGD


mat = []
soma = 0
aux = True
ordem_n = int(input('Digite a ordem N da matriz: '))
aux = ordem_n
print()
criar_matriz(mat, ordem_n)
ler_matriz(mat, ordem_n)
print()
imprimir_matriz(mat, ordem_n)
somaL = soma_linhas(mat, ordem_n, soma, soma, soma, aux)
somaC = soma_colunas(mat, ordem_n, soma, soma, soma, aux, ordem_n)
somaD = soma_diagonal(mat, ordem_n, soma, soma)
if not somaL:
    print()
    print('A matriz digitada não é um quadrado mágico.')
elif not somaC:
    print()
    print('A matriz digitada não é um quadrado mágico.')
elif not somaD:
    print()
    print('A matriz digitada não é um quadrado mágico.')
else:
    print()
    print('A matriz digitada é um quadrado mágico.')

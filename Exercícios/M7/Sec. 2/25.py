"""
Faça um programa para determinar a próxima jogada em um jogo da velha. assumir que o
tabuleiro é representado por uma matriz de 3x3, onde cada posição representa uma das
casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1 representando
respectivamente uma casa contendo uma peça minha (-1), uma casa vazia do tabuleiro (0),
e uma casa contendo uma peça do meu oponente(1).

Exemplo:

                                        -1 | 1 | 1
                                        ----------
                                        -1 |-1 | 0
                                        ----------
                                         0 | 1 | 0
"""
m = []
c = 0
jv = [
    [-1, 1, -1],
    [-1, -1, 1],
    [0, 1, 1],
]


# !Construção do jogo da velha:
print()
for i in range(3):
    for j in range(3):
        if jv[i][j] == 1:
            jv[i][j] = " 1"

        elif jv[i][j] == 0:
            jv[i][j] = " 0"

        print(jv[i][j], end=" ")

        if j < 2:
            print("|", end="")

    print("\n-----------", end="")
    print()
print()

# *Traduzindo a string para int:
for i in range(3):
    for j in range(3):
        if jv[i][j] == " 1":
            jv[i][j] = 1

        elif jv[i][j] == " 0":
            jv[i][j] = 0


# !Verificação das linhas:
for i in range(3):
    vef = 0

    for j in range(3):
        vef += jv[i][j]

        if vef == -2:
            if jv[i][j] == 0:
                m.append((i + 1, j + 1))
                c = 1
                break


# !Verificação das colunas:
if c == 0:
    for i in range(3):
        vef = 0

        for j in range(3):
            vef += jv[j][i]

            if vef == -2:
                if jv[j][i] == 0:
                    m.append((j + 1, i + 1))
                    c = 1
                    break


# !Verificação da diagonal principal:
if c == 0:
    vef = 0
    for i in range(3):
        vef += jv[i][i]

        if vef == -2:
            if jv[i][i] == 0:
                m.append((i + 1, i + 1))
                c = 1
                break


# !Verificação da diagonal secundária:
if c == 0:
    vef = 0
    jv = jv[::-1]
    for i in range(3):
        vef += jv[i][i]

        if vef == -2:
            if jv[i][i] == 0:
                m.append((i + 1, i + 1))
                c = 1
                break


print(f"Sua jogada deve ser na linha {m[0][0]}, com a coluna {m[0][1]}.")

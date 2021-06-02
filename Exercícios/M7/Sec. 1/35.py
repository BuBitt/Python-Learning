"""
Faça um programa que leia dois números a e b (positivos menores que 10000) e:

    1 - Crie um vetor onde cada posição é um algarismo do número. A Primeira posição é
        o algarismo menos significativo.

    2 - Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores
        construídos anteriormente.

    Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do
          resultado e some 1 a próxima posição
"""
from random import randrange


a = randrange(10000)
b = randrange(10000)
ad = ''


a = str(a)
b = str(b)
a = a[::-1]
b = b[::-1]


la = list(a)
lb = list(b)
lf = []


for i in range(len(la)):
    la[i] = int(la[i])


for i in range(len(lb)):
    lb[i] = int(lb[i])
print(la[::-1], '<- Vetor A')
print(lb[::-1], '<- Vetor B')


if len(la) < len(lb):
    vali = len(la)
else:
    vali = len(lb)


for i in range(vali):
    lf.append(la[i] + lb[i])

    if len(la) != len(lb):
        if len(la) < len(lb):
            vef = len(lb) - len(la)

        else:
            vef = len(la) - len(lb)

    if i == vali - 1:
        if len(la) < len(lb):
            for t in range(vef):
                lf.append(lb[t + 1 + i])

        elif len(lb) < len(la):
            for t in range(vef):
                lf.append(la[t + 1 + i])


if lf[3] >= 10:
    lf.append(0)


for i in range(len(lf)):
    if lf[i] >= 10:
        lf[i] -= 10

        if i == len(lf) - 1:
            break
        else:
            lf[i + 1] += 1


lf = lf[::-1]


for i in range(len(lf)):
    lf[i] = str(lf[i])
    ad += lf[i]

ad = int(ad)
print(lf, '<- Vetor Resultante')
print(ad, '<- Resposta final inteira')

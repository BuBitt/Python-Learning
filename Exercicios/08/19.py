"""
Faça uma função que retorne o maior fator primo de um número.
"""


def gerador_de_fatores(numero):
    fatores = []
    turno = 1

    while True:
        turno += 1

        while True:
            resultado = numero / turno

            if numero % turno == 0:
                numero = resultado
                fatores.append(turno)

            elif numero % turno != 0:
                break

        if numero == 1:
            break
    return fatores


def remover_repeticoes(lista):
    lista = set(lista)
    lista = list(lista)
    lista.sort()
    return lista


def check_prime_lista(lista):
    maior_fator_primo = 0
    remover_repeticoes(lista)

    for _, fator in enumerate(lista):
        for turno in range(2, fator + 1):

            if fator % turno == 0 and fator != turno:
                break

            elif fator == turno:
                if fator > maior_fator_primo:
                    maior_fator_primo = fator
    return maior_fator_primo


num = int(input('Digite um número: '))
print(gerador_de_fatores(num))
print(remover_repeticoes(gerador_de_fatores(num)))
print(check_prime_lista(gerador_de_fatores(num)))

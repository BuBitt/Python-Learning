"""
Faça um programa para ler 10 números DIFERENTES a serem armazenados em um
vetor. Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos,
sendo que caso o usuário digite outro número que já foi digitado anteriormente,
o programa deverá pedir para ele digitar outro número. Note que cada valor digitado
pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre os
números que já foram fornecidos. Exibir na tela o vetor final que foi digitado.
"""
v = []
aux = True


while len(v) < 10:
    adc = int(input('Digite um número: '))
    print(len(v))

    if adc in v:
        while aux:
            adc = int(input('Número já exitente no vetor, digite outro número: '))

            if adc in v:
                aux = aux

            else:
                v.append(adc)
                break

    else:
        v.append(adc)
print(v)

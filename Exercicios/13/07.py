import os


def subs(path, arq_entrada, arq_saida):
    os.chdir(path)
    with open(arq_entrada) as arq_e:
        vogais = 'aeiouAEIOU'
        final = [arq_e.read()]

        for vogal in vogais:
            final[0] = final[0].replace(vogal, '*')

        with open(arq_saida, '+w') as arq_s:
            arq_s.write(final[0])
            print(arq_s.read())


subs('arquivos', 'arq.txt', 'arq_s.txt')
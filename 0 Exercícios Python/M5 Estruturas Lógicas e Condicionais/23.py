"""
Determine se um determinado ano lido é bissexto. Sendo qum ano é bissexto
se for divisível por 4 e não for divisível por 100. por exemplo:
1988, 1992, 1996.
"""
ano = int(input('Digite o ano de verificação: '))

if (ano % 4) == 0 and (ano % 100) != 0:
    print(f'\n{ano} é bissexto.')
else:
    print(f'\n{ano} não é bissexto.')

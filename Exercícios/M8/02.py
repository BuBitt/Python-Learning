"""
Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba na tela
no formato textual por extenso. Exemplo: 01/01/2000, imprimir: 1 de janeiro de 2000.
"""
data = str(input('Digite uma data DD/MM/AAAA: '))

def conv_data(date):
    dia = int(date[0:2])
    ano = int(date[6:10])
    mes = 0
    
    if date[3:5] == '01':
        mes = 'Janeiro'
    
    elif date[3:5] == '02':
        mes = 'Fevereiro'
    
    elif date[3:5] == '03':
        mes = 'Março'
    
    elif date[3:5] == '04':
        mes = 'Abril'
    
    elif date[3:5] == '05':
        mes = 'Maio'
    
    elif date[3:5] == '06':
        mes = 'Junho'
    
    elif date[3:5] == '07':
        mes = 'Julho'
    
    elif date[3:5] == '08':
        mes = 'Agosto'
    
    elif date[3:5] == '09':
        mes = 'Setembro'
    
    elif date[3:5] == '10':
        mes = 'Outubro'
    
    elif date[3:5] == '11':
        mes = 'novembro'
    
    elif date[3:5] == '12':
        mes = 'Dezembro'
                    
    return print(f'\n{dia} de {mes} de {ano}')

conv_data(data)

"""
Leia o salário de um trabalhador e o valor da prestação de um emprestimo
se a prestação for maior que 20% do salário imprima: Empréstimo não concedido
caso contrário: Emprestimo concedido.
"""
salario = float(input('Digite o valor do salário: '))
valemp = float(input('Digite o valor do empréstimo: '))

if valemp > (salario * 0.20):
    print('Empréstimo não concedido.')
else:
    print('Emprestimo concedido.')

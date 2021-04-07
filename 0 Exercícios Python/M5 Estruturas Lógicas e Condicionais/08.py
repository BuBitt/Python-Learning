"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas
são válidas e exiba a tela a média destas notas uma nota válida deve ser
obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua
um valor válido, este faro deve ser informado ao usuário e o programa termina.
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    print((nota1 + nota2) / 2)
else:
    print('As notas digitadas não são válidas')

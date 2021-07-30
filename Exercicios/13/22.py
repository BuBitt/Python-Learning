"""
Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome
de um arquivo de saída. O arquivo de entrada contém o nome de mu aluno ocupando 40
caracteres e três inteiros que indicam suas notas. O programa deverá ler o arquivo
de entrar e gerar um arquivo de saída onde aparece o nome do aluno e as suas notas
em ordem crescente.
"""
import os


def ordena_notas(path_in, path_out):
	with open(os.path.join(path_in + '.txt')) as arq:
		lines = [line.split(',') for line in arq.readlines().copy()]

		for i, v in enumerate(lines):
			name = v[0]
			nums = v[1]
			nums = nums.split(' ')
			nums = [int(num) for num in nums]
			nums.sort()
			with open(path_out + '.txt', 'w') as arq_out:
				line = '.' * (40 - len(name) - 1)
				arq_out.write(f'{name} {line}{[num for num in nums]}')

	print("Operação Realizada")


ordena_notas('22in', '22out')

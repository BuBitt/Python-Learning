with open('23out.txt', 'w') as arq:
	for i in range(5):
		name = input('Nome do funcionário: ')
		anos = int(input('Anos de serviço: '))
		arq.write(f'NOME: {name}, ANOS DE SERVIÇO: {anos}\n')

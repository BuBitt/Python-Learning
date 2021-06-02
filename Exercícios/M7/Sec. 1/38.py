"""
Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses
valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao
final na tela os valores em ordem.
"""
v = []


for i in range(10):
    inp = float(int(input("\nDigite um número: ")))
    v.append(inp)
    v.sort()
    print(v)

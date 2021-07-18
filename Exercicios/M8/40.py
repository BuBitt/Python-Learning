v = [1 ,2 , 3, 4, 5, 6, 7, 8, 9 , 10, 12]

def conta(vetor):
    qte = 0
    for _, v in enumerate(vetor):
        if v % 2 == 0:
            qte += 1

    return qte

print(conta(v))

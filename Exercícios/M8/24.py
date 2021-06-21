
def gera_f_quadratica(a=0, b=0, c=0):
    return lambda x: a * x ** 2 + b * x + c


r = gera_f_quadratica(-10, 20, 10)


[print('.' * abs(round(r(i) / 50)), round(r(i))) for i in range(20)]


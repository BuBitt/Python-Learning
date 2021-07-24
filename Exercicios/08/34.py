def fatorial_duplo(x):
    d_fact = x

    for i in range(2, x, 2):
        d_fact *= x - i

    return d_fact


print(fatorial_duplo(5))

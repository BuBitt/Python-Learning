def fatorial(x):
    fatorial = 1

    for i in range(2, x + 1):
        fatorial *= i

    return fatorial


def superfatorial(x):
    s_fatorial = 1

    for i in range(2, x + 1):
        s_fatorial *= fatorial(i)

    return s_fatorial


print(superfatorial(4))

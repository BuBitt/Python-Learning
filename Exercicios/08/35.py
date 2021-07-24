def q_fac(x):
    fact = 1
    qq_fact = 1

    for i in range(2, x + 1):
        fact *= i

    for i in range(2, x * 2 + 1):
        qq_fact *= i

    return qq_fact / fact


print(q_fac(23))

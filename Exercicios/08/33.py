def sum_alg(x):
    fac = 1
    som = 0

    for i in range(2, x + 1):
        fac *= i

    s_fac = list(str(fac))

    for _, v in enumerate(s_fac):
        som += int(v)

    return som


print(sum_alg(4))

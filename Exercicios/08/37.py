def hiperfatorial(x):
    h_fatorial = 1

    for i in range(1, x + 1):
        print(i)
        h_fatorial *= i ** i
    return h_fatorial


print(hiperfatorial(4))

"""
38. Faça um programa que calcule o termo pitagórico a, b, c, para o qual a + b + c = 1000. Um
    terno pitagórico é um conjunto de três números naturais, a, b, c, para a qual,

                                           a² + b² = c²

    Por exemplo,

                                    3² + 4² = 9 + 16 = 25 = 5²
"""
for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if a + b + c == 1000:
                if a ** 2 + b ** 2 == c ** 2:
                    print(a, b, c)

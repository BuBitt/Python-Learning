import os


def get_prices(path):
    with open(path) as pri:
        prices = [price.replace('\n', '') for price in pri.readlines()]
        soma = 0
        for i in range(1, len(prices), 2):
            soma += int(prices[i])

        return soma


print(get_prices('18in.txt'))

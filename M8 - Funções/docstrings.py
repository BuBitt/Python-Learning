"""
Documentando funções com docstrings
"""
# Exemplos
def diz_oi():
    """Uma função simples que diz 'oi'!"""
    print('Oi')
print()

print(diz_oi.__doc__)
print(help(diz_oi))


def exp(n, p=2):
    """Função que retona por padrão o quadrade de um 'número' ou 'numero' a 'potência' informada.

    Args:
        n (int): O número a ser elevado a determinada 'potência"
        p (int, optional): O valor da potência. O número padrão é 2.
    """

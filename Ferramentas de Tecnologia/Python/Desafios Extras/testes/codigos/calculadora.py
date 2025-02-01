"""
Módulo para operações matemáticas simples.

Este módulo contém funções para soma e subtração de dois números,
incluindo testes embutidos com doctest.
"""


def soma(x, y):
    """
    Retorna a soma de x e y.

    >>> soma(10, 15)
    25

    >>> soma(-10, 5)
    -5

    >>> soma('300', 200)
    Traceback (most recent call last):
    AssertionError: X precisa ser int ou float

    >>> soma(300, '200')
    Traceback (most recent call last):
    AssertionError: Y precisa ser int ou float

    :param x: Primeiro número a ser somado (int ou float).
    :param y: Segundo número a ser somado (int ou float).
    :return: Resultado da soma de x e y.
    """
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x + y


def subtrair(x, y):
    """
    Retorna a subtração de x e y.

    >>> subtrair(30, 15)
    15

    >>> subtrair(10, 5)
    5

    >>> subtrair('300', 200)
    Traceback (most recent call last):
    AssertionError: X precisa ser int ou float

    >>> subtrair(300, '200')
    Traceback (most recent call last):
    AssertionError: Y precisa ser int ou float

    :param x: Número do qual será subtraído (int ou float).
    :param y: Número a ser subtraído de x (int ou float).
    :return: Resultado da subtração de x por y.
    """
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x - y


if __name__ == "__main__":
    import doctest

    # Executa os testes definidos nas docstrings ao rodar o script diretamente
    doctest.testmod(verbose=True)

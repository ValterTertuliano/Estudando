"""
Função bacon_com_ovos

Esta função recebe um número inteiro e retorna uma string com base nas regras:

1 - Se for múltiplo de 3 e 5, retorna "bacon com ovos".
2 - Se for apenas múltiplo de 3, retorna "bacon".
3 - Se for apenas múltiplo de 5, retorna "ovos".
4 - Se não for múltiplo de 3 nem de 5, retorna "fome".
"""


def bacon_com_ovos(n: int) -> str:
    """
    Retorna uma string baseada na divisibilidade de um número por 3 e/ou 5.

    :param n: Número inteiro a ser verificado.
    :return: Uma string com a classificação do número.
    """

    # Verifica se a entrada é um número inteiro, lançando um erro se não for.
    assert isinstance(n, int), "n deve ser int"

    # Verifica se o número é múltiplo de 3 e 5 ao mesmo tempo.
    if (n % 3 == 0) and (n % 5 == 0):
        return "bacon com ovos"

    # Verifica se o número é múltiplo de 3.
    if n % 3 == 0:
        return "bacon"

    # Verifica se o número é múltiplo de 5.
    if n % 5 == 0:
        return "ovos"

    # Caso o número não seja múltiplo de 3 nem de 5, retorna "fome".
    return "fome"

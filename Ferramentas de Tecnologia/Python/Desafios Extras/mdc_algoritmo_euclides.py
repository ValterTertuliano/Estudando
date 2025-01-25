def calcular_mdc(x: int, y: int):
    """
    Essa função usa o algoritmo de Euclides para encontrar o MAXIMO DIVISOR COMUM entre X e Y
    Args:
    x : valor inteiro
    y : valor inteiro

    Return:
    x : O valor do MDC entre X e Y
    """
    while (y != 0):
        resto = x % y # resto da divisão
        x = y # o valor do MDC está aqui
        y = resto
    return x

print(f'O MDC é {calcular_mdc(10, 15)}')
print(f'O MDC é {calcular_mdc(20, 15)}')
print(f'O MDC é {calcular_mdc(30, 15)}')
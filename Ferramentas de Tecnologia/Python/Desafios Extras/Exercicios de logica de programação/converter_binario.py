def converter_para_binario(n: int) -> str:
    """
    Converte um número inteiro decimal para sua representação binária.

    Parâmetros:
        n (int): O número inteiro a ser convertido.

    Retorna:
        str: O número binário equivalente representado como uma str.
    """

    if not n:
        return '0'
    
    # Lista para armazenar os restos da divisão, que formarão o número binário.
    resultado1 = []

    # Loop para realizar a conversão enquanto n for maior ou igual a 1.
    while n >= 1:
        # Calcula o resto da divisão por 2 (dígito binário).
        resto = n % 2

        # Atualiza n para a parte inteira da divisão por 2.
        inteiro = n // 2
        n = inteiro

        # Adiciona o resto à lista (como string para posterior junção).
        resultado1.append(str(resto))

    # Inverte a lista e junta os elementos para formar o número binário.
    resultado = ''.join(list(reversed(resultado1)))

    # Retorna o valor convertido para inteiro.
    return resultado


# Exemplo de uso: converte o número 25 para binário.
print(converter_para_binario(25))
print(converter_para_binario(252))
print(converter_para_binario(22))

def fizzbuzz(n):
    """
    Retorna 'Fizz' se o número for múltiplo de 3,
    'Buzz' se for múltiplo de 5,
    'FizzBuzz' se for múltiplo de ambos (3 e 5),
    ou o próprio número caso contrário.

    Parâmetros:
    n (int): O número a ser verificado.

    Retorna:
    str ou int: 'Fizz', 'Buzz', 'FizzBuzz' ou o próprio número.
    """
    
    # Verifica se o número é múltiplo de 3
    tres = n % 3 == 0
    # Verifica se o número é múltiplo de 5
    cinco = n % 5 == 0
    
    # Retorna 'Fizz' se for múltiplo de 3, mas não de 5
    if tres and not cinco:
        return "Fizz"
    
    # Retorna 'Buzz' se for múltiplo de 5, mas não de 3
    if cinco and not tres:
        return "Buzz"
    
    # Retorna 'FizzBuzz' se for múltiplo de 3 e 5 ao mesmo tempo
    if tres and cinco:
        return "FizzBuzz"
    
    # Retorna o próprio número caso não seja múltiplo de 3 nem de 5
    return n

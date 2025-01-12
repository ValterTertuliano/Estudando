# link do desafio -> https://www.youtube.com/watch?v=iFvnOEPNPSk&list=PLLgKYjEKBqxcIeoikzTNZJtmxjW8eYLM2&index=6

from math import sqrt

def equacao_segundo_grau(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' deve ser diferente de zero.")
    
    delta = (b**2) - 4 * a * c
    
    if delta < 0:
        # Para raízes complexas
        raise ValueError("O delta é negativo, a equação tem raízes complexas.")
    
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    
    return x1, x2

if __name__ == "__main__":
    
    a = 2
    b = -4
    c = -6
    x1, x2 = equacao_segundo_grau(a, b, c)

    print("X1: ", x1)
    print("X2: ", x2)
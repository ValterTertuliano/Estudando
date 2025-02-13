# link do desafio -> https://www.youtube.com/watch?v=doKyvCGztvA&list=PLLgKYjEKBqxcIeoikzTNZJtmxjW8eYLM2&index=3

# Função para desenhar o triângulo retângulo
def desenha_triangulo(base):
    
    for i in range(base):
        print('* ' * (i+1))

# Função para desenhar o quadrado
def desenha_quadrado(base):
    for _ in range(base):
        print('* '*base)
if __name__ == "__main__":
    desenha_quadrado(5)
    print()
    desenha_triangulo(5)

    del desenha_quadrado
    del desenha_triangulo
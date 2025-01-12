# link do desafio -> https://www.youtube.com/watch?v=6hapSDg8Wns&list=PLLgKYjEKBqxcIeoikzTNZJtmxjW8eYLM2&index=5 

def somar_matrizes(matriz1, matriz2):
    tamanho_matriz1 = len(matriz1)
    tamanho_matriz2 = len(matriz2)

    maior_tamanho = tamanho_matriz1 if tamanho_matriz1 >= tamanho_matriz2 else tamanho_matriz2

    nova_matriz = []
    for x in range(maior_tamanho):
        
        # so´vai dar erro caso uma matrix seja maior que a outra, nesse caso um dos objetos recebe 0, mantendo a matriz equilibrada
        try:
            matrix_1 = matriz1[x]
        except:
            matrix_1 = 0
        
        try:
            matrix = matriz2[x]
        except:
            matrix = 0

        somar_matrizes = matrix_1 + matrix
        nova_matriz.append(somar_matrizes)
    
    return nova_matriz

if __name__ == "__main__":
    
    # crie uma função que soma duas matrizes
    matriz1 = [x+1 for x in range(20)]
    matriz2 = [x+1 for x in range(20)]

    nova_matrix = (somar_matrizes(matriz1, matriz2))
    print(nova_matrix, 'n: ', len(nova_matrix))
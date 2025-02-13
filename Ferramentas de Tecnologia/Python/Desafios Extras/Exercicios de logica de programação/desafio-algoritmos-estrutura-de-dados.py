# Problema 2: Ordenando uma matriz de inteiros
# Implemente uma função que receba uma matriz 2D de inteiros 
# (lista de listas) e retorne uma nova matriz onde cada linha 
# esteja ordenada em ordem crescente.

matriz = [
    [34, 12, 5],
    [99, 45, 2],
    [7, 3, 18]
]

# Escreva sua solução aqui
matriz2 = [sorted(x) for x in matriz]

# exibindo matriz ordenada
print(matriz2)


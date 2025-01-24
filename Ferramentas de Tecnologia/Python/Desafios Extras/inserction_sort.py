# Lista inicial com números em ordem decrescente (desordenada)
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Descobrimos o tamanho da lista para usar no loop
n = len(lista)

# Começamos do segundo número (índice 1), já que o primeiro número (índice 0) está "ordenado por padrão"
for x in range(1, n):
    
    # Guardamos o número atual que vamos colocar no lugar certo
    chave = lista[x]
    
    # Pegamos o índice do número anterior ao atual
    i = x - 1
    
    # Esse loop verifica se o número da esquerda é maior que o atual (a chave)
    while i >= 0 and lista[i] > chave:
        # Se for maior, movemos o número para a direita, abrindo espaço para a chave
        lista[i + 1] = lista[i]
        
        # Passamos para o próximo número à esquerda
        i -= 1
    
    # Quando saímos do loop, colocamos o número atual (a chave) no lugar correto
    lista[i + 1] = chave

# No final do loop principal, todos os números estarão ordenados
print(lista)

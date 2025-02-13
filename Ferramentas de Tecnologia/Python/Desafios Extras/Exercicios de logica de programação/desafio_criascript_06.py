# link do desafio - https://www.youtube.com/watch?v=oBEZiQaRZao&list=PLLgKYjEKBqxcIeoikzTNZJtmxjW8eYLM2&index=2

# cria uma função que recebe uma lista de dicionarios de produtos, valor minimo e valor maximo e que retorna a lista de dicionarios com os produtos filtrados 

def filtrar_produtos(lista_de_produtos: list, valor_minimo: float, valor_maximo: float) -> list:
    lista_filtrada = []
    for produto in lista_de_produtos:
        for nome_produto, preco_produto in produto.items():
            if  (preco_produto >= valor_minimo and preco_produto <= valor_maximo):

                lista_filtrada.append({nome_produto: preco_produto})
    
    return lista_filtrada

if __name__ == "__main__":
    lista_de_produtos = [
        {'produto1': 5},
        {'produto2': 4},
        {'produto3': 3},
        {'produto4': 2},
        {'produto5': 1},
    ]

    valor_minimo = 1
    valor_maximo = 3

    print(filtrar_produtos(lista_de_produtos, valor_minimo, valor_maximo))

    del lista_de_produtos
    del valor_maximo
    del valor_minimo
    del filtrar_produtos
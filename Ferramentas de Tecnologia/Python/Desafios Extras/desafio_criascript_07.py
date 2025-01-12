# link desafio -> https://www.youtube.com/watch?v=0bX4oDGbJxE&list=PLLgKYjEKBqxcIeoikzTNZJtmxjW8eYLM2&index=1

def calcular_media_alunos(lista_de_dicionarios, nota_de_aprovacao):
    """
    Calcula a média das notas de cada aluno, determina se o aluno foi aprovado
    com base em uma nota mínima de aprovação e atualiza os dados dos alunos.

    Parâmetros:
    lista_de_dicionarios (list): Lista de dicionários, onde cada dicionário contém o nome do aluno
                                 como chave e uma lista de suas notas como valor.
    nota_de_aprovacao (float): A nota mínima para um aluno ser aprovado.

    Retorna:
    list: A lista de dicionários atualizada com as notas, média e status de aprovação.
    """
    for dicionario in lista_de_dicionarios:
        # Itera sobre os alunos do dicionário
        for aluno in dicionario:
            lista_de_notas = dicionario[aluno]
            
            # Obtém o tamanho da lista de notas (quantidade de notas)
            tamanho = len(lista_de_notas)

            # Soma todas as notas do aluno
            somar_notas = sum(lista_de_notas)

            # Calcula a média das notas
            media_das_notas = somar_notas / tamanho

            # Determina se o aluno foi aprovado, com base na nota mínima
            aprovado = media_das_notas > nota_de_aprovacao

            # Atualiza o dicionário do aluno com as informações de notas, média e aprovação
            dicionario[aluno] = {'Notas': lista_de_notas, "Média": media_das_notas, "Aprovado": aprovado}

            # Exibe o resultado de aprovação ou reprovação do aluno
            if aprovado:
                print(aluno, ' Aprovado: ', "Média: ", media_das_notas)
            else:
                print(aluno, ' Reprovado: ', "Média: ", media_das_notas)

    # Retorna a lista de dicionários atualizada com as informações dos alunos
    return lista_de_dicionarios

if __name__ == "__main__":
    # Exemplo de dados de alunos com suas notas
    lista_de_dicionarios = [
        {'estudante1': [3, 3, 3]},
        {'estudante2': [4, 4, 4, 4]},
        {'estudante3': [5, 5, 5, 5, 5]},
        {'estudante4': [6, 6, 6, 6, 6, 6]},
        {'estudante5': [7, 7, 7, 7, 7, 7, 7]},
        {'bugs': [x for x in range(1_000_000)]}
    ]

    # Chama a função para calcular a média e exibir o resultado
    l = calcular_media_alunos(lista_de_dicionarios, nota_de_aprovacao=6)
    del l
    del lista_de_dicionarios
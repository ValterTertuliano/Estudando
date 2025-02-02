import requests


class Pessoa:
    """
    Classe que representa uma pessoa, com nome, sobrenome e o estado dos dados obtidos.
    Possui um método para obter dados de um serviço externo.
    """

    def __init__(self, nome, sobrenome):
        """
        Construtor da classe Pessoa.

        Inicializa o nome, sobrenome e o estado 'dados_obtidos' como False.

        :param nome: Nome da pessoa (str).
        :param sobrenome: Sobrenome da pessoa (str).
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        """
        Método que faz uma requisição GET para um serviço externo (JSONPlaceholder).

        Se a requisição for bem-sucedida (status 200), altera o estado de 'dados_obtidos'
        para True e retorna 'CONECTADO'. Caso contrário, retorna 'ERRO 404' e mantém
        'dados_obtidos' como False.

        :return: "CONECTADO" se a requisição for bem-sucedida,
                "ERRO 404" caso contrário.
        """
        resposta = requests.get("https://jsonplaceholder.typicode.com/users/1")

        if resposta.ok:
            self.dados_obtidos = True
            return "CONECTADO"
        else:
            self.dados_obtidos = False
            return "ERRO 404"

import sys
import os

# Adiciona o diretório pai ao caminho de busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importa o módulo de testes e a classe Pessoa
import unittest
from codigo.pessoa import Pessoa
from unittest.mock import patch


class TestePessoa(unittest.TestCase):
    """
    Classe de testes unitários para a classe Pessoa.
    Testa os atributos e métodos da classe Pessoa.
    """

    def setUp(self):
        """
        Método de configuração chamado antes de cada método de teste.
        Cria uma instância de Pessoa para os testes.
        """
        self.p1 = Pessoa("Valter", "Tertuliano")

    def test_pessoa_attr_nome_tem_valor_correto(self):
        """
        Testa se o atributo 'nome' da pessoa tem o valor correto.
        """
        self.assertEqual(self.p1.nome, "Valter")

    def test_pessoa_attr_nome_e_string(self):
        """
        Testa se o atributo 'nome' da pessoa é uma string.
        """
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        """
        Testa se o atributo 'sobrenome' da pessoa tem o valor correto.
        """
        self.assertEqual(self.p1.sobrenome, "Tertuliano")

    def test_pessoa_attr_sobrenome_e_string(self):
        """
        Testa se o atributo 'sobrenome' da pessoa é uma string.
        """
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        """
        Testa se o atributo 'dados_obtidos' da pessoa inicia com o valor False.
        """
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        """
        Testa se o método 'obter_todos_os_dados' retorna 'CONECTADO' e altera
        o estado de 'dados_obtidos' quando a requisição é bem-sucedida.
        """
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        """
        Testa se o método 'obter_todos_os_dados' retorna 'ERRO 404' e não altera
        o estado de 'dados_obtidos' quando a requisição falha.
        """
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        """
        Testa o método 'obter_todos_os_dados' para verificar comportamento em
        sequência de sucesso e falha nas requisições.
        """
        with patch("requests.get") as fake_request:
            # Simula sucesso da requisição
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p1.dados_obtidos)

            # Simula falha da requisição
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p1.dados_obtidos)


if __name__ == "__main__":
    # Executa os testes com saída detalhada
    unittest.main(verbosity=2)

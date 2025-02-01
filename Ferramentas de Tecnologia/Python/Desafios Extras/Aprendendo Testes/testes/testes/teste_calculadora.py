import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from codigos.calculadora import soma, subtrair
import unittest
from codigos.calculadora import soma, subtrair


class TestarCalculadora(unittest.TestCase):
    """Testes para as funções soma e subtrair da calculadora."""

    # Testes para soma
    def test_soma_5_e_5_deve_retornar_10(self):
        """Testa se a soma de 5 e 5 retorna 10."""
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        """Testa se a soma de -5 e 5 retorna 0."""
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        """Testa a função soma com múltiplas entradas."""
        x_y_saidas = (
            (10, 10, 20),
            (20, 10, 30),
            (-10, 10, 0),
            (-20, 10, -10),
        )
        for x, y, saida in x_y_saidas:
            self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        """Testa se a soma falha quando x não é int ou float."""
        with self.assertRaises(AssertionError):
            soma("11", 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        """Testa se a soma falha quando y não é int ou float."""
        with self.assertRaises(AssertionError):
            soma(11, "0")

    # Testes para subtrair
    def test_subtrair_10_e_5_deve_retornar_5(self):
        """Testa se a subtração de 10 e 5 retorna 5."""
        self.assertEqual(subtrair(10, 5), 5)

    def test_subtrair_5_negativo_e_5_deve_retornar_negativo_10(self):
        """Testa se a subtração de -5 e 5 retorna -10."""
        self.assertEqual(subtrair(-5, 5), -10)

    def test_subtrair_varias_entradas(self):
        """Testa a função subtrair com múltiplas entradas."""
        x_y_saidas = (
            (10, 10, 0),
            (20, 10, 10),
            (-10, 10, -20),
            (-20, -10, -10),
        )
        for x, y, saida in x_y_saidas:
            self.assertEqual(subtrair(x, y), saida)

    def test_subtrair_x_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        """Testa se a subtração falha quando x não é int ou float."""
        with self.assertRaises(AssertionError):
            subtrair("11", 0)

    def test_subtrair_y_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        """Testa se a subtração falha quando y não é int ou float."""
        with self.assertRaises(AssertionError):
            subtrair(11, "0")


unittest.main(verbosity=2)

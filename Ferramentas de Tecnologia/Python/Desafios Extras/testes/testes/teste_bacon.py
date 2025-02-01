"""
TDD - Test Driven Development (Desenvolvimento Dirigido a Testes)

Red:
Parte 1 -> Criar o teste e ver falhar.

Green:
Parte 2 -> Criar o código e ver o teste passar.

Refactor:
Parte 3 -> Melhorar o código.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from codigos.bacon import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    """Classe de testes para a função bacon_com_ovos."""

    def test_bacon_com_ovos(self):
        """Deve gerar um erro ao receber um valor inválido."""
        with self.assertRaises(AssertionError):
            bacon_com_ovos("0")

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(
        self,
    ):
        """Deve retornar 'bacon com ovos' se o número for múltiplo de 3 e 5."""
        entradas = (15, 30, 45, 60, 75)
        saida = "bacon com ovos"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, f'{entrada} não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_fome_se_entrada_nao_for_multiplo_de_3_e_5(
        self,
    ):
        """Deve retornar 'fome' se o número não for múltiplo de 3 e 5."""
        entradas = (1, 2, 4, 7, 8)
        saida = "fome"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, f'{entrada} não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_e_multiplo_de_3(self):
        """Deve retornar 'bacon' se o número for múltiplo de 3."""
        entradas = (3, 6, 9, 12, 18)
        saida = "bacon"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, f'{entrada} não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_e_multiplo_de_5(self):
        """Deve retornar 'ovos' se o número for múltiplo de 5."""
        entradas = (5, 10, 20, 25, 35)
        saida = "ovos"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, f'{entrada} não retornou "{saida}"'
                )


# Executa os testes com mais detalhes
unittest.main(verbosity=2)

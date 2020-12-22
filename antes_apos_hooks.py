"""
Unittest - Antes e após hooks

Hooks são os testes em si.

setUp() -> é executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;

tearDown( -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões
com bancos de dados.

"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self) :
        # Configurações do setup
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
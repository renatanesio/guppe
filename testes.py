import unittest

from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    def test_comer_comida_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_comida_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormindo_pouco(self):
        """Testando o retorno com poucas horas de sono"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir 4 horas. =('
        )

    def test_dormir_muito(self):
        """Testando o retorno com muitas horas de sono"""
        self.assertEqual(
            dormir(10),
            'Ah não, dormi muito! Agora estou atrasada para o trabalho!'
        )

if __name__ == '__main__':
    unittest.main()

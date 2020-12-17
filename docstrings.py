"""
Documentando funções com Docstrings

Podemos ter acesso à documentação de uma função em Python
utilizando a propriedade especial __doc__

Ou ainda com help(funcao)
"""


# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'."""
    return "Oi!"


# print(diz_oi.__doc__)

# help(diz_oi)


def exponencial(numero, potencia=2):

    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência à qual elevamos o número.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """

    return numero ** potencia


print(help(exponencial))

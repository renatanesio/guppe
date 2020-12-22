"""
Por que testar códigos?

Testes automatizados!

---------------------------------------
|                                     |
|         frontend e backend          |
|                                     |
---------------------------------------
|        testes automatizados         |
---------------------------------------

Por que testar?
    - Reduzir bugs
    - Testes garantem que novos recursos não quebrem recursos antigos
    - Testes garantem que bugs corrigidos anteriormente continuam corrigidos
    - Testes garantem que a refatoração não tragam novos bugs

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD são utilizados estágios de Desenvolvimento
    - Você escreve seu teste primeiro
    - Então você escreve o código mínimo suficiente para passar
    - Então refatora

Estágios são conhecidos como:
    - Red
    - Green
    - Refactor

"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} faz miau.')


felix = Gato('Felix')

felix.miar()

print(felix.nome)

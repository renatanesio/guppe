"""
POO - Polimosfismo


Sobrescrita de métodos: quando um método de uma classe pai é reimplementado na classe filha (Override)

Overriding é a essência do polimorfismo

"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha deve implementar este método!')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo')


pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

marie = Gato('Marie')
marie.comer()
marie.falar()

splinter = Rato('Splinter')
splinter.comer()
splinter.falar()

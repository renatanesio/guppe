"""
POO - Herança Múltipla

Herança múltipla nada mais é do que a possibilidade de uma classe herdar
de múltiplas classes, fazendo com que a classe filha herde todos os atributos
e métodos de todas as classes herdadas.


OBS: a herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta
    - Por multiderivação indireta


# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass

"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimenta(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimenta(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Willy')
print(baleia.nadar())
print(baleia.cumprimenta())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimenta())

tux = Pinguim('Tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimenta())  # Method Resolution Order - MRO


# Objeto é instância de...

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')


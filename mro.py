"""
POO - MRO - Method Resolution Order

MRO (Ordem de Resolução de Métodos) determina o método que será executado primeiro

Em Python é possível conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    _ Via help()


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


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('Tux')
print(tux.cumprimenta())

"""
Pinguim(Aquatico, Terrestre)
Eu sou Tux do mar!

Pinguim(Terrestre, Aquatico)
Eu sou Tux da terra!

"""

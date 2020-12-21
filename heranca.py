"""
POO - Herança (Inheritance)

A ideia de herança é reaproveitar código, e também extender as classes.

OBS: Com a herança, a partir de uma classe existente, extende-se outra classe
que passa a herdar atributos e métodos da classe herdade.


Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionário
    - nome
    - sobrenome
    - cpf
    - matrícula


OBS: quando uma classe herda de outra classe, ela herda todos os atributos e
métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:

    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

Quando uma classe herda de outra classe, ela é chamada:
    - Sub Classe
    - Classe Filha
    - Classe Específica

Sobrescrita de método ocorre quando sobrescrevemos um método presente na super classe
em classes filhas.

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma incomum de acesso
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionário: {self.__matricula}. Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-10', 5000.00)
funcionario1 = Funcionario('Brad', 'Pitt', '987.654.321-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)


# Sobrescrita de método
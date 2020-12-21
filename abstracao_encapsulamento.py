"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular o código dentro de um grupo lógico
e hiraárquico utilizando classes.

Encapsular -> cápsula


              classe
----------------------------------
|                                |
|      Atributos e Métodos       |
|                                |
----------------------------------

# Relembrando Atributos/Métodos privados em Python

Classe: Pessoa
Atributo privado: __nome
Método privado> __falar

Esses elementos privados só deveriam ser acessados dentro da classe, mas o
Python não bloqueia este acesso. Em vez disso, ocorre o Name Mangling, que altera
a forma de acessar os elementos privados.

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia.Pessoa__falar()


Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e métodos privados de usuário.


"""


class Conta:

    contador = 4999

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f'Saldo de {self.__saldo} reais do titular {self.__titular} com limite de {self.__limite} reais.')

    def depositar(self, valor):
        if(valor > 0):
            self.__saldo += valor
        else:
            print('Operação inválida!')

    def sacar(self, valor):
        if (valor > 0) and (self.__saldo - valor + self.__limite >= 0):
            self.__saldo -= valor
            return True
        else:
            print('Operação inválida!')
            return False

    def transfere(self, conta, valor):
        if(self.sacar(valor)):
            conta.depositar(valor)
            print(f'Foram transferidos {valor} reais de {self.__titular} para {conta.mostra_nome()}.')

    def mostra_nome(self):
        return self.__titular

# conta1 = Conta('Geek', 150.00, 1500)
#
# conta1.extrato()
#
# conta1.depositar(150)
#
# conta1.extrato()
#
# print(conta1.__dict__)
#
# conta1.depositar(-100)
#
# print(conta1.__dict__)
#
# conta1.sacar(-100)
#
# print(conta1.__dict__)
#
# conta1.sacar(3000)
#
# print(conta1.__dict__)
#
# conta1.sacar(1000)
#
# print(conta1.__dict__)

conta1 = Conta('Angelina', 1000.00, 2000.00)
conta2 = Conta('Felicity', 1500.00, 2000.00)

conta1.extrato()
conta2.extrato()

print('\n')

conta1.transfere(conta2, 500)
conta1.extrato()
conta2.extrato()

print('\n')

conta1.transfere(conta2, 1500)
conta1.extrato()
conta2.extrato()

print('\n')

conta2.transfere(conta1, 1000)
conta1.extrato()
conta2.extrato()

print('\n')

conta1.transfere(conta2, 2001.00)
conta1.extrato()
conta2.extrato()
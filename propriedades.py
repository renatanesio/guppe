"""
POO - Propriedades

Getters: retornam valor do atributo
Setters: alteram valor do atributo

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return  self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}.'

    def depositar(self, valor):
        if(valor > 0):
            self.__saldo += valor
            print(f'Foram depositados {valor} reais.')
        else:
            print("Operação inválida!")

    def sacar(self, valor):
        if (valor > 0) and (self.__saldo - valor + self.__limite >= 0):
            self.__saldo -= valor
        else:
            print('Operação inválida!')

    def transferir(self, valor, destino):
        if (valor > 0) and (self.__saldo - valor + self.__limite >= 0):
            self.__saldo -= valor
            destino.__saldo += valor
        else:
            print('Operação inválida!')




conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

conta1.limite = 7000

print(conta1.__dict__)

print(conta1.valor_total)
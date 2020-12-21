"""
POO - Objetos

Objetos: são instâncias da classe.

"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        self.__ligada = not self.__ligada


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def mostra_nome(self):
        return self.__nome


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente.mostra_nome()}')



class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.senha= senha





# Instâncias ou objetos
lamp1 = Lampada('Branca', 127, 60)

print(f'A lâmpada está ligada: {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lâmpada está ligada: {lamp1.checa_lampada()}')

user1 = Usuario('Angelina', 'Jolie', 'aj@gmail.com', '123456')

print(user1)  # Endereço
print(type(user1))

cli1 = Cliente('Angelina Jolie', '123.456.789-10')

cc2 = ContaCorrente(5000, 10000, cli1)

cc2.mostra_cliente()
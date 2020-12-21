"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos
conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
        - Podem ser públicos ou privados
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de Instância: São atributos declarados dentro do método construtor.

OBS: Método construtor: é um método especial utilizado para a construção do objeto.


# Método: funções dentro de uma classe

Em Python, por convenção, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado,
utiliza-se duplo underscore __ no início de seu nome.

Isso é conhecido também como Name Mangling.

# O que significa atributo de instância?

# Significa que, ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

p1 = Produto('PlayStation 4', 'Console', 2500.00)
p2 = Produto('PlayStation 5', 'Console', 5090.00)

print(p1.valor)
print(p2.valor)

# OBS: não é preciso criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)

print(p1.id)
print(p2.id)


"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


# Classes com Atributo de Instância Público

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


# class Produto:
#
#     def __init__(self, nome, descricao, valor):
#         self.id = Produto.contador + 1
#         self.nome = nome
#         self.descricao = descricao
#         self.valor = (valor
#         Produto.contador = self.id


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
# não impedirá que façamos acesso aos atributos sinalizados como privados fora da classe

# Exemplo

user = Acesso('user@gmail.com', '123456')
user.mostra_email()
user.mostra_senha()


# print(user.__senha)  # AttributeError

# print(user._Acesso__senha)  # Temos acesso, mas não deveríamos fazer este acesso (Name mangling)


# Atributos de Classe
# São atributos que são declarados diretamente na classe, ou seja, fora do construtor.
# Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as
# instâncias da classe. Isto é, em vez de cada instância da classe ter seus próprios valores,
# com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:
    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinâmicos: um atributo de instância que pode ser criado
# em tempo de execução

# OBS: O atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('PS4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5 kg'  # Note que na classe produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

print(p1.__dict__)
print(p2.__dict__)

# Deletando atributos

del p2.peso

print(p1.__dict__)
print(p2.__dict__)

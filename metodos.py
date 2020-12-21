"""
POO - Métodos

- Métodos (funções): representam os comportamentos do objeto, ou seja, as
ações que este objeto pode realizar no seu sistema.

Em Python dividimos os métodos em dois grupos: Métodos de instância e Métodos dde Classe

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função
é construir o objeto a partir da classe

OBS: elementos em python que iniciam e terminam com duplo underscore __ é chamado dunder (Double
Underscores)

OBS: Os métodos/funções dunder em python são chamados de métodos mágicos

ATENÇÃO: Não crie funções dunder. Deixe a magia para os mágicos!

# Métodos são escritos em letras minúsculas, usando snake_case


# Exemplos: Métodos de Instância


p1 = Produto('PS4', 'Video Game', 2300)
print(p1.desconto(20))
print(p1.desconto(10))

user1 = Usuario('AngElina', 'JoLie', 'angelina@gmail.com', 'BradPitt')
print(Usuario.nome_completo(user1))
print(user1.nome_completo())

print(user1.checa_senha('BradPitt'))

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Digite seu email: ')
senha = input('Digite a senha: ')
confirma_senha = input('Confirme a senha: ')

user = None
if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criado com sucesso!')
else:
    print('Senha não confere.')


if user is not None:
    senha = input('Digite a senha para acesso: ')
    if user.checa_senha(senha):
        print('Seja bem-vindo de volta.')
    else:
        print('Acesso inválido!')

if user is not None:
    print(f'Senha user Criptografafa: {user._Usuario__senha}.')


# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens



"""


# Métodos de Instância

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * (100 - porcentagem) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    @staticmethod
    def definicao():
        return 'UXR344'


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__email = email
        self.__senha = cryp.hash(senha)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if(cryp.verify(senha, self.__senha)):
            return True
        return False

    # Método privado
    def __gera_usuario(self):
        return self.__email.split('@')[0]



# Método estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Ana', 'Grama', 'anagrama@gmail.com', 'GramaAna')

print(user._Usuario__gera_usuario())  #NÃO faça isso

# Métodos de Classe

Usuario.conta_usuarios()

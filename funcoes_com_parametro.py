"""
Funções com Parâmetros (de entrada)

- Funções que recebem dados a serem processados

entrada -> processamento -> saída

Há funções:
- Sem entrada e sem saída
- Com entrada, mas sem saída
- Sem entrada, mas com saída
- Com entrada e com saída


# Refatorando uma função
def quadrado_de_7():
    return 7*7


def quadrado(numero):
    return numero ** 2


def cubo(numero):
    return numero ** 3


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(cubo(7))
print(cubo(2))
print(cubo(5))

ret = cubo(6)
print(ret)


# Refatorando a função
def cantar_parabens(aniversariante):
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!")
    print(f'Viva o(a) {aniversariante}!\n')


cantar_parabens('Renata')


# Funções podem ter n parâmetros de entrada, separados por vírgula


# Exemplos
def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(2, 5))
print(multiplica(10, 20))

print(outra(2, 5, 'Geek'))
print(outra(3, 2, 'Python'))

# OBS: Se a gente informar um valor errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 3, 2))  # Argumentos demais - TypeError
# print(soma(2))  # Argumentos a menos - TypeError


# Nomeando parâmetros
def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'


# Refatorando
def nome_completo(nome, sobrenome): # Parâmetros
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Albert', 'Einstein')) # Argumentos


# A diferença entre parâmetros e argumentos

# - Parâmetros são variáveis declaradas na definição de uma função

# - Argumentos são dados passados durante a execução de uma função



# A ordem dos argumentos importa

print(nome_completo('Einstein', 'Albert'))


# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem

print(nome_completo(sobrenome='Einstein', nome='Albert'))

"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = range(10)

print(soma_impares(lista))

tupla = tuple(range(10))
print(soma_impares(tupla))

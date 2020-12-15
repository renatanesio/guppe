"""
Default parameters

- Argumentos são opcionais

# Exemplo de argumento opcional

print("Geek")
print()  # Opcional


# Exemplo de argumento obrigatório

def quadrado(numero):
    return numero ** 2


print(quadrado(2))  # Argumento obrigatório


# Exemplo de argumento opcional

def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(2, 4))

print(exponencial(2))  # Por padrão, eleve ao quadrado


# OBS: Em funções Python, os parâmetros com valores default devem sempre estar ao final da declaraçã

def teste(num=2, potencia):  # SyntaxError
    return num ** potencia


# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo, instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você fosse o instrutor.'
    return f'Olá, {nome}!'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Samanta'))


# Por que utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis

# Qualquer tipo de dado pode ser usado como parâmetro

"""


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2,2, subtracao))

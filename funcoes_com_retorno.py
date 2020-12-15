"""
Funções com retorno


numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')



def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()

print(f'Retorno de ret: {ret}')

# OBS: Em Python, quando uma função não retorna um valor, o retorno é None

# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()

print(f'Retorno de ret: {ret}')

OBS: não é preciso criar uma variável para receber o retorno de uma função.
Ela pode ser passada para outras funções.


# Refatorando a primeira função


def diz_oi():
    return 'Oi, '


alguem = "Pedro"

print(diz_oi() + alguem)


OBS: Sobre a palavra reservada return

1 - Ela finaliza a função
2 - Podemos ter diferentes returns em uma função
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

# Exemplo 1 - Ela finaliza a função

def diz_oi():
    print("Estou sendo executado antes do retorno...")
    return 'Oi!'
    # print("Estou sendo executado após o retorno...")  # Nunca seria executada

diz_oi()


# Exemplo 2 - Podemos ter diferentes returns em uma função


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 'b'


print(nova_funcao())


# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
"""

# Vamos criar uma função para jogar a moeda


from random import random


def joga_moeda():
    # Gera um número pseudo-aleatório entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

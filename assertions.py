"""
Assertions (Afirmações)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações
utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo
AssertionError.

OBS: Podemos especificar, opcionalmente, um segundo argumento ou até mesmo uma mensagem de
erro personalizada.

OBS: A palavra 'assert' pode ser utilizada em qualquer função.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado.

"""


def soma_numeros_positivos(a,b):
    assert a >= 0 and b >= 0, 'Ambos precisam ser positivos!'
    return a + b


ret = soma_numeros_positivos(0, 4)
ret = soma_numeros_positivos(-1, 4)
print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'batata frita',
        'doces',
        'cachorro quente',
    ], 'A comida precisa ser fast food'
    return f'Estou comendo {comida}'


comida = input('Informe a comida: ')
print((comer_fast_food(comida)))



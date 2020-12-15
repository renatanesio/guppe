"""
Dicionários

OBS: em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos da América', 'py': 'Paraguay'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos da América', py='Paragyau')
print(paises)
print(type(paises))


# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# OBS: caso tentemos acessar usando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get (Recomendado)

print(paises.get('br'))
print(paises.get('ru'))

OBS: o tipo None em Python é sempre considerado falso

pais = paises.get('py')

russia = paises.get('ru')
# Cao o get não encontre o objeto com a chave informada será retornado o valor None

if russia:
    print(f'Encontrei o país {russia}!')
else:
    print("País não encontrado!")

if pais:
    print(f'Encontrei o país {pais}!')
else:
    print("País não encontrado!")

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')
print(pais)


# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla,
# dicionário, como chaves


# Tuplas são interessantes como chaves de dicionários por serem imutáveis
localidades = {
    (51.500719996351194, -0.12463210689698899): 'Big Ben',
    (51.503273905319034, -0.119521514868192): 'London Eye',
    (51.501339383865144, -0.14184652620187163): 'Palácio de Buckingham'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# Conclusão 1: a forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma

# Conclusão 2: em dicionários, NÃO podemos ter chaves repetidas

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 = Mais comum

ret = receita.pop('mar')
print(ret)

# OBS 1: aqui precisamos sempre informar a chave, caso contrário um KeyError será retornado
# OBS 2: ao removermos um objeto, o valor deste objeto é sempre retornado

# Forma 2

del receita['fev']
print(receita)

# Se a chave não existir, será gerado um key error
# OBS: neste caso, o valor removido não é retornado


"""

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras em que adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
    - nome
    - quantidade
    - preço
    Produto 2
    - nome
    - quantidade
    - preço

# - Poderíamos utilizar uma lista para isso

carrinho = []

produto1 = ['PlayStation 5', 1, 5090.00]
produto2 = ['Cyberpunk 2077', 1, 251.91]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 2 - Poderíamos utilizar uma Tupla para isso

produto1 = ('PlayStation 5', 1, 5090.00)
produto2 = ('Cyberpunk 2077', 1, 251.91)

carrinho = (produto1, produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 3 - Poderíamos utilizar um dicionário para isso

carrinho = []

produto1 = {'nome': 'PlayStation 5', 'quantidade': 1, 'preço': 5090.00}
produto2 = {'nome': 'Cyberpunk 2077', 'quantidade': 1, 'preço': 251.91}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário
d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 - Deep copy
d = dict(a=1, b=2, c=3)

novo = d.copy()

print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow copy

d = dict(a=1, b=2, c=3)

novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)

"""


# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# O método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e atribuirá a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')

print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

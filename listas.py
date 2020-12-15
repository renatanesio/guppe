"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem DINÂMICOS e também podermos colocar QUALQUER tipo de dados.

Linguagens C/Java: arrays
    - Possuem tamanho e tipo de dado fixos

Já em Python:
- Dinâmico: não possui tamanho fixo
- Qualquer tipo de dado

As listas em Python são representadas por colchetes []

Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, só é possível adicionar um elemento por vez

lista.append() -> adiciona um único valor à lista, coloca uma lista como elemento único

lista.extend() -> adiciona cada valor de um iterável como elemento adicional
    - funciona também como lista_a + lista_b

lista.reverse() -> inverte uma lista
print(lista[::-1]) -> inverte a impressão da lista

len(lista) -> número de elementos de uma lista

lista.pop() -> remove o último elemento de uma lista e retorna esse último elemento

lista5.clear() -> remove todos os elementos da lista

texto.split() -> separa os elementos da lista pelo espaço (default)

texto = ' '.join(lista) -> Transforma lista em string e adiciona espaço entre cada elemento
"""

# lista1 = [1, 3, 6, 9, 85, 78, 95, 5, 66, 98, 18]
# print(lista1)
# lista2 = ["R", "e", "n", "a", "t", "a", " ", "N", "é", "s", "i", "o"]
# print(lista2)
# lista3 = []
# print(lista3)
# lista4 = list(range(1, 51, 5))
# print(lista4)
# lista5 = list("Renata Nésio")
# print(lista5)
#
# # Podemos facilmente checar se determinado valor está contido na lista
# num = 6
# if num in lista4:
#     print(f'\nEncontrei o número {num}!')
# else:
#     print(f'\nO número {num} não está aqui!')
#
# caractere: str = 'z'
# if caractere in lista5:
#     print(f'Encontramos o caractere {caractere}!')
# else:
#     print(f'Desculpe, o caractere {caractere} não está aqui!')
#
# # Podemos facilmente ordenar uma lista
# lista1.sort()
# print(lista1)
#
# lista2.sort()
# print(lista2)
#
# # Podemos facilmente contar o número de ocorrências de um valor em uma lista
# c = 'a'
# print(f'\nHá {lista5.count(c)} ocorrências do caractere {c}.')
#
# # Podemos facilmente adicionar novos elementos à lista com a função append
# print(lista1)
# lista1.append(1001)
# print(lista1)
#
# # Coloca uma lista como elemento único
# lista1.append([1, 2, 3])
#
# if [3, 2, 3] in lista1:
#     print("\nEncontrei a lista!")
# else:
#     print("\nDesculpe, a lista não está aqui.")
#
# # Coloca cada valor da lista como um elemento adicional
# lista1.extend([123, 321])
#
# print(lista1)
#
# lista1.extend([5])
#
# print(lista1)
#
# lista1.extend('Enacom')
#
# print(lista1)
#
# # Podemos inserir um novo elemento na lista informando a posição do índice
# # Isso não substitui o valor inicial, que será deslocado para a direita da lista
# lista1.insert(2, 'Novo valor')
# print(lista1)
#
# # Podemos facilmente juntar duas listas
#
# lista6 = lista1 + lista2
# print(lista6)
#
# # Podemos facilmente inverter uma lista
# lista1.reverse()
# print(lista1)
#
# lista1.reverse()
# print(lista1[::-1])
#
# # Copiar uma lista
# lista6 = lista2.copy()
# print(lista6)
#
# # Tamanho de uma lista
# print(len(lista2))
#
# # Podemos remover facilmente o último elemento de uma lista
# print(lista5)
# print(lista5.pop())
# print(lista5)
#
# # Podemos remover um elemento pelo índice
# print(lista5.pop(3))
# print(lista5)
#
# # Podemos facilmente limpar uma lista
# lista5.clear()
# print(lista5)
#
# # Podemos facilmente repetir elementos em uma lista
# nova = [1, 2, 3]
# nova = nova * 3
# print(nova)
#
# # Podemos facilmente converter uma string para uma lista
# curso = "Programação em Python do básico ao avançado"
# print(curso)
# curso = curso.split(' ')
# print(curso)
#
# curso = "Programação,em,Python,do,básico,ao,avançado"
# print(curso)
# curso = curso.split(',')
# print(curso)
#
# # Convertendo uma lista em uma string
# lista7 = ['Programação', 'em', 'Python', 'do', 'básico', 'ao', 'avançado']
# print(lista7)
#
# # Pega a lista7, pega o espaço entre cada elemento e transforma em uma string
# curso = ' '.join(lista7)
# print(curso)
#
# # Iterando sobre listas
#
# # Exemplo 1 - Utilizando for
# for elemento in lista1:
#     print(elemento, end=' ')
#
# # Exemplo 2 - Utilizando for
# soma = ''
# for elemento in lista1:
#     soma = soma + str(elemento)
# print("\n" + soma, end=' ')
#
# # Exemplo 3 - Utilizando while
# carrinho = []
# produto = ''
#
# while produto != 'sair':
#     produto = input('\nAdicione um produto ao carrinho ou digite "sair" para sair: ')
#     if produto != 'sair':
#         carrinho.append(produto)
# print("Seu carrinho tem:")
# for indice, item in enumerate(carrinho):
#     if indice != len(carrinho)-1:
#         print(item, end=', ')
#     else:
#         print(item, end='')
#
# # Utilizando variáveis em listas
# num1 = 1
# num2 = 2
# num3 = 3
# numeros = [num1, num2, num3]
#
# print('\n')
# print(numeros)

# # Fazemos acesso aos elementos de forma indexada
#
cores = ['verde', 'amarelo', 'azul', 'branco']
# print(cores[0])  # verde
# print(cores[1])  # amarelo
# print(cores[2])  # azul
# print(cores[3])  # branco
#
# # Fazer acesso aos elementos de forma inversa
#
# print(cores[-1])  # branco
# print(cores[-2])  # azul
# print(cores[-3])  # amarelo
# print(cores[-4])  # verde
#
# for cor in cores:
#     print(cor)

# indice = 0
#
# while indice < len(cores):
#     print(cores[indice])
#     indice = indice + 1

# Gerar indice em um for

# for indice, cor in enumerate(cores):
#     print(indice, cor)

# cores = list(enumerate(cores)
# print(cores)

# # Listas aceitam valores repetidos
#
# lista = []
# lista.append(44)
# lista.append(44)
# lista.append(26)
# lista.append(26)
#
# print(lista)

# Encontrar o índice de um elemento na lista

# numeros = [26, 25, 6, 12, 89, 59, 26]
#
# print(numeros.index(89))
#
# # Se o número não estiver na lista, será apresentado erro
# # print(numeros.index(7))
#
# print(numeros.index(26))  # Retorna índice do primeiro valor encontrado
#
# # Podemos fazer uma busca dentro de um range, ou seja, por qual índice começar a buscar
# print(numeros.index(26, 3))
#
# # Podemos fazer busca dentro de um range, início/fim
# print(numeros.index(6, 1, 5))

# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(lista[1:4])
#
# print(lista[1:])  # Parâmetro início
# print(lista[-2:])  # Parâmetro início
#
# print(lista[:2])  # Parâmetro fim, exclusivo
# print(lista[:-3])  # Parâmetro fim, exclusivo
#
# print(lista[::])  # Imprime todos
#
# print(lista[2:7:2])  # Imprime de dois em dois

# nomes = ['Geek', 'University']
#
# nomes[0], nomes[1] = nomes[1], nomes[0]
#
# print(nomes)
#
# nomes.reverse()
# print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se forem floats/inteiros
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(sum(lista))  # Soma
# print(max(lista))  # Valor máximo
# print(min(lista))  # Valor mínimo
# print(len(lista))  # Tamanho da lista

# Transformar lista em tupla

# print(lista)
# print(type(lista))
#
# tupla = tuple(lista)
# print(tupla)
# print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1, num2, num3)

# Se tivermos um número diferentes na lista do número de variáveis para receber, haverá erros

# Copiando uma lista para outra (Shallow copy e Deep copy)

# Forma 1

lista = [1, 2, 3]

# Veja que ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista,
# mas elas são independentes. Isso é chamado de Deep Copy

print(lista)
nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista,
# mas após realizar uma mo
lista = [1, 2, 3]

print(lista)
nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

lista.append(5)
print(lista)
print(nova)

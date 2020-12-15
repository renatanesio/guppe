"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis

# Cuidado 1: as tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4) # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4= (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

(4) -> não é tupla
(4,) -> é tupla
4, -> é tupla

# Conclusão: podemos concluir que as tuplas são definidas pela vírgula e não pelo uso do parênteses

# Podemos gerar uma tupla dinamicamente com range(início, fim, parada)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tuplas

tupla = ('Geek University', 'Programação em Python')
escola, curso = tupla

print(escola)
print(curso)

# OBS: gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

# Os métodos para adição e remoção de elementos nas tuplas não existem, porque são imutáveis

# Soma, Valor Máximo, Valor Mínimo, Tamanho

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1+tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1+tupla2
print(tupla3)

# Tuplas são imutáveis, mas podemos sobrescrever seus valores
tupla1 = tupla1+tupla2
print(tupla1)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)
print(26 in tupla)

# Iterando em uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# O acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i], end=' ')
    i += 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

# Slicing
# tupla[inicio:fim:passo]
print(meses[5:9])

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

# Exemplo

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro*
# * Porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

# Não há shallow copy em tuplas
nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)

tupla = (1, 2, 3)
print(dir(tupla))

"""



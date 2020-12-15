"""
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusivo (início padrão 0, passo de 1 em 1)

# Forma 2

range (valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusivo (início especificado, passo de 1 em 1)

# Forma 3

range (valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusivo (início especificado, final especificado, passo especificado)

# Forma 4 (Forma 3, só que inversa)

range (valor_inicial, valor_de_parada, passo inverso)

OBS: valor_de_parada não inclusivo (início especificado, parada especificada, passo especificado)

"""

# Forma 1
for num in range(11):
    print(num, end=" ")

print("\n")

# Forma 2
for num in range(1, 11):
    print(num, end=" ")

print("\n")

# Forma 3
for num in range(5, 51, 5):
    print(num, end=" ")

print("\n")

# Forma 4
for num in range(50, -1, -5):
    print(num, end=" ")

print("\n")

lista = list(range(0, 101, 20))

print(lista)

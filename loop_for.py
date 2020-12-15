"""
Loop for

Loop -> estrutura de repetiçãoo
For -> uma dessas estruturas

C ou Java

for(int i = 0; i < 0; i++){
    //execução do loop
}

Python

for item in iterável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou valores iteráveis

Exemplos de iteráveis
- String
    nome = "Enacom Handicrafted Technologies"
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
    range(valor_inicial, valor_final)
    OBS: valor_final não inclusivo

- Enumerate
((0, 'H'), (1, 'a'), (2, 'n')...)

OBS: quando não precisamos de um valor, podemos descartá-lo utilizando um underscore (_)

https://www.unicode.org/emoji/charts/full-emoji-list.html
"""

nome = "Enacom Handicrafted Technologies"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in numeros:
    print(numero)

# Exemplo de enumerate 1
for indice, letra in enumerate(nome):
    print(indice, letra)

# Exemplo de enumerate 2
for _, letra in enumerate(nome):
    print(letra, end='')
print("\n")

# qtd = int(input("Quantas vezes esse loop deve rodar? "))
#
# soma = 0
# for n in range(1, qtd + 1):
#     num = int(input(f'Informe o valor {n}/{qtd}: '))
#     soma = soma + num

# print(f'A soma é {soma}.')

# Original+ U+1F970
# Modificado: U0001F970

emoji = ''

for _ in range(3):
    for num in range(1, 10):
        print('\U0001F970' * num)

# Original+ U+1F973
# Modificado: U0001F973

emoji = "U0001F973"

for _ in range(3):
    for num in range(1, 10):
        print('\U0001F973' * num)

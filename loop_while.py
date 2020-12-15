"""
Loop while

Forma geral

while expressao_booleana:
    # execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira

Expressão booleana é toda expressão cujo resultado é verdadeiro ou falso

É importante cuidar do critério de parada
"""

# Exemplo 1
numero = 1
while numero < 10:
    print(numero, end=" ")
    numero += 1

print("\n")

# Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input('Já chegamos? ')

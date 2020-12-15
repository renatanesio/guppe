"""
PEP8 - Python Enhancement Proposal

Propostas de melhorias para a linguagem Python

The Zen of Python
import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] Utilize CamelCase para nomes de classes;

class CalculadoraCientifica:
    pass

[2] Utilize nomes em minúsculo separados por underscore para funções ou variáveis;

def soma():
    pass

def soma_dois():
    pass

[3] Utilize 4 espaços para indentação!!

if 'a' in 'banana':
    print("tem")

[4] Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] Imports devem ser sempre feitos em linhas separadas
import sys
import os

from types import StringType, ListType

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

- Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou doctrings
e antes de constantes ou variáveis globais

[6] Espaços em expressões e instruções

funcao(algo[1], {outro: 2})
algo(1)
dict['chave'] = lista[indice]
x = 1
y = 2
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha
"""

"""
Definindo funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares repetidas vezes;

OBS: se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.


Já utilizamos:
- print()
- len()
- max()
- min()
- count()


# Exemplo de utilização de funções:

cores = ['rosa', 'roxo', 'vermelho', 'azul']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python'

print(curso)

cores.append('branco')

print(cores)

# curso.append("Mais dados...")  #AttributeError

cores.clear()
print(cores)


# print(help(print))

# DRY - Don't Repeat Yourself



Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
nome_da_funcao -> SEMPRE com letras minúsculas e, se for nome composto, separado por underscore (snake_case)

bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função

OBS: veja que para definir uma função utilizamos a palavra reservada 'def', informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com dois pontos :


"""

"""
OBS: 

1 - Veja que dentro de uma função podemos utilizar outras funções
2 - Veja que nossa função só executa uma tarefa
3 - Veja que esta função não recebe nenhum parâmetro de entrada
4 - Veja que esta função não tem retorno

# Definindo a primeira função


# Exemplo 1

def diz_oi():
    print('oi!')


diz_oi()

# Exemplo 2

def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!")
    print("Viva o aniversariante!\n")


for _ in range(5):
    cantar_parabens()
    
# Em Python, podemos criar variáveis do tipo de uma função e executar esta função através da variável

def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!")
    print("Viva o aniversariante!\n")


canta = cantar_parabens

canta()
    
    
"""


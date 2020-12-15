"""
Recebendo dados do usuário

input -> Todo dado recebido via input é do tipo String

"""
# Entrada de dados
nome = input("Qual seu nome? ")

# Processamento
nome = nome.title()

# Saída de dados
print('Olá, %s' % nome)

# Nova entrada de dados
idade = input("Qual a sua idade? ")

# Saída de dados
if int(idade) < 18:
    # print 'antigo' 2.x
    # print("Desculpe, %s, você tem apenas %s anos e não pode entrar." % (nome, idade))
    # print 'moderno' 3.x
    print('Desculpe, {0}, você tem apenas {1} anos e não pode entrar.'.format(nome, idade))
else:
    # exemplo de print 'mais atual' 3.7
    print(f'Seja bem-vindo(a), {nome}. Você nasceu em {2020 - int(idade)}, correto?')

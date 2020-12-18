"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real representados
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos
    conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada,
    possivelmente iríamos querer saber se ela é 110V ou 220V, sua cor, sua luminosidade, etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este
    objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se de ambas as palavras em maiúsculo, todas juntas (CamelCase).

OBS: Quando planejamos um software e definimos quais classes teremos que ter no sistema, chamamos estes
objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()
conta = ContaCorrente()

print(type(lamp))
print(type(conta))
print(help(int))

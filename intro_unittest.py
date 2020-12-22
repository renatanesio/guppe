"""
Introdução ao módulo Unittest

https://docs.python.org/3/library/unittest.html

Unittest -> Testes unitários

O que são testes unitários?
    - Forma de testar unidades individuais de código fonte
        - Unidades individuais: funções, métodos, classes, módulos, etc

# OBS: Teste unitário não é específico da linguagem Python

Para criar os testes, criamos classes que herdam de unittest.TestCase e então
ganhamos todos os 'assertions' presentes no módulo.

Para rodar todos os testes, utilizamos unittest.main()

TestCase: casos de teste para sua unidade

# Conhecendo as assertions

Método                          Checa que
--------------------------------------------
assertEqual(a, b)               a == b
assertNotEqual(a, b)            a != b
assertTrue(x)                   x é verdadeiro
assertFalse(x)                  x é falso
assertIs(a, b)                  a é b
assertIsNot(a, b)               a não é b
assertIsNone(x)                 x é None
assertIsNotNone(x)              x não é None
assertIn(a, b)                  a está em b
assertNotIn(a, b)               a não está em b
assertIsInstance(a, b)          a é instância de b
assertNotIsInstance(a, b)       a não é instância de b


Por convenção, todos os testes em um test case devem ter seu nome iniciado com test_.

# Para executar os testes com unittest:

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose:

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendável) docstrings nos testes.


"""


# Prática - Utilizando a abordagem TDD
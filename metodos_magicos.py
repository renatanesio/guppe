"""
POO - Métodos mágicos

São todos os métodos que utilizam dunder

Dunder -> Double Underscore

dunder init -> __init__

dunder repr -> Representação do objeto

"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor.title()
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo}, escrito por {self.__autor}'

    def __str__(self):
        """Tem prioridade sobre __repr__"""
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória.')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += str(self) + ' '
            return msg
        return 'Operação inválida!'


livro1 = Livro('Crime e Castigo', 'Fiódor Dostoiévski', 591)
livro2 = Livro('Os Irmãos Karamázov', 'Fiódor Dostoiévski', 911)

# Representação do objeto
print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))
print(repr(livro1))
print(repr(livro2))

# del livro1
# del livro2

print(livro1 + livro2)

print(livro1*3)

# dir(__builtins__)

# https://pt.stackoverflow.com/questions/176465
# https://awari.com.br/metodos-magicos-em-python-desvendando-os-segredos-da-programacao
# https://awari.com.br/metodos-magicos-em-python-aprenda-a-utilizar-os-segredos-da-linguagem-de-programacao

# Métodos mágicos, também conhecidos como métodos especiais ou métodos dunder (por começarem e terminarem com duplo
# sublinhado), são funções embutidas em classes Python que permitem a implementação de comportamentos específicos.
# Eles são chamados implicitamente pelo interpretador Python em certas situações. Aqui está um resumo dos métodos
# mágicos mais utilizados em Python, juntamente com exemplos:

# __init__(self, ...): Método de inicialização, chamado quando uma instância da classe é criada.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("João", 30)


# __str__(self): Retorna a representação de string da instância. É chamado quando str(obj) é usado.
class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"


p2 = Pessoa2("João", 30)
# print(str(p1))  # Saída: João tem 30 anos


# __repr__(self): Retorna a representação oficial da instância. É chamado quando repr(obj) é usado ou quando a instância
# é mostrada no shell interativo.
class Pessoa3:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"


p3 = Pessoa3("João", 30)
# print(repr(p1))  # Saída: Pessoa('João', 30)


# __len__(self): Retorna o tamanho da instância. É chamado quando len(obj) é usado.
class MinhaLista:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


lista = MinhaLista([1, 2, 3, 4, 5])
# print(len(lista))  # Saída: 5


# __getitem__(self, key): Permite acesso aos itens da instância usando a notação de colchetes [].
class MinhaLista2:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


lista2 = MinhaLista2([1, 2, 3, 4, 5])
print(lista2[2])  # Saída: 3


# __iter__(self): Retorna um iterador para a instância. É usado em loops e quando iter(obj) é chamado.
class MinhaLista3:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)


lista3 = MinhaLista3([1, 2, 3, 4, 5])
for item in lista3:
    print(item)  # Saída: 1, 2, 3, 4, 5


# __contains__(self, item): Verifica se um item está presente na instância. É chamado quando item in obj é usado
class MinhaLista4:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


lista4 = MinhaLista4([1, 2, 3, 4, 5])
print(3 in lista4)  # Saída: True


# __add__(self, other): Define a operação de adição para a instância. É chamado quando obj1 + obj2 é usado.
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)


po1 = Ponto(1, 2)
po2 = Ponto(3, 4)
po3 = po1 + po2
print((p3.x, p3.y))  # Saída: (4, 6)


# __call__(self, ...): Permite que a instância seja chamada como uma função.
class Calculadora:
    def __call__(self, x, y):
        return x + y


calc = Calculadora()
print(calc(3, 4))  # Saída: 7


# __eq__(self, other): Define o comportamento de igualdade entre duas instâncias. É chamado quando obj1 == obj2 é usado.
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Ponto(1, 2)
p2 = Ponto(1, 2)
print(p1 == p2)  # Saída: True

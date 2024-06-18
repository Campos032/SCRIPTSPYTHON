# Os paradigmas de programação representam diferentes estilos ou abordagens para resolver problemas de programação.
# Aqui estão alguns dos paradigmas mais importantes:

# Programação Imperativa: Este é o paradigma mais comum, onde os programas consistem em uma sequência de instruções
# que alteram o estado do programa. Exemplos incluem linguagens como C e Python.

# Programação Orientada a Objetos (POO): Este paradigma organiza o código em objetos que podem conter dados e métodos
# para manipular esses dados. Exemplos de linguagens de programação orientadas a objetos incluem Java, C++, e Python.

# Programação Funcional: Este paradigma trata a computação como uma avaliação de funções matemáticas e evita o estado
# e a mutação de dados. Linguagens funcionais populares incluem Haskell, Lisp, e Erlang.

# Programação Lógica: Este paradigma se baseia em regras lógicas e inferência para computar resultados. Prolog é uma
# linguagem de programação lógica comum.

# Programação Baseada em Restrições: Este paradigma expressa problemas como restrições sobre as variáveis que devem
# ser satisfeitas. O solucionador de restrições então encontra soluções que satisfaçam todas as restrições. Exemplos
# incluem linguagens como CHR (Constraint Handling Rules).

# Programação Orientada a Eventos: Neste paradigma, o fluxo de controle do programa é determinado pelos eventos que
# ocorrem no sistema. JavaScript é uma linguagem que suporta esse paradigma para desenvolvimento web.

# Programação Orientada a Aspectos (AOP): Este paradigma permite modularizar comportamentos que afetam várias partes
# do código. AspectJ é uma linguagem de programação que estende o Java com recursos de AOP.

# Programação Reativa: Este paradigma é centrado na propagação automática de mudanças. É comumente usado em
# aplicações que envolvem fluxos contínuos de dados, como interfaces de usuário reativas e sistemas distribuídos.
# Exemplos incluem RxJava (para Java) e RxJS (para JavaScript).

# Exemplo de resolução de um mesmo problema em cada paradigma
# Programação Imperativa:
# Problema: Calcular a soma dos elementos de uma lista.
def soma_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma


lista1 = [1, 2, 3, 4, 5]
print(soma_lista(lista1))  # Saída: 15


# Programação Orientada a Objetos (POO):
# Problema: Calcular a soma dos elementos de uma lista usando uma classe.
class Calculadora:
    def __init__(self, lista):
        self.lista = lista

    def soma_lista(self):
        return sum(self.lista)


lista = [1, 2, 3, 4, 5]
calc = Calculadora(lista)
print(calc.soma_lista())  # Saída: 15

# Programação Funcional:
# Problema: Calcular a soma dos elementos de uma lista usando programação funcional.
from functools import reduce

lista = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, lista)
print(soma)  # Saída: 15


# Programação Lógica:
# Problema: Calcular a soma dos elementos de uma lista usando recursão em programação lógica
# (em Python, não é o paradigma principal, mas podemos simular).
def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])


lista = [1, 2, 3, 4, 5]
print(soma_lista(lista))  # Saída: 15

# Programação Baseada em Restrições:
# Problema: Calcular a soma dos elementos de uma lista usando a biblioteca PuLP para programação linear
# (simulando restrições).
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

lista = [1, 2, 3, 4, 5]
prob = LpProblem("Soma_Lista", LpMaximize)
vars = LpVariable.dicts("x", range(len(lista)), lowBound=0, cat='Integer')
prob += lpSum(vars[i] * lista[i] for i in range(len(lista)))
prob.solve()

soma = sum(vars[i].varValue * lista[i] for i in range(len(lista)))
print(int(soma))  # Saída: 15

# Programação Orientada a Eventos:
# Problema: Calcular a soma dos elementos de uma lista utilizando a biblioteca tkinter para capturar eventos de clique
# de botão.
import tkinter as tk


def calcular_soma():
    soma = sum(int(entry.get()) for entry in entries)
    resultado_label.config(text=f"Soma: {soma}")


janela = tk.Tk()
entries = []
for i in range(5):
    entry = tk.Entry(janela)
    entry.pack()
    entries.append(entry)

calcular_button = tk.Button(janela, text="Calcular Soma", command=calcular_soma)
calcular_button.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()


# Programação Orientada a Aspectos (AOP):
# Exemplo: Calcular a soma dos elementos de uma lista com logging antes da execução da função.
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executando função: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logging_decorator
def soma_lista(lista):
    return sum(lista)


lista = [1, 2, 3, 4, 5]
print(soma_lista(lista))  # Saída: 15

# Programação Reativa:
# Problema: Calcular a soma dos elementos de uma lista reativamente usando a biblioteca RxPy.
from rx import from_
from rx.operators import scan

lista = [1, 2, 3, 4, 5]
observable = from_(lista)

soma = observable.pipe(
    scan(lambda acc, x: acc + x)
).subscribe(lambda result: print(result))

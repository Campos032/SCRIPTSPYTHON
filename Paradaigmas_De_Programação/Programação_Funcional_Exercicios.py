# Mapeamento (Mapping):
# Escreva uma função que receba uma lista de números e retorne uma nova lista com cada elemento multiplicado por 2.
def mapping(function, lista: list):
    return [function(num) for num in lista]


def multi_2(num):
    return num * 2


lista_numeros = [1, 2, 4, 6]

dobro_lista = mapping(multi_2, lista_numeros)


# print(dobro_lista)


# Filtragem (Filtering):
# Escreva uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.
def filter_pair(function, lista: list):
    return [num for num in lista if function(num)]


def div_2(num):
    return num % 2 == 0


lista_original = [1, 2, 4, 6]

lista_pares = filter_pair(div_2, lista_original)

# print(lista_pares)
# print(lista_original)


# Redução (Reducing):
# Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.
def soma_lista(lista):
    return [num + lista[i + 1] for i, num in enumerate(lista) if i < len(lista) - 1]


lista_somar = [1, 2]

lista_somada = soma_lista(lista_somar)

# print(lista_somada)


# Recursão:
# Escreva uma função recursiva para calcular o fatorial de um número.
def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial(num - 1)


fatorial_teste = fatorial(5)
# print(fatorial_teste)


# Currying:
# Escreva uma função que aceite três argumentos e retorne a soma dos três.
def soma(a, b, c):
    return a + b + c


soma_teste = soma(1, 2, 3)
# print(soma_teste)


# Aplicação Parcial: Utilizando currying, escreva uma função que aceite dois argumentos e retorne a soma deles. Em
# seguida, aplique parcialmente essa função para criar uma nova função que adicione 10 a um número.
def soma(a):
    def soma_b(b):
        def soma_c(c):
            return a + b + c
        return soma_c
    return soma_b


soma_parcial = soma(1)(2)
# print(soma_parcial)
resultado = soma_parcial(3)
# print(resultado)  # Saída: 6


# Composição de Funções: Escreva duas funções, uma que receba um número e o eleve ao quadrado e outra que multiplique
# um número por 2. Em seguida, crie uma terceira função que seja a composição dessas duas funções.
def quadrado(num):
    return num ** 2


def multi_2(num):
    return num * 2


def combina(num):
    return multi_2(quadrado(num))


teste = combina(2)
# print(teste)

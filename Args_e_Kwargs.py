# www.hashtagtreinamentos.com/args-e-kwargs-em-python

# *args:
# O *args permite que você passe um número variável de argumentos posicionais para uma função.
# Os argumentos são empacotados em uma tupla dentro da função.

def my_function(*args):
    for arg in args:
        print(arg)


my_function(1, 2, 3, 4)


# **kwargs:
# O **kwargs permite que você passe um número variável de argumentos de palavras-chave para uma função.
# Os argumentos são empacotados em um dicionário dentro da função.

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_function(name="Alice", age=25, city="New York")

# Escreva uma função chamada soma_todos que aceita um número variável de argumentos posicionais e retorna a soma de
# todos os números passados como argumentos.
def soma_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total
# print(soma_todos(2, 9, 4, 5))


# Escreva uma função chamada concatenar_strings que aceita um número variável de argumentos posicionais do tipo string e
# retorna uma única string que é a concatenação de todas as strings passadas como argumentos.
def concatenar_strings(*args):
    string_concatenada = ''
    for string in args:
        string_concatenada += string
    return string_concatenada
# print(concatenar_strings('M', 'á', 'r', 'c', 'i', 'o'))


# Escreva uma função chamada criar_dicionario que aceita um número variável de argumentos de palavras-chave e retorna um
# dicionário contendo todos os pares chave-valor passados como argumentos.
def criar_dicionario(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# criar_dicionario(Nome='Márcio Campos Júnior', Idade=18, Sexo='Masculino')


# Escreva uma função chamada media_notas que aceita um número variável de argumentos posicionais representando notas e
# retorna a média dessas notas.
def media_notas(*args):
    media = sum(args) / len(args)
    return media
# print(media_notas(10, 5, 9))


# Escreva uma função chamada contar_letras que aceita um número variável de argumentos de palavras-chave, onde as chaves
# são palavras e os valores são as letras a serem contadas. A função deve retornar um dicionário com a contagem de cada
# letra em cada palavra.
def contar_letras(**kwargs):
    for key, value in kwargs.items():
        print(f"A palavra {key} possui {key.count(value)} letras {value.upper()}")
# contar_letras(paralelepipedo='a', mansao_do_ronaldinho='o', so_pra_contrariar='r')


# Escreva uma função chamada filtrar_argumentos que aceita um número variável de argumentos de palavras-chave. A função
# deve retornar um dicionário contendo apenas os pares chave-valor onde a chave começa com a letra 'a'.
def filtrar_argumentos(**kwargs):
    for key, value in kwargs.items():
        if key[0].lower() == 'a':
            print(f"{key.title()}: {value.title()}")
# filtrar_argumentos(aurora='boreal')

cores = {"vermelho": '\033[0;31m',
         "verde": '\033[0;32m',
         "azul-claro": '\033[0;36m',
         "cinza": '\033[0;37m',
         "roxo": '\033[0;35m',
         "amarelo": '\033[0;33m',
         "termina": '\033[m'}


def leia_int(num):
    try:
        inteiro = int(input(num))
        if not inteiro:
            return leia_int(num)
    except ValueError:
        print('Erro, tipo de dado inserido é inválido!')
        return leia_int(num)
    except KeyboardInterrupt:
        return
    else:
        return inteiro


def verificar_db():
    try:
        with open('database.txt', 'r') as db:
            db.close()
        return 'DataBase já existe!'
    except FileNotFoundError:
        with open('database.txt', 'w') as db:
            db.close()
        return 'DataBase foi criado!'


def linha(tamanho=52):
    line = f'{cores["roxo"]}{"-" * tamanho}{cores["termina"]}'
    return line


def cabecalho(txt):
    print(linha())
    print(txt.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho(f'{cores["roxo"]}Menu Inicial{cores["termina"]}')
    indice = 1
    for item in lista:
        print(f'{cores["azul-claro"]}{indice} - {item}{cores["termina"]}')
        indice += 1
    print(linha())
    escolha = leia_int(f'{cores["amarelo"]}Escolha uma ação: {cores["termina"]}')
    return escolha


def ler_db():
    with open('database.txt', 'r') as db:
        db = db.read()
    return db

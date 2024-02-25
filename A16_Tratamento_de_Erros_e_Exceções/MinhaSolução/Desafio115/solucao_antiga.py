import time


def cadastro_com_db():
    cores = {"vermelho": '\033[0;31m',
             "verde": '\033[0;32m',
             "azul-claro": '\033[0;36m',
             "cinza": '\033[0;37m',
             "roxo": '\033[0;35m',
             "amarelo": '\033[0;33m',
             "termina": '\033[m'}

    try:
        with open('database.txt', 'r') as db:
            db = db
    except FileNotFoundError:
        with open('database.txt', 'w') as db:
            db = db

    def ver_database():
        with open('database.txt', 'r') as db:
            print(f"{cores['roxo']}{61 * '-'}")
            if len(db.read()) == 0:
                print(20 * ' ', 'Não possui Cadastros')
                print(61 * '-', cores["termina"])
                return cadastro_com_db()
            print(20 * ' ', 'Pessoas Cadastradas')
            print(61 * '-', cores["termina"])
        with open('database.txt', 'r') as db:
            for linha in db.readlines():
                linha = linha.strip()
                print(f"{cores['azul-claro']}{linha[:linha.find(';')]}".ljust(40),
                      f"{linha[linha.find(';') + 1:]} Anos{cores['termina']}")
        return cadastro_com_db()

    def cadastrar_pessoa():
        print(f"{cores['roxo']}{61 * '-'}")
        print(25 * ' ', 'CADASTRO')
        print(61 * '-', cores["termina"])
        nome = input(f'{cores["azul-claro"]}Digite seu nome: ')
        idade = input('Digite sua idade: ')
        with open('database.txt', 'a+') as db:
            # db.seek(0)
            database = db.read()
            # if nome != unidecode.unidecode(database):
            #     print('Acentos ou caractéres especiais não são permitidos, tente novamente.')
            #     return cadastrar_pessoa()
            if nome.lower() in database.lower():
                print(f'{cores["vermelho"]}Esse nome já existe, tente novamente.{cores["termina"]}')
                return cadastrar_pessoa()
            nome = nome.title()
            db.write(nome + ';' + idade + '\n')
            print(f'{cores["verde"]}{nome} foi cadastrado(a) com sucesso.{cores["termina"]}')
        return cadastro_com_db()

    # Escolha do usuário
    print(f"{cores['roxo']}{61 * '-'}")
    print(22 * ' ', 'Menu Principal')
    print(61 * '-', cores["termina"])
    choice = int(input(f'{cores["azul-claro"]}1 - Ver Tabela de Cadastro'
                       f'\n2 - Cadastrar Pessoa'
                       f'\n3 - Sair{cores["termina"]}'
                       f'\n{cores["roxo"]}{61 * "-"}{cores["termina"]}'
                       f'\n{cores["amarelo"]}Escolha uma ação: {cores["termina"]}'))

    if choice == 3:
        print()
        print(f'{cores["vermelho"]}Saindo', end='')
        for sec in range(0, 3):
            time.sleep(1)
            print('.', end='')
        print()
        return
    elif choice == 1:
        return ver_database()
    elif choice == 2:
        return cadastrar_pessoa()


cadastro_com_db()

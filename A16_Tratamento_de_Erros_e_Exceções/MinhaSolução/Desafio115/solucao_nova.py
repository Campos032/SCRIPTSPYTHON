# Ao assistir um trecho da primeira aula do desafio 115, percebi que talvez tenha cometido um erro em não fazer de forma
# modularizada, então decidi refatorar o código.
import time

from modulo import *


def cadastro_com_db():
    verificar_db()

    def ver_cadastrados():
        with open('database.txt', 'r') as db:
            quantidade = len(db.read())
            if quantidade == 0:
                cabecalho(f'{cores["amarelo"]}NÃO HÁ CADASTROS{cores["termina"]}')
                return cadastro_com_db()
            else:
                db.seek(0)
                cabecalho(f'{cores["roxo"]}Pessoas Cadastradas{cores["termina"]}')
                for pessoa in db.readlines():
                    pessoa = pessoa.strip()
                    print(f"{cores['azul-claro']}{pessoa[:pessoa.find(';')]}".ljust(40),
                          f"{pessoa[pessoa.find(';') + 1:]} Anos{cores['termina']}")
        return cadastro_com_db()

    def cadastrar_pessoa():
        cabecalho(f'{cores["roxo"]}Cadastro{cores["termina"]}')
        nome = input(f'{cores["azul-claro"]}Digite o nome: {cores["termina"]}')
        while nome.lower() in ler_db().lower():
            print(f'{cores["vermelho"]}Esse nome já existe, tente novamente.{cores["termina"]}')
            nome = input(f'{cores["azul-claro"]}Digite o nome: {cores["termina"]}')
        idade = leia_int(f'{cores["azul-claro"]}Digite a idade: {cores["termina"]}')
        with open('database.txt', 'a+') as db:
            nome = nome.title().strip()
            db.write(nome + ';' + f'{idade}' + '\n')
            print(f'{cores["verde"]}{nome} foi cadastrado(a) com sucesso.{cores["termina"]}')
        return cadastro_com_db()

    escolha = menu(['Ver Tabela De Cadastro', 'Cadastrar Pessoa', 'Sair do Sistema'])

    if escolha == 3:
        print()
        print(f'{cores["vermelho"]}Saindo', end='')
        for sec in range(0, 3):
            time.sleep(1)
            print('.', end='')
        print()
        return
    elif escolha == 1:
        return ver_cadastrados()
    elif escolha == 2:
        return cadastrar_pessoa()


cadastro_com_db()

# Desafio 90 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela, aprovado se média acima de 7
from datetime import datetime
from random import randint


# Solução Comentários
def solucao_comentario():
    aluno = {'nome': str(input('Nome: '))}
    aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
    aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] < 6 else 'recuperação'
    for key, value in aluno.items():
        print(f'{key}:', value)


def solucao_comentario2():
    aluno = {'nome': str(input('Nome: ')), 'média': float(input('Digite a média:'))}
    aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] < 6 else 'recuperação'
    for key, value in aluno.items():
        print(f'{key}:', value)


# Solução do Vídeo
def aluno_aprovacao_video():
    aluno = dict()
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situação'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['situação'] = 'Reprovado'
    for key, valor in aluno.items():
        print(f'{key} é igual a {valor}')


# Minha Solução
def aluno_aprovacao():
    aluno = {'nome': str(input('Escreva o nome do aluno: ')), 'media': float(input('Digite a nota média do aluno: '))}
    print(f'Nome Aluno - {aluno["nome"]}\nNota Média - {aluno["media"]}')
    # print(f'Média - {aluno["media"]}')
    if aluno['media'] >= 7:
        aluno['situacao'] = 'Aprovado'
        print(f'Situação - {aluno["situacao"]}!')
    elif 7 > aluno['media'] >= 5:
        aluno['situacao'] = 'Recuperação'
        print(f'Situação - {aluno["situacao"]}!')
    else:
        aluno['situacao'] = 'Reprovado'
        print(f'Situação - {aluno["situacao"]}!')


# Desafio 91 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
def jogo_dado():
    jogadas = dict()
    listajogadas = list()
    ordem = list()
    for jogada in range(1, 5):
        jogador = jogadas[f"jogador{jogada}"] = int(randint(1, 6))
        print(f'O jogador{jogada} tirou {jogador} no dado.')
        listajogadas.append(jogadas.copy())
        jogadas.clear()
    numerojogador = 1
    jogador_no_zero = ''
    for indice, valor in enumerate(listajogadas):
        if not ordem or listajogadas[indice][f"jogador{numerojogador}"] > ordem[0]:
            ordem.insert(0, listajogadas[indice])
            numerojogador += 1
        else:
            pos = 0
            while pos < len(ordem):
                if listajogadas[indice][f"jogador{numerojogador}"] <= ordem[pos]:
                    ordem.insert(pos, listajogadas[indice][f"jogador{numerojogador}"])
                    numerojogador += 1
                    break
                pos += 1
    print(ordem)
    # for jogador, valor in jogadas.items():
    #     if valor == 1 or valor > maior_valor[-1]:
    #         ordem.insert(0, jogador)
    #     else:
    #         posicao = 0
    #         while posicao < len(jogadas):
    #             for numero in maior_valor:
    #                 if valor >= numero:
    #                     ordem.insert(ordem.index(numero) - 1, jogador)
    #                 posicao += 1
    # while len(ordem) < len(jogadas):
    #     pos_jogador = 1
    #     for jogador in jogadas:
    #         if jogadas[f"jogador{pos_jogador}"] > maior_valor[0]:
    #             ordem.insert(0, jogador)
    #             pos_jogador += 1
    #         else:
    #             pos = 0
    #             while pos < len(jogadas):
    #                 if jogadas[f"jogador{pos_jogador}"] <= ordem[pos][1]:
    #                     ordem.insert(pos-1, jogador)
    #                     break
    #                 pos += 1


# Desafio 92 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um
# Dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

def cadastro_pessoa():
    cadastro = dict()
    cadastro['nome'] = str(input('Digite seu nome conforme seu CPF: '))
    cadastro['ano_de_nascimento'] = int(input('Digite seu ano de nascimento conforme seu CPF:'))
    cadastro['ctps'] = int(input('Se você possuir Carteira de Trabalho informe senão digite 0: '))
    if cadastro['ctps'] != 0:
        cadastro['ano_contratacao'] = int(input('Informe o seu ano de contratação: '))
        cadastro['salario'] = float(input(f'Informe seu salário: '))

        ano_atual = datetime.now().year
        idade_minima = 65
        tempo_contribuicao_minimo = 35

        idade = ano_atual - cadastro['ano_de_nascimento']
        tempo_contribuicao = ano_atual - cadastro['ano_contratacao']

        if idade >= idade_minima and tempo_contribuicao >= tempo_contribuicao_minimo:
            print(f'{cadastro["nome"]} está apto a se aposentar.')
            cadastro['idade_aposentadoria'] = idade
        else:
            if idade + tempo_contribuicao_minimo <= 65:
                cadastro['idade_aposentadoria'] = 65
            else:
                cadastro['idade_aposentadoria'] = idade + tempo_contribuicao
        for key, valor in cadastro.items():
            if key == 'salario':
                print(f'{key.capitalize()} = R${valor:.2f}')
            else:
                print(f'{key.capitalize()} = {valor}')


# Desafio 93 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

def jogador_futebol():
    cadastro_jogador = dict()
    cadastro_jogador['nome_jogador'] = str(input('Escreva o nome do jogador: '))
    cadastro_jogador['numero_partidas'] = int(input('Informe o número de partidas do jogador: '))
    cadastro_jogador['total_gols'] = 0
    for partida in range(1, cadastro_jogador['numero_partidas'] + 1):
        cadastro_jogador['total_gols'] += int(input(f'Informe o número de gols do jogador na {partida}° partida: '))
    cadastro_jogador['media_gols'] = cadastro_jogador['total_gols'] / cadastro_jogador['numero_partidas']
    for key, valor in cadastro_jogador.items():
        print(f'{key.capitalize()} - {valor}')


def jogador_futebol2():
    cadastro_jogador = dict()
    cadastro_jogador['nome_jogador'] = str(input('Escreva o nome do jogador: '))
    cadastro_jogador['numero_partidas'] = int(input('Informe o número de partidas do jogador: '))
    cadastro_jogador['gol_cada_partida'] = []
    for partida in range(1, cadastro_jogador['numero_partidas'] + 1):
        cadastro_jogador['gol_cada_partida'].append(int(input(f'Informe o número de gols do jogador na {partida}° '
                                                              f'partida: ')))
    cadastro_jogador['media_gols'] = sum(cadastro_jogador['gol_cada_partida']) / cadastro_jogador['numero_partidas']
    cadastro_jogador['total_gol'] = sum(cadastro_jogador['gol_cada_partida'])
    for key, valor in cadastro_jogador.items():
        if key == 'gol_cada_partida':
            for indice, value in enumerate(cadastro_jogador['gol_cada_partida']):
                print(f'Na {indice + 1}° partida, fez {value} gol(s).')
        else:
            print(f'{key.capitalize()} - {valor}')


# Desafio 94 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre: A - Quantas pessoas foram cadastradas. B - A média
# de idade do grupo C - Uma lista com todas as mulheres D - Uma lista com todas as pessoas com idade acima da média.

def cadastro_pessoas():
    pessoas_lista = list()
    while True:
        pessoa = dict()
        pessoa['nome'] = str(input('Digite  seu nome: '))
        pessoa['idade'] = int(input('Digite sua idade: '))
        pessoa['sexo'] = int(input('1 - Masculino  /  2 - Feminino: '))
        pessoas_lista.append(pessoa.copy())
        pessoa.clear()

        choice = int(input('1 - Continuar  /  2 - Sair: '))
        if choice == 2:
            qnt_pessoas = len(pessoas_lista)
            idade_lista = list()
            for pessoa in pessoas_lista:
                idade_lista.append(pessoa['idade'])
            idade_media = sum(idade_lista) / qnt_pessoas
            mulheres = list()
            pessoas_acima_media = list()
            for pessoa in pessoas_lista:
                if pessoa['sexo'] == 2:
                    mulheres.append(pessoa['nome'])
                if pessoa['idade'] > idade_media:
                    pessoas_acima_media.append(pessoa['nome'])
            print(f'Foram cadastradas {qnt_pessoas} pessoas.')
            print(f'A média de idade do grupo é {idade_media} anos.')
            print(f'As mulheres cadastradas são {mulheres}.')
            print(f'As pessoas com idade acima da média são {pessoas_acima_media}.')
            break

        elif choice == 1:
            continue


# Desafio 95 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador

def novetres_aprimorado():
    lista_jogadores = list()
    while True:
        cadastro_jogador = dict()
        cadastro_jogador['nome_jogador'] = str(input('Escreva o nome do jogador: '))
        cadastro_jogador['numero_partidas'] = int(input('Informe o número de partidas do jogador: '))
        cadastro_jogador['total_gols'] = 0
        cadastro_jogador['gol'] = list()
        for partida in range(1, cadastro_jogador['numero_partidas'] + 1):
            cadastro_jogador['total_gols'] += int(input(f'Informe o número de gols do jogador na {partida}° partida: '))
        cadastro_jogador['media_gols'] = cadastro_jogador['total_gols'] / cadastro_jogador['numero_partidas']
        lista_jogadores.append(cadastro_jogador.copy())
        cadastro_jogador.clear()

        choice = int(input('1 - Parar Cadastro  /  2 - Continuar: '))
        if choice == 1:
            print()
            while True:
                print('Jogadores: ', end='')
                for pessoa in lista_jogadores:
                    print(f' {pessoa["nome_jogador"]}', end=' ')
                print()
                detalhes_ou_nao = int(input('1 - Ver detalhes  /  2 - Sair: '))
                if detalhes_ou_nao == 1:
                    qual_jogador = str(input('Escreva o nome do jogador: '))
                    for pessoa in lista_jogadores:
                        if pessoa['nome_jogador'] == qual_jogador:
                            hat_trick = 0
                            print(f'{qual_jogador} jogou {pessoa["numero_partidas"]} jogos  e fez '
                                  f'{pessoa["total_gols"]} gols.')
                            for partida, gol in enumerate(pessoa['gol']):
                                print(f'Fez {gol} na Partida{partida + 1}.')
                                if gol == 3:
                                    hat_trick += 1
                            print(f'A média de gols do jogador {qual_jogador} foi {pessoa["media_gols"]:.2f} gols.')
                            if hat_trick > 0:
                                print(f'E fez {hat_trick} hat tricks.')
                            print()
                elif detalhes_ou_nao == 2:
                    print()
                    print('Finalizando Programa de Cadastro...')
                    print(9 * ' ', 'VOLTE SEMPRE!')
                    break
        elif choice == 2:
            continue

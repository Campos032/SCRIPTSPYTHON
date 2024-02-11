# Desafio 101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
#  de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional 
# ou Obrigatório nas eleições
from datetime import datetime


def voto_g():
    def voto(ano_nascimento):
        hoje = datetime.now().year
        idade = hoje - ano_nascimento
        if idade < 15:
            return f'{idade} anos - Voto negado.'
        elif 15 <= idade <= 17 or idade > 70:
            return f'{idade} anos - Voto Opcional.'
        else:
            return f'{idade} anos - Voto obrigatório.'

    ano_de_nascimento = int(input('Informe seu ano de nascimento: '))
    situacao_eleitoral = voto(ano_de_nascimento)
    print(situacao_eleitoral)


# Desafio 102 Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
# número a calcular e o outro chamado show, que será o valor lógico(opcional) indicando se será mostrado ou não na
# tela o processo de cálculo de fatorial.

def fatorial_g():
    def fatorial(numero, mostrar=1):
        resultado = 1
        for i in range(1, numero + 1):
            if mostrar == 1:
                print(f'{resultado} x {i} = {resultado * i}')
                resultado *= i
            else:
                resultado *= i
        return resultado

    num = int(input('Digite um número para calcular seu fatorial: '))
    show_calculo = int(input('Para mostrar os cálculos digite 1: '))
    print(f'O fatorial de {num} é', fatorial(num, show_calculo))


# Desafio 103 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
# jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não 
# tenha sido informado corretamente. 

def ficha_g():
    def ficha(nome='<desconhecido>', gols=0):
        print(f'Nome jogador - {nome}'
              f'\nQuantidade de gols - {gols}')

    name = input('Digite o nome do jogador: ')
    goals = int(input('Digite o número de gols: '))
    ficha(name, goals)


# Desafio 104 Crie um programa qie tenha uma função leiaInt() que vai funcionar de forma semelhante á função input()
# do Python só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um Número: ')
def leia_int_g():
    def leia_int(num):
        inteiro = input(num)
        while not inteiro.isdigit():
            print('Erro, insira um valor valido!')
            inteiro = input(num)
        else:
            return int(inteiro)

    numero_inteiro = leia_int('Digite um número: ')
    print(numero_inteiro, 'É um número inteiro!')


# Desafio 105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações: - Quantidade de notas - A maior nota - A menor nota - A média da turma
# - A situação, Adicione também as docstrings da função
def notas_g():
    def notas(numero_cadastros):
        cadastro_alunos = list()
        cadastro_temporario = dict()
        for aluno in range(1, numero_cadastros + 1):
            print(f'Cadastro Aluno{aluno}')
            cadastro_temporario['nome'] = str(input('Escreva o nome do aluno: '))
            cadastro_temporario['nota1'] = float(input('Digite a nota1: '))
            cadastro_temporario['nota2'] = float(input('Digite a nota2: '))
            cadastro_alunos.append(cadastro_temporario.copy())
            cadastro_temporario.clear()
        print(f'Foram cadastradas {numero_cadastros * 2} notas')
        maior_nota = 0
        menor_nota = 999
        total_notas = 0
        for indice, cadastro in enumerate(cadastro_alunos):
            total_notas += cadastro_alunos[indice]['nota1']
            total_notas += cadastro_alunos[indice]['nota2']
            if cadastro_alunos[indice]['nota1'] >= maior_nota:
                maior_nota = cadastro_alunos[indice]['nota1']
            if cadastro_alunos[indice]['nota2'] >= maior_nota:
                maior_nota = cadastro_alunos[indice]['nota2']
            if cadastro_alunos[indice]['nota1'] <= menor_nota:
                maior_nota = cadastro_alunos[indice]['nota1']
            if cadastro_alunos[indice]['nota2'] <= menor_nota:
                maior_nota = cadastro_alunos[indice]['nota2']


print(10 * ' ', 'Cadastro De Alunos')
numero_de_cadastros = int(input('Informe o número de alunos a ser cadastrado: '))

# Desafio 106 Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar a palavra 'Fim',
# o programa se encerrará. OBS: Use cores

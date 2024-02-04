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
    def ficha(nome=None, gols=None):
        print(f'Nome jogador - {nome}'
              f'\nQuantidade de gols - {gols}')

    name = input('Digite o nome do jogador: ')
    goals = int(input('Digite o número de gols: '))
    ficha(name, goals)


ficha_g()

# Desafio 104 Crie um programa qie tenha uma função leiaInt() que vai funcionar de forma semelhante á função input()
# do Python só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um Número: ')

# Desafio 105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações: - Quantidade de notas - A maior nota - A menor nota - A média da turma
# - A situação Adicione também as docstrings da função

# Desafio 106 Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar a palavra 'Fim',
# o programa se encerrará. OBS: Use cores

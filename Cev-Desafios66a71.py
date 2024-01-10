import random
import time

# Desafio 66 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar 999, que dá a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles

"""print('Números Aleatórios - Soma e Quantidade')
qnt_num = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    qnt_num += 1
    soma += num
print(f'{qnt_num} números foram inseridos!\nE a soma entre eles é igual a {soma}!')"""

# Desafio 67 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado for negativo

"""while True:
    print(7 * '->')
    print('Tabuada')
    print(7 * '->')
    num = int(input('Digite um número: '))
    for i in range(0, 11):
        tab = num * i
        print(f'{num} x {i} = {tab}')"""


# Desafio 68 Faça um programa que jogue ímpar ou par com o computador. O jogo será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que el conquistou no final do jogo.


def jogo_do_impar_ou_par():
    qnt_vitoria = 0
    print(25 * ' ', 'Jogo do Ímpar ou Par')
    print()
    while True:
        print('Sou seu computador e irei pensar em um número... tente adivinhar se é ímpar ou par!')
        time.sleep(1)
        num_pc = random.randint(0, 1000)
        par_ou_impar = num_pc % 2
        choice = str(input('Digite P(par) e I(impar): ')).strip().upper()

        if choice not in 'PI':
            print('Escolha inválida, tente novamente!')
            choice = str(input('Digite P(par) e I(impar): ')).strip().upper()

        if par_ou_impar == 0 and choice == 'P':
            qnt_vitoria += 1
            print(f'Você acertou, eu escolhi {num_pc}.')
            print()

        elif par_ou_impar != 0 and choice == 'I':
            qnt_vitoria += 1
            print(f'Você acertou, eu escolhi {num_pc}.')
            print()

        else:
            print(f'Você errou, e teve {qnt_vitoria} vitórias consecutivas!')
            break


# Desafio 69 Crie um programa que leia a idade de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre: A - Quantas pessoas tem mais de 18 anos / B - Quantos homens
# foram cadastrados / C - Quantas mulheres tem menos de 20 anos

def cadastro():
    qnt_pessoas = 0
    mulher_20 = 0
    homem = 0
    print('Cadastro de Pessoas')
    while True:
        sexo = str(input('Digite [M/F]: ')).upper().strip()
        idade = int(input('Digite a idade da pessoa: '))

        if sexo not in 'MF':
            print('Sexo inválido, tente novamente!')
            sexo = str(input('Digite [M/F]: ')).upper().strip()

        if idade == ValueError:
            print('Idade inválida, tente novamente!')

        if sexo == 'F' and idade < 20:
            mulher_20 += 1
            qnt_pessoas += 1

        elif idade >= 18 and sexo == 'M':
            homem += 1
            qnt_pessoas += 1

        elif idade > 18:
            qnt_pessoas += 1

        sair = int(input('1-SAIR  2-CONTINUAR: '))

        if sair == 1:
            print()
            print(f'{qnt_pessoas} pessoas tem mais de 18 anos!\n{homem} pessoas são homens!'
                  f'\n{mulher_20} mulher(es) tem menos de 20 anos!')
            print()
            time.sleep(3)
            print('Saindo!')
            time.sleep(1)
            break


# Desafio 70 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre: A-Qual é o total gasto na compra / B-Quantos produtos custam mais de R$1000 / C-Qual é o
# nome do produto mais barato


def produto():
    qnt_produtos_1000 = 0
    total = 0
    barato = 9999999
    nome_barato = ''
    print('Cadastro de Produtos')
    while True:
        nome = str(input('Digite o nome do produto:'))
        preco = float(input('Digite o valor do produto:'))

        total += preco

        if preco < barato:
            nome_barato = nome

        if preco > 1000:
            qnt_produtos_1000 += 1

        choice = int(input('1-SAIR  2-CONTINUAR: '))

        if choice == 1:
            print(f'O total gasto na compra foi de R${total:.2f}!\n{qnt_produtos_1000} produto(s) custam mais de mil '
                  f'reais!\n{nome_barato} é o produto mais barato!')
            break

        if choice == 2:
            continue


# Desafio 71 Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será
# o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

def caixa_eletronico():
    while True:
        print(2 * ' ', 'Caixa Eletrônico')
        saque = int(input('Digite o valor do saque:'))
        qnt_notas_50 = saque // 50
        qnt_notas_20 = (saque - (qnt_notas_50 * 50)) // 20
        qnt_notas_10 = (saque - (qnt_notas_50 * 50) - (qnt_notas_20 * 20)) // 10
        qnt_notas_1 = (saque - (qnt_notas_50 * 50) - (qnt_notas_20 * 20) - (qnt_notas_10 * 10)) // 1
        print(f'Você receberá {qnt_notas_50} notas de R$50.\n{qnt_notas_20} notas de R$20.'
              f'\n{qnt_notas_10} notas de R$10.\nE {qnt_notas_1} notas de R$1.')
        print()


def caixa_eletronico2():
    print('Caixa Eletrônico')
    saque = int(input('Digite o valor a ser sacado: '))
    qnt_notas50 = 0
    qnt_notas20 = 0
    qnt_notas10 = 0
    qnt_notas1 = 0
    while saque > 0:
        if saque >= 50:
            saque -= 50
            qnt_notas50 += 1

        elif saque >= 20:
            saque -= 20
            qnt_notas20 += 1

        elif saque >= 10:
            saque -= 10
            qnt_notas10 += 1

        elif saque >= 1:
            saque -= 1
            qnt_notas1 += 1

    print(f'Voce receberá {qnt_notas50} nota(s) de R$50.\n{qnt_notas20} nota(s) de R$20.\n{qnt_notas10}'
          f' nota(s) de R$ 10\nE {qnt_notas1} nota(s) de R$1.')


def solucao_video():
    print(30 * '=')
    print(f'{"Banco CEV":^30}')  # Só funciona com o uso de aspas duplas e simples ou vice versa
    print(30 * '=')
    valor = int(input('Qual valor você quer sacar? R$'))
    total = valor
    ced = 50
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if total == 0:
                break
    print(30 * '=')
    print('Volte sempre ao Banco CEV! Tenha um bom dia!')

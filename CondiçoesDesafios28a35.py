# Operadores de condição em python (==)verifica igualdade. Retorna True se os operandos forem iguais.
# x == y # True se x for igual a y
# !=: verifica desigualdade. Retorna True se os operandos não forem iguais.
# x != y # True se x for diferente de y
# <: verifica se o operando esquerdo é menor que o operando direito.
# x < y # True se x for menor que y
# <=: verifica se o operando esquerdo é menor ou igual ao operando direito.
# x <= y # True se x for menor ou igual a y
# >: verifica se o operando esquerdo é maior que o operando direito.
# x > y # True se x for maior que y
# >=: verifica se o operando esquerdo é maior ou igual ao operando direito.
# x >= y # True se x for maior ou igual a y
# in: verifica se um elemento está presente em uma sequência (como uma lista, tupla, conjunto ou string).
# x in lista # True se x estiver na lista
# Not in: verifica se um elemento não está presente em uma sequência.
# x not in lista # True se x não estiver na lista
# is: Verifica se dois objetos têm a mesma identidade (referem-se ao mesmo objeto na memória).
# x is y # True se x e y referirem-se ao mesmo objeto
# is not: verifica se dois objetos não têm a mesma identidade.
# x is not y # True se x e y não referirem-se ao mesmo objeto
# if(se) if x < y print(x é menor que y)
# elif ou else if(se naõ for tente) elif x > z print(x é maior que z)
# else(senão) else x > z print(x não é maior que z)


cores = {"branco": '\033[0;30m',
         "vermelho": '\033[0;31m',
         "verde": '\033[0;32m',
         "amarelo": '\033[0;33m',
         "azul": '\033[34m',
         "roxo": '\033[0;35m',
         "azulclaro": '\033[0;36m',
         "cinza": '\033[0;37m',
         "fundobranco": '\033[0;40m',
         "fundovermelho": '\033[0;41m',
         "fundoverde": '\033[0;42m',
         "fundoamarelo": '\033[0;43m',
         "fundoazul": '\033[0;44m',
         "fundoroxo": '\033[0;45m',
         "fundoazulclaro": '\033[0;46m',
         "fundocinza": '\033[0;47m',
         "termina": '\033[m',
         "pretoebranco": '\033[7;30m'}


# Desafio28 Escreva um programa que faça o computador escolher um número inteiro de 0 a 5, e peça pro usuário tentar
# Adivinhar, e o programe escreva na tela se o usuário acertou ou não
import random
import time
import datetime



def adivinha_num():
    print('')
    print('Jogo de adivinha números')
    num_aleatorio = random.randint(0, 5)
    num = int(input('O computador irá escolher um número de 0 a 5 e você deve tentar adivinhar,digite um número:'))

    if num == num_aleatorio:
        time.sleep(0.5)
        print('Vôce Acertou!')
        print('-' * 30)

    else:
        time.sleep(0.5)
        print('Você errou,Tente novamente!')
        print('O número era:', num_aleatorio, "!")
        print('-' * 30)

    # elif num != (0, 5): ou if num is None:
    # print('Erro, número inválido!')
    # print('-' * 30)


# Desafio29 Escreva um programa que leia a velocidade de um carro e se ultrapassar 80km/h, mostre uma mensagem dizendo
# Que ele foi multado, a multa vai custar R$7 por cada km acima do limite


def multa():
    print('')
    print('Radar Eletrônico')
    velo = int(input('Digite a velocidade do carro em Km para saber se foi multado ou não:'))

    if velo > 80:
        print(f'Você foi multado em R${(velo - 80) * 7}!')
        print('')

    else:
        print('Você estava dentro do limite da via e não foi multado!')
        print('')


# Desafio30 Crie um programa que leia um número inteiro e diga se ele é par ou ímpar

def par_ou_impar():
    print('')
    print('Verificar se número inteiro é par ou impar')
    num = int(input('Digite um número inteiro:'))

    if num % 2 == 0:
        print('O número que você digitou é par!')

    else:
        print('O número que você digitou é ímpar!')


# Desafio31 Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando
# R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

def valor_passagem():
    print('')
    print('Calculador de preço da passagem')
    print('')
    dist = int(input('Digite a distância da viagem em Km:'))
    print('')

    if dist <= 200:
        print(f'O valor da passagem é R${dist * 0.5}!')

    else:
        print(f'O valor da passagem é R${dist * 0.45}!')


# Desafio32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

def bissexto():
    print('')
    print('Verificador de ano bissexto')
    print('')
    ano = int(input('Se você quer verificar o ano atual digite -1 ou Digite o ano que você deseja verificar:'))

    if ano == -1:
        ano = datetime.date.today().year  # Vai pegar a data de hoje no pc apenas o ano

    if ano % 100 == 0 and not ano % 400 == 0:  # Aqui eu também usei if, para quebrar a condição anterior e usar a
        # nova variável
        print(f'O ano de {ano} não é bissexto!')

    elif ano % 400 == 0 and ano % 100 == 0:
        print(f'O ano de {ano} é bissexto!')

    elif ano % 4 == 0:
        print(f'O ano {ano} é bissexto!')

    else:
        print(f'O ano {ano} não é bissexto!')


# Desafio33 Faça um programa que leia três números e diga qual o maior, qual o menor e qual fica no meio
# o método sort() modifica uma lista existente a ordenando de maneira crescente
# para fazer de forma decrescente usa sort(lista, reverse=True) ou lista.sort(reverse=True)
# ou lista.sort(lista, reverse=True)
def maior_menor():
    print('')
    print('Verificar começo, meio e final')
    print('')
    n = str(input('Digite três números separando os por vírgula:')).strip()
    ns = n.split(',')

    if ns[0] < ns[1] < ns[2]:
        print(ns[0], ns[1], ns[2])

    elif ns[0] > ns[1] > ns[2]:
        print(ns[2], ns[1], ns[0])

    elif ns[0] > ns[1] < ns[2]:
        print(ns[1], ns[0], ns[2])

    elif ns[0] < ns[1] > ns[2]:
        print(ns[2], ns[0], ns[1])

    elif ns[0] == ns[1] and ns[1] < ns[2]:
        print(ns[0], ns[1], ns[2])

    elif ns[0] == ns[1] and ns[1] > ns[2]:
        print(ns[2], ns[0], ns[1])

    elif ns[0] == ns[2] and ns[1] < ns[2]:
        print(ns[1], ns[0], ns[2])

    elif ns[0] == ns[2] and ns[1] > ns[2]:
        print(ns[0], ns[2], ns[1])

    else:
        print(ns[0], ns[2], ns[1])


# Desafio34 Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250 calcule um aumento de 10% Para inferiores ou iguais o aumento é de 15%

def salario():
    print('')
    print('Cálculo do Reajuste Salarial')
    print('')
    s = float(input('Digite seu salário:'))

    if s <= 1250:
        print(f'O seu salário será:R${s * 15 / 100 + s :.2f}')

    else:
        print(f'O seu salário será:R${s * 10 / 100 + s :.2f}')


# Desafio35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar
# Um triângulo

def triangulo():
    print('')
    print('Formando ou não um Triângulo')
    print('')
    r1 = float(input('Digite o comprimento da primeira reta:'))
    r2 = float(input('Digite o comprimento da segunda reta:'))
    r3 = float(input('Digite o comprimento da terceira reta:'))

    if r1 and r2 < r3 < r1 + r2:
        print('')
        print('É possível formar um triângulo!')

    else:
        print('')
        print('Não é possível formar um triângulo!')

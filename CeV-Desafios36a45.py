from datetime import datetime
import time
import random

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


# Desafio36 escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
# O valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo
# Que ela não pode exceder 30% do salário ou então o empréstimo será negado


def emprestimo():
    print(f'{cores["roxo"]}-={cores["termina"]}' * 26)
    print(f'{cores["amarelo"]}Calculador de Empréstimo  Para a Compra de uma Casa{cores["termina"]}')
    print(f'{cores["roxo"]}-={cores["termina"]}' * 26)
    escolha = int(input(f'{cores["amarelo"]}Digite 1 - Calcular empréstimo 2- Sair{cores["termina"]}'))

    if escolha == 2:
        print('')
        print(f'{cores["vermelho"]}Saindo!{cores["termina"]}')
        time.sleep(1)
        return

    casa = float(input(f'{cores["azulclaro"]}Digite o valor da casa:{cores["termina"]}'))
    salario = float(input(f'{cores["azulclaro"]}Digite o valor do seu salário:{cores["termina"]}'))
    anos = float(input(f'{cores["azulclaro"]}Digite em quantos anos será o pagamento:{cores["termina"]}')) * 12
    parcela = casa / anos
    print('')

    if parcela > salario + salario * 30 / 100:
        time.sleep(1)
        print(f'{cores["vermelho"]}O empréstimo não foi aprovado!{cores["termina"]}')
        print('')

    else:
        time.sleep(1)
        print(f'{cores["verde"]}O empréstimo foi aprovado!{cores["termina"]}')
        print('')


# Desafio37 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# Conversão. 1-ParaBinário 2-ParaOctal 3-ParaHexadecimal

def conversor():
    print(f'{cores["vermelho"]}-{cores["termina"]}' * 63)
    print(f'{cores["amarelo"]}Conversor de número inteiro para Binário, Octal ou Hexadecimal{cores["termina"]}')
    print(f'{cores["vermelho"]}-{cores["termina"]}' * 63)
    escolha = int(
        input(f'{cores["azulclaro"]}Digite 1 para Binário - 2 Octal - 3 Hexadecimal - 4 sair:{cores["termina"]}'))

    if escolha == 4:
        time.sleep(0.5)
        print('')
        print(f'{cores["vermelho"]}Saindo!{cores["termina"]}')
        time.sleep(1)
        return

    inteiro = int(input(f'{cores["azulclaro"]}Digite um número inteiro:{cores["termina"]}'))

    if escolha == 1:
        print('')
        print(f'{cores["amarelo"]}Em Bínário o número equivale a:{bin(inteiro)[2:]}{cores["termina"]}')
        print('')
        return conversor()

    elif escolha == 2:
        print('')
        print(f'{cores["roxo"]}Em Octal o número equivale a:{oct(inteiro)[2:]}{cores["termina"]}')
        print('')
        return conversor()

    elif escolha == 3:
        print('')
        print(f'{cores["verde"]}Em hexadecimal o número equivale a:{hex(inteiro)[2:]}{cores["termina"]}')
        print('')
        return conversor()


# def conversor2():

# Desafio38 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
# O primeiro valor é maior - O segundo valor é maior - Não existe valor maior, os dois são iguais

def qualmaior():
    print('')
    print(f'{cores["azulclaro"]}Verificar qual número maior e qual menor!{cores["termina"]}')
    print('')
    escolha = int(input('1-Verificar  2-Sair:'))

    if escolha == 2:
        print('')
        time.sleep(0.75)
        print(f'{cores["vermelho"]}Saindo!{cores["termina"]}')
        time.sleep(1.5)
        return

    print('')
    num1 = int(input(f'{cores["amarelo"]}Digite um número:{cores["termina"]}'))
    num2 = int(input(f'{cores["roxo"]}Digite outro número:{cores["termina"]}'))
    num3 = int(input(f'{cores["vermelho"]}Digite mais um número:{cores["termina"]}'))

    if num1 > num2 and num1 > num3:
        print('')
        print(f'{cores["amarelo"]}O primeiro número é o maior!{cores["termina"]}')
        return qualmaior()

    elif num3 > num1 and num3 > num2:
        print('')
        print(f'{cores["vermelho"]}O terceiro número é o maior!{cores["termina"]}')
        return qualmaior()

    elif num2 > num1 and num2 > num3:
        print('')
        print(f'{cores["roxo"]}O segundo número é o maior!{cores["termina"]}')
        return qualmaior()

    elif num1 == num2 == num3:
        print('')
        print(f'{cores["azul"]}Os números são iguais!{cores["termina"]}')
        return qualmaior()

    elif num1 == num2 and num1 < num3:
        print('')
        print(f'{cores["vermelho"]}O terceiro número é o maior!{cores["termina"]}')
        return qualmaior()

    elif num2 == num3 and num1 > num2:
        print('')
        print(f'{cores["amarelo"]}O primeiro número é o maior!{cores["termina"]}')
        return qualmaior()

    elif num1 == num3 and num1 < num2:
        print('')
        print(f'{cores["roxo"]}O segundo número é o maior!{cores["termina"]}')
        return qualmaior()


# Desafio39 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
# Se ele ainda vai se alistar ao serviço militar - Se é a hora de se alistar - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar quanto tempo falta ou que passou do prazo

def alistar():
    print('')
    print(13 * ' ', f'{cores["verde"]}Verificador de Alistamento Militar{cores["termina"]}')
    print('')
    datastr = input(f'{cores["azulclaro"]}Informe sua data de nascimento no seguinte formato (DD-MM-YYYY):'
                    f'{cores["termina"]}')

    datahj = datetime.now()

    try:
        data = datetime.strptime(datastr, '%d-%m-%Y')

    except ValueError:
        print(f'{cores["vermelho"]}Formato Inválido, Tente novamente!{cores["termina"]}')
        return alistar()

    if data > datahj:
        print(f'{cores["vermelho"]}Data de nascimento inválida, Tente novamente!{cores["termina"]}')
        return alistar()

    anos18 = data.replace(year=data.year + 18)
    diasfaltam = datahj - anos18

    if diasfaltam.days < 0:
        diasfaltamstr = str(diasfaltam.days)
        diasfaltam = diasfaltamstr.replace('-', ' ')

    if datahj.year - data.year >= 18:
        print()
        print(
            f'{cores["verde"]}Você está apto para o alistamento militar há {diasfaltam} dias,procure a junta'
            f' de serviço militar mais próxima'
            f' ou para mais informações acessar o site alistamento.eb.mil.br{cores["termina"]}')

    elif datahj.year - data.year < 18:
        print()
        print(f'{cores["amarelo"]}Faltam {diasfaltam} dias para você ficar apto ao alistamento militar, '
              f'para mais informações acessar o site alistamento.eb.mil.br{cores["termina"]}')


# Desafio40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# De acordo, com a média atingida: Média abaixo de 5 = Reprovado - Média entre 5 e 6,9 = Recuperação
# Média 7 ou superior = Aprovado

def aprovacao():
    print()
    print(f'{cores["roxo"]}Aprovação/Desaprovação{cores["termina"]}')
    print()
    nota1 = float(input(f'{cores["azulclaro"]}Digite a primeira nota:{cores["termina"]}'))
    nota2 = float(input(f'{cores["azulclaro"]}Digite a segunda nota:{cores["termina"]}'))

    if (nota1 + nota2) / 2 < 5:
        print('')
        print(f'{cores["vermelho"]}Você não atingiu a meta necessária e foi reprovado!{cores["termina"]}')

    elif (nota1 + nota2) / 2 >= 5 < 7:
        print('')
        print(f'{cores["amarelo"]}Você não atingiu a média necessária e deverá fazer a recuperação!{cores["termina"]}')

    elif (nota1 + nota2) / 2 > 7:
        print('')
        print(f'{cores["verde"]}Parabéns, você foi aprovado!{cores["termina"]}')


# Desafio41 A Confederação Nacional de Natação, precisa de um programa que leia o ano de nascimento de um atleta e
# Mostre sua categoria, de acordo, com a idade: Até 9 anos = Mirim: Até 14 anos = Infantil: Até 19 anos = Júnior
# Até 20 anos = Sênior: Acima = Master

def categoria():
    print()
    print(15 * ' ', f'{cores["roxo"]}Categoria Atleta de Natação{cores["termina"]}')
    print()
    idadeatleta = input(f'{cores["azulclaro"]}Informe sua data de nascimento no seguinte formato (DD-MM-YYYY):'
                        f'{cores["termina"]}')

    datahj = datetime.now()

    try:
        idade = datetime.strptime(idadeatleta, '%d-%m-%Y')

    except ValueError:
        print()
        print(f'{cores["vermelho"]}Formato de data inválido, tente novamente!{cores["termina"]}')
        return aprovacao()

    if idade > datahj:
        print()
        print(f'{cores["vermelho"]}Data inválida, tente novamente!{cores["termina"]}')
        return aprovacao()

    if datahj.year - idade.year < 9:
        print()
        print(f'{cores["verde"]}De acordo com sua idade, você deve participar da categoria Mirim '
              f'Até 9 anos!{cores["termina"]}')

    elif datahj.year - idade.year < 14:
        print()
        print(f'{cores["verde"]}De acordo com sua idade, você deve participar da categoria Infantil '
              f'Até 14 anos!{cores["termina"]}')

    elif datahj.year - idade.year < 19:
        print()
        print(f'{cores["verde"]}De acordo com sua idade, você deve participar da categoria Júnior '
              f'Até 19 anos!{cores["termina"]}')

    elif datahj.year - idade.year < 22:
        print()
        print(f'{cores["verde"]}De acordo com sua idade, você deve participar da categoria Sênior '
              f'Até 22 anos!{cores["termina"]}')

    else:
        print()
        print(f'{cores["verde"]}De acordo com sua idade, você deve participar da categoria '
              f'Master acima dos 22 anos!{cores["termina"]}')


# Desafio42 Refaça o desafio 35 dos triângulos acrescentando que tipo de triângulo será formado
# desigualdade triangular para verificar se os comprimentos dos lados formam realmente um triângulo. A desigualdade tri
# angular afirma que a soma de quaisquer dois lados de um triângulo deve ser maior que o comprimento do terceiro lado.
# Triângulo Equilátero: Todos os lados têm o mesmo comprimento.
# Triângulo Isósceles: Dois lados têm o mesmo comprimento.
# Triângulo Escaleno: Todos os lados têm comprimentos diferentes.

def triangulo():
    print()
    print(f'{cores["roxo"]}Analisador de Triângulo{cores["termina"]}')
    print()
    a = float(input(f'{cores["verde"]}Comprimento da reta A:{cores["termina"]}'))
    b = float(input(f'{cores["azul"]}Comprimento da reta B:{cores["termina"]}'))
    c = float(input(f'{cores["amarelo"]}Comprimneto da reta C:{cores["termina"]}'))
    print()

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print(f'{cores["fundoverde"]}Formará um Tiângulo Equilátero!{cores["termina"]}')

        elif a == b or a == c or b == c:
            print(f'{cores["fundoamarelo"]}Formará um Triângulo Isóceles!{cores["termina"]}')

        else:
            print(f'{cores["fundoazulclaro"]}Formará um Triângulo Escaleno!{cores["termina"]}')

    else:
        print(f'{cores["vermelho"]}Não é possível formar um triângulo com essas medidas,Tente Novamente!'
              f'{cores["termina"]}')
        return triangulo()


# Desafio43 Desenvolva uma lógica que leia o peso e a altura de seu IMC e mostre seu status, de acordo, com a tabela:
# Abaixo de 18,5 = Abaixo do Peso - Entre 18,5 e 25 = Peso Ideal - 25 até 30 = Sobrepeso - 30 até 40 = Obesidade
# Acima de 40 = Obesidade Mórbida

def imc_calculator():  # IMC = peso(kg) / [altura x altura(m)]
    print()
    print(f'{cores["roxo"]}Calcular seu IMC(Índice de massa corporal){cores["termina"]}')
    print()
    altura = float(input(f'{cores["amarelo"]}Digite sua altura em (m):{cores["termina"]}'))
    peso = float(input(f'{cores["amarelo"]}Digite seu peso em (Kg):{cores["termina"]}'))
    print()

    if peso / (altura * altura) < 18.5:
        print(f'{cores["vermelho"]}Procure um profissional especializado você está abaixo do peso ideal!'
              f'{cores["termina"]}')
        print(f'{cores["roxo"]}IMC = {peso / (altura * altura):.1f}{cores["termina"]}')

    elif 18.5 < peso / (altura * altura) < 25:
        print(f'{cores["verde"]}Parabéns, você está no seu peso ideal!{cores["termina"]}')
        print(f'{cores["roxo"]}IMC = {peso / (altura * altura):.1f}{cores["termina"]}')

    elif 25 < peso / (altura * altura) < 30:# Condição simples
        print(f'{cores["amarelo"]}Nem tão ruim nem tão bom, você está com sobrepeso, busque melhorar seus hábitos!'
              f'{cores["termina"]}')
        print(f'{cores["roxo"]}IMC = {peso / (altura * altura):.1f}{cores["termina"]}')

    elif peso / (altura * altura) > 30 and peso / (altura * altura) < 40: # Condição complexa
        print(f'{cores["vermelho"]}Você já está passando dos limites do seu corpo e se encontra Obeso,'
              f' busque ajuda de um profissional!'
              f'{cores["termina"]}')
        print(f'{cores["roxo"]}IMC = {peso / (altura * altura):.1f}{cores["termina"]}')

    elif peso / (altura * altura) > 40:
        print(f'{cores["vermelho"]}Você está em uma situação muito delicada e demonstra Obesidade Mórbida,'
              f' busque ajuda de um profissional'
              f' antes que seja tarde dms!'
              f'{cores["termina"]}')
        print(f'{cores["roxo"]}IMC = {peso / (altura * altura):.1f}{cores["termina"]}')


# Desafio44 Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e
# Condição de pagamento: Á vista dinheiro/cheque: 10% de desconto - Á vista no catão: 5% de desconto
# Em até 2x no catão: preço normal - 3x ou mais no cartão: 20% de juros

def valor():
    print('')
    print(f'{cores["roxo"]}Valor a ser pago de acordo com o tipo de pagamento{cores["termina"]}')
    print('')
    print(f'{cores["azulclaro"]}Opções de pagamento\n'
          '\n'
          '1 - Á vista Dinheiro/Cheque = 10% de desconto!\n'
          '2 - Á vista no cartão = 5% de desconto\n'
          '3 - Em até 2x no cartão = preço normal\n'
          f'4 - 3x ou mais no cartão = 20% de jurosco{cores["termina"]}')
    print('')
    escolha = int(input(f'{cores["amarelo"]}Escolha a forma de pagamento:{cores["termina"]}'))

    if escolha not in [1, 2, 3, 4]:
        print('')
        print(f'{cores["vermelho"]}Escolha inválida, Tente novamente!{cores["termina"]}')
        return valor()

    valor_do_produto = float(input(f'{cores["amarelo"]}Digite o valor do produto:{cores["termina"]}'))
    print()

    if escolha == 1:
        print(f'{cores["verde"]}O valor total a ser pago é R${valor_do_produto - 10 / 100 * valor_do_produto}'
              f'{cores["termina"]}')

    elif escolha == 2:
        print(f'{cores["verde"]}O valor total a ser pago é R${valor_do_produto - 5 / 100 * valor_do_produto}'
              f'{cores["termina"]}')

    elif escolha == 3:
        print(f'{cores["verde"]}O valor total a ser pago é R${valor_do_produto}{cores["termina"]}')

    elif escolha == 4:
        print(f'{cores["verde"]}O valor total a ser pago é R${valor_do_produto + 20 / 100 * valor_do_produto}'
              f'{cores["termina"]}')


# Desafio45 Crie um programa que fça o computador jogar Jokenpô com você

def jokenpo():
    print()

    cartas = ['Pedra', 'Papel', 'Tesoura']
    escolhamaquina = random.choice(cartas)

    print(11 * ' ', f'{cores["roxo"]}Jokenpô{cores["termina"]}')
    escolhajogador = int(input(f'{cores["azulclaro"]}Escolha 1-Pedra 2-Papel 3-Tesoura 4-Sair:{cores["termina"]}'))
    print()

    if escolhajogador == 4:
        time.sleep(0.2)
        print(f'{cores["vermelho"]}Saindo!{cores["termina"]}')
        time.sleep(0.4)
        return

    time.sleep(0.2)
    print(f'{cores["azul"]}Eu escolho {escolhamaquina}!{cores["termina"]}')
    print()

    if escolhamaquina == 'Pedra' and escolhajogador == 1:
        time.sleep(1)
        print(f'{cores["amarelo"]}Empate!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Pedra' and escolhajogador == 2:
        time.sleep(1)
        print(f'{cores["verde"]}Você Venceu!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Pedra' and escolhajogador == 3:
        time.sleep(1)
        print(f'{cores["vermelho"]}Você Perdeu!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Papel' and escolhajogador == 1:
        time.sleep(1)
        print(f'{cores["vermelho"]}Você Perdeu!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Papel' and escolhajogador == 2:
        time.sleep(1)
        print(f'{cores["amarelo"]}Empate!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Papel' and escolhajogador == 3:
        time.sleep(1)
        print(f'{cores["verde"]}Você Venceu!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Tesoura' and escolhajogador == 1:
        time.sleep(1)
        print(f'{cores["verde"]}Você Venceu!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Tesoura' and escolhajogador == 2:
        time.sleep(1)
        print(f'{cores["vermelho"]}Você Perdeu!{cores["termina"]}')
        return jokenpo()

    elif escolhamaquina == 'Tesoura' and escolhajogador == 3:
        time.sleep(1)
        print(f'{cores["amarelo"]}Empate!{cores["termina"]}')
        return jokenpo()

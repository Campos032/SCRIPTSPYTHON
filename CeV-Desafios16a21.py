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

# Desafio16 Crie um programa que leia um número escolhido pelo usuário e mostre apenas sua porção inteira
import math
import random
import sys
import playsound


def num_int():
    print('')
    num = float(input('Digite um número qualquer e receberá sua porção inteira:'))
    print('')
    print(f'A porção inteira de {num} é {math.trunc(num)}!')  # ou {int(num)}


# Desafio17 Faça um programa que leia o comprimento do cateto oposto e adjacente de um triângulo retângulo, e mostre o comprimento da hipotenusa

def hip():
    print('')
    print('Aqui iremos calcular a hipotenusa de um triângulo')
    print('')
    cat_op = float(input('Digite o valor do cateto oposto:'))
    cat_ad = float(input('Digite o valor do cateto adjacente:'))
    hipo = math.hypot(cat_op, cat_ad)  # Ou math.sqrt(cat_op**2 + cat_ad**2)
    print(f'O valor da Hipotenusa é {hipo:.2f}!')


# Desafio18 Faça um programa que leia um ângulo qualquer e que mostre na tela o seno, cosseno e tangente desse ângulo

def sen_cos_tan():
    print('')
    print('Aqui iremos verificar o seno, cosseno e a tangente de um ângulo')
    print('')
    ang = float(input('Digite quantos graus o ângulo possui:'))
    rad = math.radians(ang)
    sen = math.sin(rad)
    cos = math.cos(rad)
    tan = math.tan(rad)
    print(f'O seno de {ang}° é {sen:.2f}!\nO cosseno é {cos:.2f}!\nA tangente é {tan:.2f}!')


# Desafio19 Um professor quer sortear um de seus quatro alunos para apagar o quadro, crie um programa que leia os nomes e escolha um para o professor printando-o na tela

def sorteio():
    print('')
    print('Sorteio de Nomes')
    alunos = str(input('Escreva os nomes ou números que deseja sortear separando-os por vírgula:'))
    sort = alunos.split(',')
    print(random.choice(sort))


# Desafio20 O professor támbem quer sortear a ordem de apresentação de trabalho do alunos, crie um programa que faça isso lendo os nomes e os printando na ordem aleatória

def sorteio_da_ordem1():
    print('')
    print('Sorteio da Ordem de Apresentação')
    alunos = str(input('Escreva os nomes ou números que deseja sortear separando-os por vírgula:'))
    sort = alunos.split(',')  # slipt vai separar a str de acordo com o parâmetro que voce usou para separar
    random.shuffle(sort)  # random.shuffle apenas embaralha a lista e não cria uma nova lista embaralhada por isso print(sort) e não criar uma variável para random.shuffle
    print(sort)


sorteio_da_ordem1()


def sorteio_da_ordem2():
    print('')
    print('Sorteio da Ordem de Apresentação')
    a1 = input('Escreva o nome do aluno1:')
    a2 = input('Escreva o nome do aluno2:')
    a3 = input('Escreva o nome do aluno3:')
    a4 = input('Escreva o nome do aluno4:')
    lis = [a1, a2, a3, a4]
    random.shuffle(lis)
    print(lis)


# Desafio21 Crie um programa que abra e reproduza um arquivo em mp3

def abrir_mp3():
    while True:
        print('')
        print('Abrir MP3')
        print('')
        print('1 - Beat1')
        print('2 - Beat2')
        print('3 - Beat3')
        print('4 - Beat4')
        print('5 - Sair')
        print('')
        choice = int(input('Digite um número de acordo com a música que você deseja ouvir:'))

        if choice == 5:
            print('Saindo!')
            sys.exit()

        elif choice == 1:
            playsound.playsound('C:\Celular\Download/002.mp3')

        elif choice == 2:
            playsound.playsound('C:\Celular\Download/spirit2.mp3')

        elif choice == 3:
            playsound.playsound('C:\Celular\Download/violãov.mp3')

        elif choice == 4:
            playsound.playsound('C:\Celular\Download/arp.mp3')


abrir_mp3()

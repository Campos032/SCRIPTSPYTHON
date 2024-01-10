import time
import emoji
from datetime import date


# Desafio 46 Crie um programa que faça a contagem regressiva a partir de 10 com o intervalo de 1 segundo e solte os
# fogos de artifício


def fogos():
    print('Contagem Regressiva Para Fogos')
    emoji1 = emoji.emojize(":partying_face:", language='alias')
    emojis = emoji1 + emoji1 + emoji1 + emoji1
    for i in range(10, 0, -1):
        time.sleep(1)
        print(i)
    print(f'{emojis}FOGOS{emojis}')


# Desafio 47 Crie um programa que mostre todos os números pares entre 1 e 50


def pares():
    print('Números pares até 50')
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)


# Ou for i in range(1, 50, 2): Dessa forma iremos usar menos processamento
#        print(i)


# Desafio 48 Crie um programa que mostre a soma de todos os números ímpares que são múltiplos de 3 entre 1 e 500

def multi3():
    print()
    limite = 501
    multi = []
    for i in range(1, 501):
        m = 3 * i
        if m >= limite:
            break
        elif m % 2 != 0:
            multi.append(m)
    print(sum(multi))


# Desafio 49 Faça a tabuada utilizando do laço for


def tabuada():
    n = int(input('Digite um número:'))
    for i in range(0, 11):
        print(f'{i} x {n} = {n * i}')


# Desafio 50 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor for ímpar desconsidere

def snint():
    lista = []
    for i in range(0, 6):
        n = int(input('Digite um número:'))
        if n % 2 == 0:
            lista.append(n)
    print(sum(lista))


# Desafio 51 Dessenvolva um programa que leia o primeiro termo e a razão de uma PA. Nos mostre os 10 primeiros termos
# Dessa progressão
# Formula geral PA, an = a1 + (n – 1)r, a1 = primeiro termo da PA, n=a posição desejada do termo, r=a razão a cada 2
def pa():
    a1 = int(input('Digite o Primeiro termo da PA:'))
    r = int(input('Digite a razão da PA:'))
    for i in range(1, 11):
        print(a1 + (i - 1) * r)

# Desafio 52 Crie um programa que leia um número inteiro e diga se ele é ou não um número primo


def primo():
    n = int(input('Digite um número inteiro:'))
    print()
    for i in range(2, n):
        if n % i == 0:
            print('Esse número não é primo!')
            break
        else:
            print('Esse número é primo!')
            break


# Desafio 53 Crie um programa que leia uma frase e diga se ela é ou não um palíndromo, desconsidere os espaços

def palin():
    frase = str(input('Escreva uma frase:')).lower()
    frase_sem_espacos = frase.replace(' ', '')
    reversestr = ''
    for letras in reversed(frase_sem_espacos):
        reversestr += letras
    if reversestr == frase_sem_espacos:
        print('Essa frase é um palíndromo!')
    else:
        print('Essa frase não é um palíndromo!')


# Desafio 54 Crie um programa que leia o ano de nasciemnto de 7 pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade, quantas já são maiores

def idade2():
    maior = []
    hj = date.today().year
    for i in range(0, 7):
        i = int(input('Digite o seu ano de nascimento:'))
        id = hj - i
        if id >= 18:
            maior.append(idade)
    print(f'{maior.__len__()} pessoas são maiores de idade e {7 - maior.__len__()} são menores de idade!')


def idade():
    idade1 = []
    for i in range(0, 7):
        i = int(input('Digite a idade:'))
        if i >= 18:
            idade1.append(i)
    print(f'{idade1.__len__()} pessoas são maiores de idade e {7 - idade1.__len__()} são menores de idade!')


# Desafio 55 Crie um programa que leia o peso de 5 pessoa e diga qual o maior e qual o menor peso

def peso_maior_e_menor():
    peso = []
    for i in range(1, 7):
        p = float(input(f'Digite o {i}° peso:'))
        peso.append(p)
    print(f'O maior peso é {max(peso):.2f} Kg!')
    print(f'O menor peso é {min(peso):.2f} Kg!')


# Desafio 56 Crie um programa que leia nome, idade e sexo de 4 pessoas e mostre:
# A média de idade do grupo
# O nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

def n_i_s():
    n_homem = []
    i_homem = []
    i = []
    fem = 0
    for c in range(1, 5):
        print(5 * '-', f'{c}° Pessoa', 5 * '-')
        nome = str(input('Nome:'))
        idade = int(input('Idade:'))
        sexo = int(input('1-Masculino  2-Feminino:'))

        i.append(idade)

        if idade < 20 and sexo == 2:
            fem += 1

        if sexo == 1:
            n_homem.append(nome)
            i_homem.append(idade)

    maioridade_m = max(i_homem)
    indice = i_homem.index(maioridade_m)

    print(f'O nome do homem mais velho é {n_homem[indice]}!')
    print(f'A média de idade do grupo é de {sum(i) / 4} anos!')
    print(f'A quantidade de mulheres com menos de 20 anos é {fem}!')

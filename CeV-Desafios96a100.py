import random


# Desafio 96 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(
# largura e comprimento) e mostre a área do terreno.
def area_g():
    def area(a, b):
        return a * b

    largura = float(input('Informe a largura de um terreno: '))
    comprimento = float(input('Informe o comprimento de um terreno: '))
    print(f'A área de um terreno é {area(largura, comprimento):.2f}m².')


# Desafio 97 Faça um programa que tenha uma função chamada escreva(), que receba como parâmetro e mostre uma mensagem
# com tamanho adaptável.
def escreva_g():
    def escreva(comprimento):
        tamanho = str((len(comprimento) + 4) * '~')
        tamanho2 = len(tamanho)
        print(tamanho)
        print(comprimento.center(tamanho2))
        print(tamanho)

    escreva('Carlos')
    escreva('Carlinhos Brown')
    escreva('Juninho Do Fusca')


# Desafio 98 Faça um programa que tenha uma funçao que receba três parâmetros: início, fim e passo e realize a
# contagem Seu programa tem que realizar três contagens através da função criada: A - De 1 até 10, a cada 1 B - De
# 10 até 0, a cada 2 C - Uma contagem personalizada.
def contagem_g():
    def contagem(inicio, fim, passo):
        for num in range(1, 11, 1):
            print(num, end=' ')
        print()
        for num in range(10, -1, -2):
            print(num, end=' ')
        print()
        inicio = int(input('Informe o início: '))
        fim = int(input('Informe o fim: '))
        passo = int(input('Informe o passo: '))
        for num in range(inicio, fim, passo):
            print(num, end=' ')
        print()

    print(4 * ' ', 'Contagem')
    contagem(0, 0, 0)


# Desafio 99 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior_g():
    def maior(num1):
        maior1 = 0
        for numero in num1:
            if numero > maior:
                maior1 = numero
        print(f'O maior número é {maior1}.')

    print(12 * ' ', 'Qual o maior número')
    lista = list()
    for num in range(1, int(input('Informe quantos números você quer comparar: ')) + 1):
        lista.append(int(input(f'Digite o {num}° número: ')))
    print(lista)
    # while True:
    #     lista.append(int(input('Digite um número: ')))
    #     choice = int(input('1 - SAIR  /  2 - CONTINUAR: '))
    #     if choice == 1:
    #         print(lista)
    #         break
    #     else:
    #         continue
    maior(lista)


# Desafio 100 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A
# primeira função vai sortear 5 números e vai colocá-los dentro da lista e segunda função vai mostrar a soma entre
# todos os valores PARES sorteados pela função anterior.
def sorteio_e_par():
    numeros = list()

    def sorteio():
        for numero in random.sample(range(0, 100 + 1), 10):
            numeros.append(numero)

    sorteio()
    print(numeros)

    def somar_par():
        soma_pares = 0
        for numero in numeros:
            if numero % 2 == 0:
                soma_pares += numero
        print(f'A soma dos números pares é {soma_pares}.')

    somar_par()

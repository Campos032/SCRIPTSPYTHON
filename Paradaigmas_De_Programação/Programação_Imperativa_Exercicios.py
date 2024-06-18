# Cálculo de Média: Escreva um programa que solicite ao usuário uma lista de números e, em seguida, calcule e exiba a
# média desses números.
def media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)


def input_lista():
    tamanho_lista = int(input('Digite o tamanho da lista: '))
    lista = []
    while len(lista) < tamanho_lista:
        lista.append(int(input('Digite um número: ')))
    return lista


def chama_media():
    print('Calcula Média')
    lista = input_lista()
    media_lista = media(lista)
    return print(f'A média da lista é {media_lista}')


# chama_media()


# Verificação de Palíndromo: Escreva um programa que solicite uma palavra ao usuário e verifique se ela é um
# palíndromo (ou seja, se ela é a mesma palavra quando lida de trás para frente).
def recebe_palavra():
    palavra = str(input('Digite uma palavra: '))
    return palavra


def verifica_palindromo(palavra):
    if palavra[::-1].lower() == palavra.lower():
        return print('Essa palavra é um palíndromo')
    return print('Essa palavra não é um palíndromo')


def chama_verifica_palindromo():
    return verifica_palindromo(recebe_palavra())


# chama_verifica_palindromo()


# Ordenação de Lista: Escreva um programa que ordene uma lista de números fornecida pelo usuário em ordem crescente
# ou decrescente. Você pode implementar seu próprio algoritmo de ordenação ou usar funções embutidas na linguagem de
# programação que está utilizando.
def recebe_lista_num():
    tamanho_lista = int(input('Digite o tamanho da lista: '))
    lista = []
    while len(lista) < tamanho_lista:
        lista.append(int(input('Digite um número: ')))
    return lista


def cresce_decresce(lista_num, modo=True):
    if modo:
        return sorted(lista_num)
    else:
        return sorted(lista_num, reverse=True)


def principal():
    return print(cresce_decresce(recebe_lista_num(), False))


# principal()


# Conversão de Temperatura: Escreva um programa que solicite ao usuário uma temperatura em Celsius e a converta para
# Fahrenheit ou vice-versa, dependendo da escolha do usuário.
def temp_conversor(temp, tipo):
    if tipo == 1:
        print('Farenhaits em Celcius')
        print(f'{temp}F° em C° é: {(temp - 32) / 1.8}')
    elif tipo == 2:
        print('Celcius em Farenhaits')
        print(f'{int(temp)}c° em f° é: {int(temp * 1.8 + 32)}°')


def executa_conversor():
    print('Conversor de Temperatura')
    temp = float(input('Digite a temperatura que você quer converter: '))
    tipo = int(input('Escolha o tipo de conversão'
                     '\n1 - Farenhaits em Celcius'
                     '\n2 - Celcius em Farenhaits'
                     '\nDigite sua escolha: '))
    return temp_conversor(temp, tipo)


# executa_conversor()


# Contagem de Vogais e Consoantes:
# Escreva um programa que conte o número de vogais e consoantes em uma frase fornecida pelo usuário.
from unidecode import unidecode


def recebe_frase():
    frase = ''
    while not frase.isalpha():
        frase = str(input('Digite uma frase qualquer: ')).strip().replace(' ', '').lower()
    return unidecode(frase)


def conta_vogal_consoantes(frase):
    vogais = 0
    consoantes = 0
    for letra in frase:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            vogais += 1
        else:
            consoantes += 1
    return f'São {vogais} vogai(s) e {consoantes} consoante(s)'


def executa_contador():
    return conta_vogal_consoantes(recebe_frase())


# print(executa_contador())


# Fatorial de um Número: Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. Você pode
# implementar isso usando loops ou recursão.
def fatorial(num):
    fim = num - 1
    fat = num
    while fim != 1:
        fat *= fim
        fim -= 1
    return fat


fat_de_5 = fatorial(5)
# print(fat_de_5)


# Soma de Números Primos:
# Escreva um programa que calcule a soma de todos os números primos até um número fornecido pelo usuário.
def soma_primos(lista_primos):
    soma = 0
    for num in lista_primos:
        soma += num
    return soma


def separa_primos():
    lista_num = recebe_lista_num()
    lista_primos = []
    for num in lista_num:
        if num > 1 and all(num % i != 0 for i in range(2, num)):  # True se todas as iterações forem true
            lista_primos.append(num)  # Se for true a condição acima, o número primo é adicionado a sua lista
    return lista_primos


def executa_primos():
    return soma_primos(separa_primos())


# print(executa_primos())


# Busca Linear: Escreva uma função que implemente a busca linear em uma lista de números fornecida pelo usuário. A
# função deve procurar um número específico e retornar sua posição na lista (se estiver presente) ou -1 se não
# estiver presente.
def procura_numero(lista_num, numero):
    indices = []
    for i, num in enumerate(lista_num):
        if num == numero:
            indices.append(i)
    if len(indices) != 0:
        return f'O número procurado está no(s) índice(s) {indices}'
    return -1


def exec_search():
    return procura_numero(recebe_lista_num(), int(input('Digite o número que você deseja procurar na lista: ')))


# print(exec_search())


# Cálculo de Média Ponderada: Escreva um programa que solicite ao usuário uma lista de notas e seus respectivos
# pesos, e então calcule e exiba a média ponderada dessas notas.
def calcula_media(lista_notas) -> str:
    soma_produtos = 0
    soma_peso = 0
    for nota_peso in lista_notas:
        soma_produtos += nota_peso[0] * nota_peso[1]
        soma_peso += nota_peso[1]
    return f"{soma_produtos / soma_peso: .2f}"


def recebe_notas():
    lista_notas = []
    for num in range(0, int(input('Digite o quantidade de notas: '))):
        nota = [int(input('Digite a nota: ')), int(input('Digite o peso da nota: '))]
        lista_notas.append(nota)
    return lista_notas


def exec_calculo():
    return calcula_media(recebe_notas())


# print(exec_calculo())


# Validação de Senha: Escreva um programa que solicite ao usuário uma senha e verifique se ela atende aos critérios
# de segurança, como ter um certo comprimento mínimo, conter caracteres especiais, números, letras maiúsculas e
# minúsculas, etc.
def recebe_senha():
    print('Insira uma senha contendo os seguintes requisitos (6 caractéres ou +, 1 Caractere Especial, 1 Número, Letras'
          ' maiúsculas e minúsculas)')
    senha = str(input('Digite sua senha: ')).strip()
    return senha


import re


def valida_senha(senha):
    se_letra_minuscula = any(c.islower() for c in senha)
    se_letra_maiuscula = any(c.isupper() for c in senha)
    caractere_num = any(c.isdigit() for c in senha)
    caractere_especial = bool(re.search(r'[^\w\s]', senha))
    min_length = bool(len(senha) >= 6)
    if se_letra_maiuscula and se_letra_minuscula and caractere_num and caractere_especial and min_length:
        print(f'Senha Aceita!')
        return True
    print(f'Senha não atende os requisitos.')
    return False


# senha_aceita = valida_senha(recebe_senha())
# while not senha_aceita:
#     senha_aceita = valida_senha(recebe_senha())

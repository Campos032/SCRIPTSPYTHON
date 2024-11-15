from random import randint


# Desafio 72 Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

def numeros_por_extenso():
    num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
                   'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

    num = int(input('Digite um número de 0 a 20: '))

    while num not in range(0, 21):
        num = int(input('Escolha inválida! Digite um número de 0 a 20: '))

    print(f'O número que você digitou escrito por extenso é... {num_extenso[num]}')


# Desafio 73 Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre: A)Apenas os 5 primeiros colocados B)Os últimos 4 colocados da tabela.
# C)Uma lista com os times em ordem alfabética D)Em que posição da tabela está o time da chapecoense

def tabela_br():
    tabela_brasileiro = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
                         'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
                         'Vasco Da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

    print(f'Os cinco primeiros colocados são {tabela_brasileiro[:5]}!')
    print(f'Os 4 últimos colocados são {tabela_brasileiro[-4:]}!')
    print(f'A tabela em ordem alfabética fica da seguinte forma {sorted(tabela_brasileiro)}!')
    print(f'A posição do Flamengo na tabela é o {tabela_brasileiro.index("Flamengo") + 1}° Lugar!')


# Desafio 74 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla


def cinco_num():
    cinco_num_rand = tuple(randint(0, 999999) for x in range(5))  # ou criar uma tupla (randint(0, 999999))
    print(f'5 Números Aleatórios = {cinco_num_rand}')  # E inserir randint o quanto de vezes for necessário
    print(f'O maior número é {max(cinco_num_rand)}!')
    print(f'O menor número é {min(cinco_num_rand)}!')

    # print('Os valores sorteados foram: ', end = '')  # O end foi utilizado para não haver quebra de linha
    # for n in cinco_num_rand:
    # print(f'{n} ', end='')


# Desafio 75 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A)Quantas vezes apareceu o valor 9 B)Em que posição foi digitado o primeiro valor 3 C)Quais foram os números pares

# Solução Vídeo
def sol_video():
    """v1 = int(input('Digite o 1° Valor: '))
    v2 = int(input('Digite o 2° Valor: '))
    v3 = int(input('Digite o 3° Valor: '))
    v4 = int(input('Digite o 4° Valor: '))
    vtot = (v1, v2, v3, v4)"""

    # Ou

    nums = (int(input('Digite o 1° Valor: ')),
            int(input('Digite o 2° Valor: ')),
            int(input('Digite o 3° Valor: ')),
            int(input('Digite o 4° Valor: ')))

    print(f'Você digitou os valores {nums}')
    print(f'O 9 apareceu {nums.count(9)} vez(es).')
    if 3 in nums:
        print(f'O número 3 apareceu primeiro na posição {nums.index(3)}')
    else:
        print(f'O número 3 não foi digitado.')
    print(f'Os valores pares digitados foram: ', end='')
    for x in nums:
        if x % 2 == 0:
            print(x, end=' ')


# Minha Solução
def quatro_valores():
    minha_tupla = ()
    cont = 0
    while cont < 4:
        num = int(input('Digite um número qualquer: '))
        # stringnum = str(num)  # Aqui transformei em str, para assim concatenar um no outro em uma nova tupla
        minha_tupla += (num,)  # Anteriormente eu utilizei tuple(stringnum), mas se usar (num, ) não é necessário
        cont += 1  # Converter em str

    print(f'Esses foram os valores digitados... {minha_tupla}.')
    print(f'O nove foi digitado {minha_tupla.count(9)} vez(es).')

    if minha_tupla.count(9) > 0:
        print(f'E apareceu primeiro na {minha_tupla.index(9) + 1}° posição.')

    if 3 in minha_tupla:
        print(f'O número 3 apareceu primeiro na posição {minha_tupla.index(3) + 1}')
    else:
        print(f'O número 3 não foi digitado.')

    # minha_tupla_numint = tuple(map(int, minha_tupla))  # Nessa linha será criada uma nova tupla transformando todos os
    # elementos em inteiros usando o método map
    pares = ()
    for x in minha_tupla:  # for x in minha_tupla_numint: foi o que usei antes
        if x % 2 == 0:
            # x = str(x) # Aqui transformei em str, para assim concatenar um no outro em uma nova tupla
            pares += tuple(x)

    if len(pares) > 0:
        print(f'Os números pares digitados foram {pares}.')


# Desafio 76 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
# No final< mostre uma listagem de preços organizando os dados em forma tubular.

# Solução Vídeo
def solucao_video_tabela_e_preco():
    itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
             'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
    print('-' * 40)
    print(f'{"LISTAGEM DE PRODUTOS":^40}')
    print('-' * 40)
    for pos in range(0, len(itens)):
        if pos % 2 == 0:
            print(f'{itens[pos]:.<30}', end='')
        else:
            print(f'R${itens[pos]:>7.2f}')
    print('-' * 40)


# Minha Solução
def prod_preco():
    produtos_precos = ('Banana', 5, 'Maça', 6, 'Carvão', 7, 'Água', 2.50)
    for x in range(0, len(produtos_precos), 2):  # Vai pegar um índice contando a cada 2, tendo o limite de acordo com
        print(f'O produto {produtos_precos[x]} custa'  # o máximo de itens na tupla
              f' {produtos_precos[x + 1]} reais.')


# Desafio 77 Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar
# para cada palavra, quais são as suas vogais

# Solução do Vídeo
def vogais_solucao_video():
    palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
                'Mercado', 'Programador', 'Futuro', 'Utopia')
    for p in palavras:
        print(f'\nNa palavra {p.upper()} temos ', end='')
        for letra in p:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')


# Minha Solução
def vogais():
    palavras = ('Macarronada', 'Cerebro', 'Umbigo', 'Lombriga', 'Cry', 'Carne', 'Leao', 'Jukebox')

    palavras_min = tuple(elemento.lower() if isinstance(elemento, str) else elemento for elemento in palavras)

    for x in palavras_min:
        vogais_em_cada_palavra = ''
        # If 'a' or 'e' or 'i' or 'o' or 'u' in x:
        # O problema estava na expressão if 'a' or 'e' or 'i' or 'o' or 'u' in x:. Essa expressão é interpretada de
        # forma incorreta em relação ao que você deseja verificar. Vou explicar como ela é avaliada:
        # if 'a': Isso sempre será verdadeiro, porque 'a' é uma string não vazia, e qualquer string não vazia é
        # considerada verdadeira em uma condição.
        # Se a primeira parte for verdadeira, as partes subsequentes da condição
        # (or 'e', or 'i', or 'o', or 'u' in x) não serão avaliadas, porque o Python já sabe que a condição total
        # será verdadeira, uma vez que a primeira parte é verdadeira.
        # Portanto, independentemente do conteúdo da variável x, a condição sempre seria verdadeira. O código
        # corrigido usa um loop para verificar cada vogal individualmente, evitando esse problema.
        if 'a' in x or 'e' in x or 'i' in x or 'o' in x or 'u' in x:  # Maneira Correta
            if 'a' in x:
                vogais_em_cada_palavra += 'a>'
            if 'e' in x:
                vogais_em_cada_palavra += 'e>'
            if 'i' in x:
                vogais_em_cada_palavra += 'i>'
            if 'o' in x:
                vogais_em_cada_palavra += 'o>'
            if 'u' in x:
                vogais_em_cada_palavra += 'u'
            print(f'A palavra {x} possui as seguintes vogais {vogais_em_cada_palavra}')
        else:
            print(f'A palavra {x} não possui vogais.')


# Outra solução que eu havia pensado, mas não consegui resolver
def vogais2():
    palavras = ('Macarronada', 'Cerebro', 'Umbigo', 'Lombriga', 'Cry', 'Carne', 'Leao', 'Jukebox')

    palavras_min = tuple(elemento.lower() if isinstance(elemento, str) else elemento for elemento in palavras)

    for x in palavras_min:
        vogais_em_cada_palavra = ''
        for vogal in 'aeiou':
            if vogal in x:
                vogais_em_cada_palavra += f'{vogal}>'
        if vogais_em_cada_palavra:
            print(f'A palavra {x} possui as seguintes vogais: {vogais_em_cada_palavra}')
        else:
            print(f'A palavra {x} não possui vogais.')

# Desafio22 Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas, O nome com todas as minúsculas, Quantas letras ao
# tem sem considerar espaços, Quantas letras tem o primeiro nome


def conta_nome():
    print('')
    print('''    Nesse programa iremos mostrar seu nome 
    Com todas as letras maiúsculas
    Com todas minúsculas 
    Quantas letras ao todo sem considerar espaços
    E quantas letras tem o primeiro nome''')
    print('')
    nome = str(input('Digite seu nome completo:')).strip()  # para remover os espaços antes e depois
    nome_sem_espaços = nome.replace(' ', '')
    nome_separado = nome.split()
    print('')
    print(nome.upper())
    print(nome.lower())
    print(len(nome_sem_espaços))  # Ou print(len(nome) - nome.count(' ')))
    print(
        f'O primeiro nome é {nome_separado[0]} e tem {len(nome_separado[0])} letras!')  # Ou nome.find(' ') para
    # contar do início até o primeiro espaço/parâmetro
    print('')


# Desafio23 Faça um programa que leia 0 a 9999 e mostre na tela cada um dos dígitos separados ex: 1834 unidade: 4
# dezena: 3 centenas: 8 milhares: 1

# def conta_unidade(): usando estrutura de repetição print('') print('Aqui iremos mostras quantas unidades tem cada
# ordem de um número de o a 9999!') print('') num = int(input('Digite um número de 0 a 9999: ')) num_str = str(num)
# ('') print(f'O número {num} tem') print('') print(f'Unidade:{num_str[-1]}')#Usando o -1 eu determino qual índice
# da str vai ser impresso -1 o último -2 o penúltimo e assim por diante print(f'Dezena:{num_str[-2]}') print(
# f'Centena:{num_str[-3]} ') print(f'Milhar:{num_str[-4]}')'''


def conta_unidade():  # Usando matemática
    print('')
    print('Aqui iremos mostras quantas unidades tem cada ordem de um número de o a 9999!')
    print('')
    num = int(input('Digite um número de 0 a 9999:'))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('')
    print(f'O número {num} Possui')
    print(f'Unidade:{u}')
    print(f'Dezena:{d}')
    print(f'Centena:{c} ')
    print(f'Milha:{m}')


# Desafio24 Crie que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'
def nome_santo():
    print('')
    print('Verificar se a cidade começa com Santo')
    print('')
    city = str(input('Digite o nome de uma cidade:')).strip()  # para remover os espaços antes e depois
    print('')
    print(city.lower().count('santo', 0, 5))  # ou print(city[0:5].lower() == 'santo')


# Desafio25 Crie um programa que leia o nome de uma pessoa e diga se ela tem o 'Silva' no nome
def nome_silva():
    print('')
    print('Verificar se o seu nome possui Silva')
    print('')
    nome = str(input('Digite o seu nome:')).strip()  # para remover os espaços antes e depois
    print('')
    print(nome.lower().find('silva'))  # ou print('silva' in nome.lower())


'''Desafio26 Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A', Em que posição ela aparece a primeira vez, Em que posição ela aparece a última vez'''


def letra_a():
    print('')
    print('Verificar quantas vezes aparece a letra A, em que posição ela aparece pela primeira e última vez')
    print('')
    frase = str(input('Digite uma frase:'))
    print('Aparece:', frase.lower().count('a'), 'vezes')
    print('Primeiro na:', frase.find('a') + 1, 'posição')
    print('E por último na:', frase.rfind('a') + 1, 'posição')
    # + 1 foi usado para mostrar a posição começando a contagem em 1 e não em 0


# Desafio27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente. Ex: Ana Maria de Souza primeiro=Ana último: Souza

def primeiro_e_ultimo_nome():
    print('')
    print('Verificar primeiro e último nome')
    print('')
    nome = str(input('Digite um nome:')).strip()
    nome_separado = nome.split()
    print('Primeiro nome:', nome_separado[0])
    print('Último nome:', nome_separado[-1])


primeiro_e_ultimo_nome()

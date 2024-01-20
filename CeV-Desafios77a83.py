# Desafio 78 Faça um programa que leia 5 valores e guarde-os em uma lista. No final mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

# Solução Vídeo
def cinco_num_lis_video():
    lista_num = []
    maior = 0
    menor = 0
    for c in range(0, 5):
        lista_num.append(int(input(f'Digite um valor para a Posição {c}: ')))
        if c == 0:
            maior = menor = lista_num[c]
        else:
            if lista_num[c] > maior:
                maior = lista_num[c]
            if lista_num[c] < menor:
                menor = lista_num[c]
    print('-' * 30)
    print(f'Você digitou os valores {lista_num}.')
    print(f'O maior valor digitado foi {maior} nas posições ', end='')
    for i, v in enumerate(lista_num):
        if lista_num[i] == maior:
            print(f'{i}... ', end='')
    print()
    print(f'O menor valor digitado foi {menor} nas posições ', end='')
    for i, v in enumerate(lista_num):
        if lista_num[i] == menor:
            print(f'{i}... ', end='')
    print()


# Minha Solução
def cinco_num_lis():
    lista_cinco_num = list()
    qnt_num = 1
    for x in range(0, 5):
        valor = int(input(f'Escreva o {qnt_num}° número:'))
        lista_cinco_num.append(valor)
        qnt_num += 1
    print(f'A lista é {lista_cinco_num}.')
    print(f'O maior valor na lista é {max(lista_cinco_num)} e aparece na(s) posição(es) ', end='')
    for i, v in enumerate(lista_cinco_num):
        if v == max(lista_cinco_num):
            print(f'{i}... ', end='')
    print()
    print(f'O menor valor da lista é {min(lista_cinco_num)} e aparece na(s) posição(es) ', end='')
    for i, v in enumerate(lista_cinco_num):
        if v == min(lista_cinco_num):
            print(f'{i}... ', end='')
    # Como eu esqueci de verificar as posições, eu usarei o enumerete igual o exercício do vídeo


# Desafio 79 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o
# número já exista lá não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescent

# Solução Vídeo
def num_lis_video():
    numeros = list()
    while True:
        n = int(input('Digite um valor: '))
        if n not in numeros:
            numeros.append(n)
        else:
            print('Valor duplicado! Não vou adicionar...')
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
        print('-=' * 30)
        numeros.sort()
    print(f'Você digitou os valores {numeros}')


# Minha Solução
def num_lis():
    lista_de_numeros = list()
    qnt_num_lista = int(input('Digite quantos números você quer adicionar a lista:'))
    qnt_num = 1
    for x in range(0, qnt_num_lista):
        print()
        valor = int(input(f'Escreva o {qnt_num}° número:'))
        if valor not in lista_de_numeros:
            lista_de_numeros.append(valor)
            print('Valor adicionado a lista!')
        else:
            print('Esse valor já está na lista e não foi adicionado!')
        qnt_num += 1
    print()
    print(f'A lista de forma crescente fica da seguinte forma {sorted(lista_de_numeros)}')


# Desafio 80 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, ja na
# posição correta de inscrição(sem usar sort()). No final, mostre a lista ordenada na tela.

# Solução Vídeo
def inserir_num_de_forma_ordenada_video():
    lista = []
    for c in range(0, 5):
        n = int(input('Digite um valor: '))
        if c == 0 or n > lista[-1]:
            lista.append(n)
            print('Adicionado ao Final da Lista...')
        else:
            pos = 0
            while pos < len(lista):
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    print(f'Adicionado na posição {pos} da lista...')
                    break
                pos += 1
    print('-=' * 30)
    print(f'Os valores digitados em ordem foram {lista}')


# Minha Solução
def inserir_num_de_forma_ordenada():
    lista_de_numeros = list()
    qnt_num = 1
    while True:
        valor = int(input(f'Escreva o {qnt_num}° número:'))
        qnt_num += 1
        if valor not in lista_de_numeros:
            inserted = False
            for i, x in enumerate(lista_de_numeros):
                if valor < x:
                    lista_de_numeros.insert(i, valor)
                    inserted = True
                    break
            if not inserted:
                lista_de_numeros.append(valor)
        choice = int(input('1-Sair  2-Continuar'))
        if choice == 1:
            print(f'A lista de forma crescente fica da seguinte forma {lista_de_numeros}')
            break
        else:
            continue


# Desafio 81 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A)Quantos números
# foram digitados. B)A lista de valores ordenada de forma decrescente C)Se o valor 5 foi digitado e está ou não na lista

# Solução Vídeo
def lista_e_parametros_video():
    valores = []
    while True:
        valores.append(int(input('Digite um valor: ')))
        resp = str(input('Quer continuar? [S/N]'))
        if resp in 'Nn':
            break
    print('-=' * 30)
    print(f'Você digitou {len(valores)} elementos.')
    valores.sort(reverse=True)
    print(f'Os valores em ordem decrescente são {valores}')
    if 5 in valores:
        print('O valor 5 faz parte da lista!')
    else:
        print('O valor 5 não foi encontrado na lista!')


# Minha Solução
def lista_e_parametros():
    lista_de_numeros = list()
    qnt_num_lista = int(input('Digite quantos números você quer adicionar a lista:'))
    qnt_num = 1
    for x in range(0, qnt_num_lista):
        valor = int(input(f'Escreva o {qnt_num}° número:'))
        lista_de_numeros.append(valor)
        qnt_num += 1
    print(f'Foram digitados {len(lista_de_numeros)} números.')
    print(f'A lista de forma decrescente fica da seguinte forma {sorted(lista_de_numeros, reverse=True)}')
    if 5 in lista_de_numeros:
        print('O numéro 5 foi digitado!')
    else:
        print('O número 5 não foi digitado!')


# Desafio 82 Crie um programa que leia vários números e os coloque em uma lista. Depois disso, crie duas litas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

# Solução vídeo
def lis_par_impar_video():
    num = list()
    pares = list()
    impares = list()
    while True:
        num.append(int(input('Digite um número: ')))
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn':
            break
    for i, v in enumerate(num):
        if v % 2 == 0:
            pares.append(v)
        elif v % 2 == 1:
            impares.append(v)
    print('-=' * 30)
    print(f'A lista completa é {num}')
    print(f'A lista de pares é {pares}')
    print(f'A lista de ímpares é {impares}')


# Minha Solução
def lis_par_impar():
    lista = []
    lista_par = []
    lista_impar = []
    qnt_num = 1
    while True:
        num = int(input(f'Escreva o {qnt_num}° número:'))
        qnt_num += 1
        lista.append(num)
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)

        choice = int(input('1-Sair  2-Continuar:'))
        if choice == 1:
            print(f'A lista completa {lista}.')
            if lista_impar:
                print(f'A lista com números ímpares {lista_impar}.')
            if lista_par:
                print(f'E a lista com números pares {lista_par}.')
            break
        else:
            continue


# Desafio 83 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Solução Vídeo
def verificador_de_expressao_video():
    expr = str(input('Digite a expressão: '))
    pilha = []
    for simb in expr:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break

    if len(pilha) == 0:
        print('Sua expressão está válida!')
    else:
        print('Sua expressão está inválida!')


# Minha Solução, mesclada com a do CHATGPT
def verificador_de_expressao():
    parenteses_abrem = []
    # parenteses_fecham = []
    print(4 * ' ', 'Verificador de Uso dos Parênteses')
    frase = str(input('Digite algo que contenha o uso de parênteses:'))
    # frase_sem_espacos = frase.replace(' ', ''), frase.strip()  # não será necessário
    vazio = False
    for x in frase:
        if x == '(':
            parenteses_abrem.append('(')
        elif x == ')':
            if not parenteses_abrem:
                vazio = True  # Encontrou ')' sem correspondente '('
                break
            parenteses_abrem.pop()
        # if x == ')':
            # parenteses_fecham.append(')')
    # if len(parenteses_abrem) - len(parenteses_fecham) == 0 and frase.index('(') < frase.index(')'):
        # print('Os parênteses estão impostos corretamente!')
    if '(' not in frase and ')' not in frase:
        print('Não foi digitado parênteses.')
    elif len(parenteses_abrem) == 0 and vazio == False:
        print('Os parênteses estão impostos corretamente!')
    else:
        print('Os parênteses estão impostos incorretamente!')

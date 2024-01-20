import time
from random import sample, randint


# Desafio 84 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A - Quantas pessoas foram cadastradas, B - Uma listagem com as pessoas mais pesadas e nomes, C - Uma listagem com as
# pessoas mais leves e nomes

# Solução Vídeo
def nome_e_peso_video():
    temp = []
    princ = []
    mai = men = 0
    while True:
        temp.append(str(input('Nome: ')))
        temp.append(float(input('Peso: ')))
        if len(princ) == 0:
            mai = men = temp[1]
        else:
            if temp[1] > mai:
                mai = temp[1]
            if temp[1] < men:
                men = temp[1]
        princ.append(temp[:])
        temp.clear()
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn':
            break
    print('-=' * 30)
    print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
    print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
    for p in princ:
        if p[1] == mai:
            print(f'[{p[0]}] ', end='')
    print()
    print(f'O menor peso foi de {men}Kg. Peso de ', end='')
    for p in princ:
        if p[1] == men:
            print(f'[{p[0]}] ', end='')
    print()


# Minha Solução
def nome_e_peso():
    print(5 * ' ', 'Cadastro de Pessoas/Pesos')
    lista_cadastro = list()
    lista_temporaria = list()
    qnt_pessoas = 0
    maior_peso = 0
    menor_peso = 9999
    while True:
        lista_temporaria.append(input('Escreva seu nome: '))
        peso = int(input('Escreva seu peso: '))
        lista_temporaria.append(peso)
        lista_cadastro.append(lista_temporaria[:])
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
        lista_temporaria.clear()
        qnt_pessoas += 1
        choice = int(input('1-Sair  2-Continuar: '))
        print(50 * '-')
        if choice == 1:
            lista_nomes_maior_peso = list()
            lista_nomes_menor_peso = list()
            for pessoa in lista_cadastro:
                if pessoa[1] >= maior_peso:
                    lista_nomes_maior_peso.append(pessoa[0])
                elif pessoa[1] <= menor_peso:
                    lista_nomes_menor_peso.append(pessoa[0])
            print(f'Foram cadastradas {qnt_pessoas} pessoas.')
            print(f'As pessoas com maior peso ({maior_peso}Kg) são... {lista_nomes_maior_peso}')
            print(f'As pessoas com menor peso ({menor_peso}Kg) são... {lista_nomes_menor_peso}')
            break
        else:
            continue


# Desafio 85 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Ótima Solução dos comentários
def solucao_comentario():
    valores = [[], []]
    for c in range(1, 8):
        num = int(input(f'Numero {c}°'))
        valores[num % 2].append(num)  # Se o número for par ele ira ser adicionado a valores[0] se impar valores[1]
    print(f'Valores pares digitados: {sorted(valores[0])}')
    print(f'Valores impares digitados: {sorted(valores[1])}')

    
# Solução Vídeo
def impar_e_par_video():
    num = [[], []]
    valor = 0
    for c in range(1, 8):
        valor = int(input(f'Digite o {c}o. valor: '))
        if valor % 2 == 0:
            num[0].append(valor)
        else:
            num[1].append(valor)
    print('-=' * 30)
    num[0].sort()
    num[1].sort()
    print(f'Os valores pares digitados foram: {num[0]}')
    print(f'Os valores ímpares digitados foram; {num[1]}')


# Minha Solução
def impar_e_par():
    print(10 * ' ', 'Pares e Ímpares - Lista Crescente')
    lista_pares_impares = [[], []]
    for pessoa in range(0, 7):
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            lista_pares_impares[0].append(numero)
        else:
            lista_pares_impares[1].append(numero)
    if len(lista_pares_impares[0]) >= 1:
        print(f'Os valores pares digitados foram: {sorted(lista_pares_impares[0])}')
    if len(lista_pares_impares[1]) >= 1:
        print(f'Os valores ímpares digitados foram: {sorted(lista_pares_impares[1])}')


# Desafio 86 Crie um programa qie crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre na tela, com a formatação correta

# Solução Vídeo
def matriz_3x3_video():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l1 in range(0, 3):
        for c in range(0, 3):
            matriz[l1][c] = int(input(f'Digite um valor para [{l1}, {c}]: '))
    print('-=' * 30)
    for l2 in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l2][c]:^5}]', end='')
        print()


# Minha Solução
def matriz_3x3():
    lista_numeros = list()
    for numero in range(0, 9):
        lista_numeros.append(int(input('Digite um número: ')))
    conta_linha = 0
    for numero in sorted(lista_numeros):
        if conta_linha < 3:
            print(f'[{numero}]', end='')
            conta_linha += 1
        elif conta_linha == 3:
            conta_linha = 1
            print()
            print(f'[{numero}]', end='')


# Desafio 87 Aprimore o desfio anterior, mostrando: A - A soma de todos os valores pares digitados.
# B - A soma dos valores da terceira coluna, C - O maior valor da segunda linha.

# Solução do Vídeo
def matriz_3x3_2versao_video():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    spar = mai = scol = 0
    for l1 in range(0, 3):
        for c in range(0, 3):
            matriz[l1][c] = int(input(f'Digite um valor para [{l1}, {c}]: '))
    print('-=' * 30)
    for l2 in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l2][c]:^5}]', end='')
            if matriz[l2][c] % 2 == 0:
                spar += matriz[l2][c]
        print()
    print('-=' * 30)
    print(f'A soma dos valores pares é {spar}')
    for l1 in range(0, 3):
        scol += matriz[l1][2]
    print(f'A soma dos valores da terceira coluna é {scol}')
    for c in range(0, 3):
        if c == 0:
            mai = matriz[1][c]
        elif matriz[1][c] > mai:
            mai = matriz[1][c]
    print(f'O maior valor da segunda linha é {mai}')


# Minha Solução
def matriz_3x3_2versao():
    lista_numeros = list()
    for numero in range(0, 9):
        lista_numeros.append(int(input('Digite um número: ')))
    print(20 * '><')
    soma_terceira_coluna = list()
    maior_valor_segunda_linha = 0
    conta_linha = 0
    conta_numero = 0
    for numero in lista_numeros:
        if 3 <= conta_numero <= 5:
            if numero > maior_valor_segunda_linha:
                maior_valor_segunda_linha = numero
        if conta_linha < 3:
            print(f'[{numero:^5}]', end='')
            if conta_linha + 1 == 3:
                soma_terceira_coluna.append(numero)
            conta_linha += 1
            conta_numero += 1
        elif conta_linha == 3:
            conta_linha = 1
            print()
            print(f'[{numero:^5}]', end='')
            conta_numero += 1
    print()
    soma_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma_pares += numero
    print(20 * '><')
    print(f'A soma de todos os valores  digitados é: {sum(lista_numeros)} dos pares é: {soma_pares}')
    print(f'A soma dos valores da terceira coluna é: {sum(soma_terceira_coluna)}')
    print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')


# Desafio 88 Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60para cada jogo, cadastrando tudo em uma lista.

# Soluções dos comentarios
def solucao_comentario1():
    num = int(input('How many times do you want to bet? '))
    for i in range(0, num):
        print(f'Bet number {i + 1}:', end=" ")
        bet = sample(range(1, 61), 6)
        print(sorted(bet))
        time.sleep(2)


def solucao_comentario2():
    for i in range(int(input('Nº de Jogos: '))):
        print(f'{i + 1}º Jogo: {sorted(sample(list(range(1, 61)), k=6))}')


# Solução do Vídeo
def mega_sena_video():
    lista = list()
    jogos = list()
    print('-' * 30)
    print('JOGA NA MEGA SENA'.center(30))
    print('-' * 30)
    quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
    tot = 1
    while tot <= quantidade:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-=' * 3, f' SORTEANDO {quantidade} JOGOS', '-=' * 3)
    for i, l in enumerate(jogos):
        print(f'JOGO {i+1}: {l}')
        time.sleep(1)
    print('-=' * 5, '<BOA SORTE!>', '-=' * 5)


# Minha Solução
def mega_sena():
    todos_jogos = list()
    jogo_temporario = list()
    print(2 * ' ', 'Gerador de jogos da Mega Sena')
    qnt_jogos = int(input('Quantos jogos você quer que eu gere? '))
    while len(todos_jogos) != qnt_jogos:
        jogo_temporario = list(sample(range(1, 61), 6))
        todos_jogos.append(jogo_temporario[:])
    for jogo in todos_jogos:
        print(jogo)
        time.sleep(1)


# Desafio 89 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

# Solução do Video
def cadastro_notas_aluno_video():
    ficha = list()
    while True:
        nome = str(input('Nome: '))
        nota1 = float(input('Nota1: '))
        nota2 = float(input('Nota2: '))
        media = (nota1 + nota2) / 2
        ficha.append([nome, [nota1, nota2], media])
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn':
            break
    print('-=' * 30)
    print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
    print('-' * 25)
    for i, a in enumerate(ficha):
        print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    while True:
        print('-' * 25)
        opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if opc == 999:
            print('FINALIZANDO...')
            break
        if opc <= len(ficha) - 1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    print('<<< VOLTE SEMPRE >>>')


# Minha Solução
def cadastro_notas_aluno():
    print(20 * ' ', 'Cadastro de Notas de Alunos')
    alunos = list()
    aluno_temporario = list()
    while True:
        aluno_temporario.append(str(input('Escreva o nome do aluno: ')))
        aluno_temporario.append(float(input('Escreva a 1° Nota: ')))
        aluno_temporario.append(float(input('Escreva a 2° Nota: ')))
        alunos.append(aluno_temporario[:])
        aluno_temporario.clear()

        choice = int(input('1-Sair Cadastro  2-Continuar Cadastro: '))
        if choice == 1:
            print(20 * '><')
            print('No.', 5 * ' ', 'Nome', 15 * ' ', 'Média')
            print(40 * '=')
            for indice, aluno in enumerate(alunos):
                print(indice, 7 * ' ', aluno[0], 13 * ' ', (aluno[1] + aluno[2]) / 2)
            print(40 * '=')
            choice2 = int(input('Escreva o número do aluno que você quer ver as notas ou [999-Sair]: '))
            if choice2 == 999:
                print('Saindo...')
                time.sleep(2)
                break
            while choice2 != 999:
                print(f'As notas do aluno {alunos[choice2][0]} são {alunos[choice2][1],alunos[choice2][2]}')
                print(40 * '-')
                choice2 = int(input('Escreva o número do aluno que você quer ver as notas ou [999-Sair]: '))
        else:
            print(25 * '-')
            continue


def cadastro_notas_aluno_formatacaostrdiferente():
    print(20 * ' ', 'Cadastro de Notas de Alunos')
    alunos = list()
    aluno_temporario = list()
    while True:
        aluno_temporario.append(str(input('Escreva o nome do aluno: ')))
        aluno_temporario.append(float(input('Escreva a 1° Nota: ')))
        aluno_temporario.append(float(input('Escreva a 2° Nota: ')))
        alunos.append(aluno_temporario[:])
        aluno_temporario.clear()

        choice = int(input('1-Sair Cadastro  2-Continuar Cadastro: '))
        if choice == 1:
            print(40 * '=')
            print('No.'.ljust(5), 'Nome'.ljust(20), 'Média'.ljust(20))
            print(40 * '=')
            for indice, aluno in enumerate(alunos):
                nome = aluno[0]
                media = (aluno[1] + aluno[2]) / 2
                print(str(indice).ljust(5), nome.ljust(20), f"{media:.2f}".ljust(20))
            print(40 * '=')
            choice2 = int(input('Escreva o número do aluno que você quer ver as notas ou [999-Sair]: '))
            if choice2 == 999:
                print('Saindo...')
                time.sleep(2)
                break
            while choice2 != 999:
                print(f'As notas do aluno {alunos[choice2][0]} são {alunos[choice2][1],alunos[choice2][2]}')
                print(40 * '-')
                choice2 = int(input('Escreva o número do aluno que você quer ver as notas ou [999-Sair]: '))
        else:
            print(25 * '-')
            continue

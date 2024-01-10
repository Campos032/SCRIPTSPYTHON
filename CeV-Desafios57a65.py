import random
import math
import time

# Desafio 57 Faça um programa que leia o sexo de uma pessoa [M/F], caso esteja errado, mostre uma mensagem de erro
# e a repita até o usuário digitar uma entrada válida

# Solução do vídeo
"""sexo = input('Digite seu sexo: [M/F] ').strip().upper()
while sexo not in 'MF':
    sexo = input('Dados inválidos, Por Favor, tente novammente: [M/F]').strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')"""


# Minha Solução
"""while True:
    sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Escolha inválida, tente novamente!')
    elif sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            sexo = 'Masculino'
        if sexo == 'F':
            sexo = 'Feminino'
        print(f'Você é do sexo {sexo}!')
        break"""

# Desafio 58 Melhore o jogo do desafio 28 onde o computador vai 'pensar' um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Solução do vídeo
"""computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu plapite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
        print(f'Você acertou em {palpites} tentativas, escolha do computador = {computador}!')
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')"""

# Minha Solução
def adivinha():
    tentativas = 0
    choice_pc = random.choice(range(1, 11))
    print('Jogo do Adivinha')
    while True:
        choice_player = int(input('Escolha um número de 1 a 10:'))

        if choice_player != choice_pc:
            tentativas += 1

        elif choice_player == choice_pc:
            print(f'Você acertou na {tentativas + 1}° tentativa!')
            con_sa = int(input('Digite 1-Continuar  2-Sair'))

            if con_sa == 1:
                return adivinha()

            elif con_sa == 2:
                print('Saindo!')
                return

# Desafio 59 Crie um programa que leia dois valores e mostre um menu na tela: [1]Somar [2]Multiplicar [3]Maior
# [4]Novos números [5]Sair do programa seu programa devera realizar a operação solicitada em cada caso

# Solução do vídeo
"""n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
opcao = 0
while opcao != 5:
    print('    [1] Somar'
    '[2] Multiplicar'
    '[3] Maior'
    '[4] Novos Números'
    '[5] Sair')

    opcao = int(input('>>>>> Escolha uma ação:'))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}!')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} * {n2} é {produto}!')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif opcao == 5:
        print()
        time.sleep(1)
        print('Saindo!')
        time.sleep(1)
    else:
        print('Escolha inválida, tente novamente!')
        time.sleep(1)"""


# Minha solução
"""while True:
    print(5 * ' ', 'Dois valores', 5 * ' ')
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))

    soma = x + y
    multi = x * y
    maior = []

    print('''
    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novos Números
    5 - Sair''')

    choice = int(input('Escolha uma ação:'))

    if choice == 1:
        print(soma)

    elif choice == 2:
        print(multi)

    elif choice == 3:
        maior.append(x)
        maior.append(y)
        print(max(maior))

    elif choice == 4:
        continue

    elif choice == 5:
        print('Saindo!')
        break"""


# Desafio 60 Faça um programa que leia um número qualquer e mostre o seu fatorial, fatorial de 5! = 5x4x3x2x1 = 120

# Solução do Vídeo
"""n = int(input('Digite um número qualquer para calcular seu fatorial:'))
c = n
f = 1
print(f'Calculando {n}!=', end='')
while c > 0:
    print(f' {c}', end='')
    print(' x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')"""

# Minha Solução
"""print(5 * ' ', 'Fatorial de um número')
num = int(input('Digite um número:'))
fat = num * (num - 1)
num1 = num - 1
while num1 != 1:
    num1 -= 1
    fat *= num1
print(fat)"""

# Desafio 61 Reforçe o desafio 51, lendo o primeiro termo de uma PA e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while. Fórmula PA an = a1 + (n – 1)r

# Solução do Vídeo
"""print('Gerador de PA')
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('Fim!')"""

# Minha Solução
"""print('Progressão Aritmética - 10 primeiros Termos')
pt = int(input('Digite o primeiro termo:'))
rz = int(input('Digite a razão da PA:'))
termos_pa = []
enésimo = 0
qnt_termos = 0
while qnt_termos < 10:
    enésimo += 1
    pa = pt + (enésimo - 1) * rz
    termos_pa.append(pa)
    qnt_termos = len(termos_pa)"""

# Desafio 62 Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerra quando ele dizer que quer 0 termos.

# Solução do vídeo
"""print('Gerador de Pa')
primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razão
        cont += 1
    print('Pausa...')
    mais = int(input('Digite quantos termos a mais você quer mostrar:'))
print(f'Progressão finalizada com {total} termos mostrados!')"""

# Minha solução 1
"""print('Progressão Aritmética ')
pt = int(input('Digite o primeiro termo:'))
rz = int(input('Digite a razão da PA:'))
termos_pa = []
enesimo = 0
qnt_termos = 0
termos = int(input('Digite a quantidade de termos da progressão você quer saber:'))
termos1 = 0
while termos != 0:
    enesimo += 1
    pa = pt + (enesimo - 1) * rz
    termos_pa.append(pa)
    qnt_termos = len(termos_pa)

    if qnt_termos == termos:
    # A função map() em Python é uma função integrada que aplica uma função a todos os itens de uma ou mais sequências
    # (listas, tuplas, etc.) e retorna um iterador que produz os resultados. É como se fosse uma estrutura de loop
        print(' > '.join(map(str, termos_pa[- termos1:])), '> Pause...')
        termos1 = int(input('Digite quantos termos a mais você quer:'))
        termos += termos1

        if termos1 == 0:
            print()
            print(f'Você visualizou {qnt_termos} termos da progressão!')
            print()
            time.sleep(1)
            print('Saindo!')"""

# Desafio 63 Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
# uma sequência Fibonacci. 0 - 1 - 1 - 2 - 3 - 5 - 8 Fórmula = an = 1/√5 * [(1 + √5 / 2)^n - (1 - √5 / 2)^n]
# a1 = a2 = 1 / O próximo termo é igual a soma dos dois anteriores

# Solução do vídeo
"""print('Sequência de Fibonacci')
n = int(input('Quantos termos voê quer mostrar?:'))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('> FIM!')"""

# Minha solução
print(8 * ' ', 'Sequência de Fibonacci')
an = int(input('Digite o índice que você deseja encontrar:'))
print()
qnt_depois_do_indice_escolhido = int(input('Digite a quantidade de elementos que você deseja saber após o '
                                           'índice escolhido:'))
ia = an - 1  # Índice anterior

r5 = math.sqrt(5)

indice_do_termo = round((1/r5) * ((((1 + r5) / 2) ** an) - (((1 - r5) / 2) ** an)))  # Round foi usado para fazer o
indice_anterior = round((1/r5) * ((((1 + r5) / 2) ** ia) - (((1 - r5) / 2) ** ia)))  # arrendondamento
prox_termo = indice_do_termo + indice_anterior

elementos_seguintes = [indice_do_termo, prox_termo]
qnt_elementos = len(elementos_seguintes)
elemento_anterior = prox_termo

while len(elementos_seguintes) - 2 < qnt_depois_do_indice_escolhido:
    elemento_anterior = elementos_seguintes[-2] + elemento_anterior
    elementos_seguintes.append(elemento_anterior)

print(f'\nO termo referente ao índice que você indicou é {indice_do_termo}!\n\nO anterior é {indice_anterior}!\n')
print(f'E os {qnt_depois_do_indice_escolhido} termos seguintes são ',' > '.join(map(str, elementos_seguintes[1::])),'!')


# Desafio 64 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma
# entre eles(desconsiderando o flag (999))

# Solução do vídeo
"""num = cont = soma = 0
num = int(input('Digite um número [999 para sair]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para sair]:'))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')"""


# Minha solução
"""qnt_num = 0
soma = 0
while condicao:
    num = int(input('Digite algum número:'))
    if num == 999:
        break            
    soma += num
    qnt_num += 1
print(f'{qnt_num} números foram inseridos!')
print(f'E a soma entre eles é igual a {soma}!')"""

# Desafio 65 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos e qual foi o maior e qual foi o maior e o menor. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores

# Solução do vídeo
"""resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).strip()
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')"""


# Minha Solução
"""lis = []
qnt_num = 0
while True:
    num = int(input('Digite um número qualquer:'))
    qnt_num += 1
    lis.append(num)

    s_n = input('Quer continuar? [S/N]').strip()
    while s_n not in 'SNsn':
        print('Escolha inválida, tente novamente!')
        s_n = input('Quer continuar? [S/N]').strip()

    if s_n in 'Nn':
        print(f'Você digitou {qnt_num} números e a média entre eles é {sum(lis) / qnt_num:.2f}!')
        print(f'O maior número digitado é {max(lis)} e o menor é {min(lis)}!')
        break

    if s_n in 'Ss':
        continue"""

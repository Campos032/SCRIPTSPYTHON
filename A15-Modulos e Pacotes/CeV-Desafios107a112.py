# Desafio 107 Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(),
# metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
from pacotes.monetario import moeda, moeda2
from pacotes.utilidadesCeV import dado


def desafio107():
    print(4 * ' ', 'Operações Monetárias')
    num = float(input('Digite um valor R$: '))
    porcento = int(input('Digite uma porcentagem: '))
    print(f'{num} mais {porcento}% é igual a {moeda.aumentar(num, porcento)}')
    print(f'{num} menos {porcento}% é igual a {moeda.diminuir(num, porcento)}')
    print(f'O dobro de {num} é igual a {moeda.dobro(num)}')
    print(f'A metade de {num} é igual a {moeda.metade(num)}')


# Desafio 108 Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os
# valores como um valor monetário formatado.
def desafio108():
    print(4 * ' ', 'Operações Monetárias')
    num = float(input('Digite um valor R$: '))
    porcento = int(input('Digite uma porcentagem: '))
    print(f'{moeda.moeda(num)} mais {porcento}% é igual a {moeda.moeda(moeda.aumentar(num, porcento))}')
    print(f'{moeda.moeda(num)} menos {porcento}% é igual a {moeda.moeda(moeda.diminuir(num, porcento))}')
    print(f'O dobro de {moeda.moeda(num)} é igual a {moeda.moeda(moeda.dobro(num))}')
    print(f'A metade de {moeda.moeda(num)} é igual a {moeda.moeda(moeda.metade(num))}')


# Desafio 109 Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ou não ser formatado pela função moeda(), desenvolvido no desafio 108.
def desafio109():
    print(4 * ' ', 'Operações Monetárias')
    num = float(input('Digite um valor R$: '))
    porcento = int(input('Digite uma porcentagem: '))
    print(f'{moeda2.moeda(num)} mais {porcento}% é igual a {moeda2.aumentar(num, porcento, True)}')
    print(f'{moeda2.moeda(num)} menos {porcento}% é igual a {moeda2.diminuir(num, porcento, False)}')
    print(f'O dobro de {moeda2.moeda(num)} é igual a {moeda2.dobro(num, True)}')
    print(f'A metade de {moeda2.moeda(num)} é igual a {moeda2.metade(num, False)}')


# Desafio 110 Adicione ao módulo moeda.py uma função chamada resumo(), que mostre na tela algumas informações geradas
# pelas funções que já temos no módulo criado até aqui, em forma de tabela.
def desafio110():
    print(4 * ' ', 'Operações Monetárias')
    num = float(input('Digite um valor R$: '))
    porcento_mais = int(input('Digite porcentagem do aumento: '))
    porcento_menos = int(input('Digite porcentagem da diminuição: '))
    moeda2.resumo(num, porcento_mais, porcento_menos)


# Desafio 111 Crie um pacote chamado utilidadesCeV que tenha dois módulos chamados moeda e dado. Transfira todas as
# funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
# Obs: Eu fui separando os modulos e pacotes antes desse desafio, portanto já está concluído

# Desafio 112 Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
# chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas como uma validação de dados para aceitar
# apenas valores que sejam monetários

valor = dado.leia_dinheiro()
moeda2.resumo(valor, 10, 50)

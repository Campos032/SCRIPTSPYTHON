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

# Desafio5 Leia um Número inteiro e diga o seu sucessor e antecessor
def num_ant_suc():
    print('')
    print('Nesse programa iremos verificar o Antecessor e o Sucessor do Número Inteiro que você digitar!')
    print('')
    num = int(input('Digite um número inteiro:'))
    print(f'O antecessor de {cores["azul"]}{num}{cores["termina"]} é {cores["roxo"]}{num - 1}{cores["termina"]}!'
          f'\nE seu sucessor é {cores["amarelo"]}{num + 1}{cores["termina"]}!')


num_ant_suc()
# Desafio6 Crie um Algorítimo que leia um número que mostre seu dobro, seu triplo e sua raiz quadrada
def num_double_triple_and_squareroot():
    print('')
    print('Aqui iremos verificar o dobro, triplo e a raiz quadrada de um número inteiro')
    print('')
    num = int(input('Digite um número inteiro:'))
    print(f'O dobro de {num} é {num * 2}!\nO triplo é {num * 3}!\nE a raiz quadrada é {num ** (1 / 2)}!')


# Desafio7 Crie um programa que leia as notas do aluno e mostre sua média
def note_average():
    print('')
    print('Aqui iremos verificar a média das notas de um aluno')
    print('')
    b1 = float(input('Digite a nota do 1° Bimestre:'))
    b2 = float(input('Digite a nota do 2° Bimestre:'))
    b3 = float(input('Digite a nota do 3° Bimestre:'))
    b4 = float(input('Digite a nota do 4° Bimestre:'))
    average = (b1 + b2 + b3 + b4) / 4
    print('')
    print(f'A média do aluno foi {average}!')
    print('')


# Desafio8 Crie um programa em que ele leia em metros e transforme em centímetros ou milímetros
def m_em_cm_e_mm():
    print('')
    print('Conversor de Metros em Centímetros e Milímetros')
    print('')
    m = float(input('Digite a quantidade de metros:'))
    print(f'{m}m equivale a {m * 100}cm!\nE a {m * 1000}mm!')


# Desafio9 Faça um programa em que leia um número qualquer e mostre a sua tabuada
def num_tabuada():
    print('')
    print('Tabuada')
    print('')
    num = float(input('Digite um número qualquer:'))
    for i in range(0, 11):
        print(num * i)
    # Ou print(f'{num} x 1 = {num * }')
    #   print(f'{num} x 2 = {num * }') e assim por diante


# Desafio10 Crie um programa que mostre quantos reais ela tem na carteira e quantos dólares ela pode comprar
# considere $1=R$3,27
def real_em_dollar():
    print('')
    print('Real em Dólar')
    print('')
    real = float(input('Digite quantos reais você tem:'))
    print('')
    print(f'Você tem R${real}!\nE consegue comprar ${real / 3.27:.2f}!')


# Desafio11 Crie um programa que leia a largura e a altura de uma parede em metros, a quantidade de tinta necessária
# para pintar, sabendo que cada litro de tinta pinta 2m² de parede
def qnt_tinta():
    print('')
    print("Quantidade de tinta necessária para pintar a parede")
    print('')
    a = float(input('Digite a altura da parede em metros:'))
    l = float(input('Digite a largura da parede em metros:'))
    print('')
    print(f'A quantidade de tinta necessária será de {a * l / 2}L!')


# Desafio12 Faça um algorítimo que leia o preço de um produto e mostre o novo preço com 5% de desconto
def preco_e_5porcento():
    print('')
    print('Calculo do Valor - 5%')
    print('')
    preço = float(input('Digite o preço atual:'))
    print('')
    print(
        f'O valor do produto após o reajuste será de {preço - preço * 5 / 100 :.2f}!'
        f'\nO desconto foi de {preço * 5 / 100:.2f}!')


# Desafio13 Faça um algorítimo que leia o salário de um funcionário e mostre o novo preço com 15% de aumento
def salario_e_15porcento():
    print('')
    print('Salário atual + 15%')
    print('')
    satual = float(input('Digite o salário atual:'))
    print('')
    print(
        f'O seu salário após o reajuste será de {satual * 15 / 100 + satual:.2f}!'
        f'\nO aumento foi de {satual * 15 / 100:.2f}!')


# Desafio14 conversor de temperaturas(tem no celular)

# Desafio15 aluguel de carros em que o programa pergunte quantos km percorridos e quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por km percorrido.
def aluguel_car():
    print('')
    print('Valor Aluguel do Carro')
    print('')
    dias = int(input('Digite a quantidade de dias em que o carro ficará/ficou alugado:'))
    print('')
    km = float(input('Digite quantos KM foi percorrido/percorrerá neste período:'))
    print('')
    print(f'O valor a ser pago é R${(dias * 60) + (km * 0.15) :.2f}!\nR${dias * 60}'
          f' pelos dias alugados!\n10R${km * 0.15} pelos Km rodados!')

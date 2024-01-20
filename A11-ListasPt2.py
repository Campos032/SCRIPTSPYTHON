# Listas em listas ou Listas compostas
def ex1():
    dados = list()
    dados.append('Pedro')
    dados.append(25)
    pessoas = list()
    pessoas.append(dados[:])  # [:] è a lista completa
    print(pessoas)
    print(pessoas[0][10])


def ex2():
    teste = list()
    teste.append('Gustavo')
    teste.append(40)
    galera = list()
    galera.append(teste[:])
    print(teste)
    print(galera)
    teste[0] = 'Maria'
    teste[1] = 22
    galera.append(teste[:])
    print(teste)
    print(galera)


def ex3():
    galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
    print(galera[2][0])
    for p in galera:
        print(p)
        print(p[0])


def ex4():
    galera = list()
    dado = list()
    for c in range(0, 2):
        dado.append(str(input('Nome: ')))
        dado.append(int(input('Idade: ')))
        galera.append(dado[:])
        dado.clear()
    totmai = 0
    totmen = 0
    for p in galera:
        if p[1] >= 21:
            print(f'{p[0]} é maior de idade')
            totmai += 1
        else:
            print(f'{p[0]} é menor de idade.')
            totmen += 1
    print(f'Temos {totmai} maior(es) e {totmen} menor(es) de idade.')

# Dicionário também é uma variável composta, Tuplas () ou tuple() - Listas [] ou list() - Dicionários {} ou dict()
# Um dicionário é nada mais que uma lista de tuplas mutáveis
# Ao contrário de listas, nos dicionários nós não pegamos os índices por número e sim de acordo com aquilo que
# intitulamos a variável, como, por exemplo, variável 'nome': 'Gustavo', o dicionário seria pessoa = {'nome': 'Gustavo'}
# para printar na tela uma 'variável' do dicionário fazemos da seguinte maneira print(pessoa['nome'])
# ao contrario das listas, no dicionário criamos um novo elemento da seguinte forma, pessoa['idade'] = 25
# o dicionário é dividido da seguinte maneira em chaves e valores 'nome': 'Gustavo', nome é a chave e gustavo o valor
# print(pessoa.values()) nos mostrará Gustavo
# print(pessoa.key()) nos mostrará nome
# print(pessoa.items()) nos mostrara os itens
# teria como fazer como, por exemplo, o enumerate: for key, value in pessoa.items(): print(f'O {k} é {v}.')
# também é possível juntar dicionários a listas ou a tuplas, ficaria da seguinte maneira
# lista_pessoa = [{'nome': 'Gustavo', 'idade': 40}, {'nome': 'Carlos', 'idade': 30}]
# del pessoa["nome"] deletar o key
# pessoa["nome"] = 'Leandro' muda o valor da key

def ex1():
    pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 40}
    print(pessoa.values())
    print(pessoa.keys())
    print(pessoa.items())


def ex2():
    filme = {'titulo': 'Star Wars',
             'ano': 1984,
             'diretor': 'George Lucas'}
    print(f'O filme {filme["titulo"]} é do ano de {filme["ano"]}. ')  # O valor Tem que ser formatado com aspas duplas
    # se estiver dentro de aspas simples e vice-versa
    print(len(filme))


def ex3():
    lista = [{'nome': 'Gustavo', 'idade': 40}, {'nome': 'Carlos', 'idade': 30}]
    print(lista[0]['nome'])


def ex4():
    # Dicionários em listas
    lista_brasil = []
    estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
    estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
    lista_brasil.append(estado1.copy())
    print(lista_brasil)
    lista_brasil.append(estado2.copy())
    print(lista_brasil)
    print(f'O primeiro estado da lista é {lista_brasil[0]["uf"]} '
          f'e a sigla do segundo estado é {lista_brasil[1]["sigla"]}.')


def ex5():
    estado = dict()
    brasil = list()
    for c in range(0, 3):
        estado['uf'] = str(input('Unidade Federativa: '))
        estado['sigla'] = str(input('Sigla do Estado: '))
        brasil.append(estado.copy())  # Para fazer cópias de listas nos utilizamos [:], em dicionários utilizamos copy()
    for e in brasil:
        # for k, v in e.items():
        # print(f'O campo {k} tem valor {v}.')
        for v in e.values():
            print(v, end=' ')
        print()

lista = [{'carlos': 2}]
print(lista[0]['carlos'])
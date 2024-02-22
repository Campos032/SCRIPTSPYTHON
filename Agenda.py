agenda = []
contatos_favoritos = []


def adicionar_contato():
    print()
    pessoa = dict()
    nome = str(input('Escreva o nome do contato: '))
    pessoa = {'Nome': f'{nome}', 'Telefone': str(input('Digite o telefone: ')),
              'Email': str(input('Digite o email: '))}
    agenda.append(pessoa.copy())
    pessoa.clear()
    print()


def mostrar_agenda():
    print()
    if not agenda:
        print(15 * ' ', 'Agenda Vazia')
        print()
        return
    print(21 * ' ', 'Agenda')
    print()
    print('Nome'.ljust(20), 'Telefone'.ljust(20), 'Email'.ljust(20))
    print(47 * '-')
    for item in agenda:
        print(item['Nome'].ljust(20), item['Telefone'].ljust(20), item['Email'].ljust(20))
    print()


def atualizar_contato():
    print()
    if not agenda:
        print(15 * ' ', 'Agenda Vazia')
        print()
        return
    nome_contato = str(input('Digite o nome do contato que você quer atualizar: '))
    for item in agenda:
        if item['Nome'] == nome_contato:
            item['Nome'] = str(input('Digite o nome: '))
            item['Telefone'] = str(input('Digite o telefone: '))
            item['Email'] = str(input('Digite o email: '))
    print()


def remover_contato():
    print()
    if not agenda:
        print(15 * ' ', 'Agenda Vazia')
        print()
        return
    nome_contato = str(input('Digite o nome do contato que você quer apagar: '))
    for item in agenda:
        if item['Nome'] == nome_contato:
            del item
    print()


def favoritar_contato():
    print()
    if not agenda:
        print(15 * ' ', 'Agenda Vazia')
        print()
        return
    nome = str(input('Digite o contato que você quer favoritar: '))
    for item in agenda:
        if item['Nome'] == nome:
            contatos_favoritos.append(item.copy())


def remover_favorito():
    print()
    if not contatos_favoritos:
        print(15 * ' ', 'Nenhum Favorito')
        print()
        return
    nome = str(input('Digite o contato que você quer favoritar: '))
    for item in contatos_favoritos:
        if item['Nome'] == nome:
            contatos_favoritos.remove(item)


def mostrar_favoritos():
    print()
    if not contatos_favoritos:
        print(15 * ' ', 'Nenhum Favorito')
        print()
        return
    print(17 * ' ', 'Agenda Favoritos')
    print()
    print('Nome'.ljust(20), 'Telefone'.ljust(20), 'Email'.ljust(20))
    print(47 * '-')
    for item in agenda:
        print(item['Nome'].ljust(20), item['Telefone'].ljust(20), item['Email'].ljust(20))
    print()


while True:
    choice = int(input('1 - Adicionar contato'
                       '\n2 - Ver Agenda'
                       '\n3 - Atualizar Contato'
                       '\n4 - Remover Contato'
                       '\n5 - Favoritar Contato'
                       '\n6 - Remover Contato Dos Favoritos'
                       '\n7 - Ver Contatos Favoritos'
                       '\n8 - Sair'
                       '\n'
                       '\nEscolha uma opção: '))

    if choice == 8:
        break
    elif choice == 1:
        adicionar_contato()
    elif choice == 2:
        mostrar_agenda()
    elif choice == 3:
        atualizar_contato()
    elif choice == 4:
        remover_contato()
    elif choice == 5:
        favoritar_contato()
    elif choice == 6:
        remover_favorito()
    elif choice == 7:
        mostrar_favoritos()

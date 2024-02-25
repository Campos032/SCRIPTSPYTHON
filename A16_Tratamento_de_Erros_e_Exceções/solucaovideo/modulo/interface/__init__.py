def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[035m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt(f'\033[32mSua opção: \033[m')
    return opcao

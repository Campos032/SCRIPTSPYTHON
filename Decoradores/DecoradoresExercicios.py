# Cronômetro de Função: Crie um decorador que calcule o tempo de execução de uma função e imprima o tempo necessário
# para a execução.
import getopt
import time


def cronometro_de_funcao(funcao):
    def cronometro(*args, **kwargs):
        inicio = time.time()
        exec_funcao = funcao(*args, **kwargs)
        fim = time.time()
        tempo_de_exec = fim - inicio
        return tempo_de_exec

    return cronometro


@cronometro_de_funcao
def conta_numero(*args):
    for numero in args:
        for num in numero:
            print(num)


# numeros = list(x for x in range(100000))
# print(conta_numero(numeros))


# Validação de Parâmetros: Crie um decorador que valide os parâmetros de entrada de uma função de acordo com
# determinados critérios (por exemplo, garantir que um argumento seja um número positivo).
def input_validator(type_validator='inteiro'):
    def validators(funcao):
        def int_validator(*args):
            if len(args) == 0:
                return KeyboardInterrupt('Nenhum valor foi inserido.')
            try:
                for num in args:
                    if not isinstance(num, int):
                        raise ValueError('Erro, tipo de dado inserido é inválido!')
            except ValueError as erro:
                return f'{erro}'
            else:
                resultado_da_funcao = funcao(*args)
                return f'Executada, com sucesso! O resultado é {resultado_da_funcao}'

        def float_validator(*args):
            if len(args) == 0:
                return KeyboardInterrupt('Nenhum valor foi inserido.')
            try:
                for num in args:
                    if not isinstance(num, float):
                        raise ValueError('Erro, tipo de dado inserido é inválido!')
            except ValueError as erro:
                return f'{erro}'
            else:
                resultado_da_funcao = funcao(*args)
                return f'Executada, com sucesso! O resultado é {resultado_da_funcao}'

        if type_validator == 'inteiro':
            return int_validator
        elif type_validator == 'decimal':
            return float_validator

    return validators


@input_validator('inteiro')
def teste1(*args):
    return sum(args)


# vart1_1 = teste1(22, 32, 33, 42, 5)
# vart1_2 = teste1(22.0, 32.0, 33, 42, 5)
# print(vart1_1)
# print(vart1_2)


@input_validator('decimal')
def teste2(*args):
    return sum(args)


# vart2_1 = teste2(22.4, 32.35, 33.2345, 42.2, 5.110)
# vart2_2 = teste2(22.0, 32.0, 33.0, 42, 5)
# print(vart2_1)
# print(vart2_2)


# Autenticação: Crie um decorador que verifique se o usuário está autenticado antes de chamar uma função que requer
# autenticação.
usuario = {'usuario': 'Júnior', 'email': 'marciocamposjunior@gmail.com', 'senha': '12345'}


def autenticador(funcao):
    def verifica_na_variavel(email, senha):
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f'Acesso Permitido para usuário {usuario["usuario"]}')
            return funcao(email, senha)
        else:
            return print(f'Acesso Negado, Email ou Senha estão incorretos')

    return verifica_na_variavel


@autenticador
def user_actions(email, senha):
    def escolha():
        escolha_user = int(input('1 - Mudar Nome'
                                 '\n2 - Mudar Email'
                                 '\n3 - Mudar Senha'
                                 '\n4 - Ver Informações Da Conta'
                                 '\n5 - Sair'
                                 '\nEscolha uma ação: '))
        return escolha_user

    while True:
        choice = escolha()
        if choice == 5:
            print('Saindo...')
            print()
            return
        elif choice == 1:
            usuario['nome'] = str(input('Digite o novo nome de usuário: '))
            print(f'Novo nome cadastrado com sucesso!\n')
        elif choice == 2:
            usuario['email'] = str(input('Digite o novo nome de email: '))
            print(f'Novo email cadastrado com sucesso!\n')
        elif choice == 3:
            usuario['senha'] = str(input('Digite a nova senha: '))
            print(f'Nova senha cadastrada com sucesso!\n')
        elif choice == 4:
            print()
            for chave, valor in usuario.items():
                print(f"{chave.title()}: {valor}")
            print()


# user_actions('marciocamposjunior@gmail.com', '12345')  # Dará acesso ao usuário
# usuario = {'usuario': 'Júnior', 'email': 'marciocamposjunior@gmail.com', 'senha': '1234'}
# user_actions('marciocamposjunior@gmail.com', '12345')  # O usuário não terá acesso


# O mesmo exercício acima, mas, utilizando de classes

def autentica_classe(funcao):
    def autenticador_2(instancia, email_log, senha_log):
        if instancia._UserAccount__email == email_log and instancia._UserAccount__senha == senha_log:
            print(f'Acesso Permitido para usuário {instancia.username}')
            return funcao(instancia, email_log, senha_log)
        else:
            return print('Acesso Negado, Email ou Senha estão incorretos')
    return autenticador_2


class UserAccount:
    def __init__(self, username: str, email: str, senha: str):
        self.username = username
        self.__email = email
        self.__senha = senha

    @autentica_classe
    def login(self, email_log: str, senha_log: str):
        return f'{self.username} {email_log} {senha_log}'
# usuario1 = UserAccount('carlos', 'carlos@', 'asdasd')
# resultado = usuario1.login('carlos@', 'asdasd')
# print(resultado)


# Cache de Função: Crie um decorador que armazene em cache o resultado de uma função para evitar cálculos repetidos se
# os mesmos argumentos forem passados novamente.
cache = {}


def guarda_cache(funcao):
    def armazena(*args):
        if tuple(sorted(args)) in cache.keys():
            print('Está no cache')
            return f"A soma de {args} é igual a {cache[tuple(sorted(args))]}"
        else:
            print('Não está no cache')
            cache[tuple(sorted(args))] = funcao(*args)
            return f"A soma de {args} é igual a {cache[tuple(sorted(args))]}"
    return armazena


@guarda_cache
def soma(*args):
    return sum(args)
# print(soma(1, 2))
# print(soma(1, 2))
# print(soma(3, 2))
# print(soma(2, 3))


# Contagem de Chamadas: Crie um decorador que mantenha a contagem de quantas vezes uma função é chamada e imprima a
# contagem após cada chamada.
def conta_chamadas(funcao):
    def contador(*args):
        contador.num += 1  # Atribui à função interna, não à variável global
        print(f'A função foi chamada {contador.num} vez')
        return funcao(*args)

    contador.num = 0  # Inicializa o contador para a função interna
    return contador


@conta_chamadas
def funcao_chamar(*args):
    return 'Certo'
# print(funcao_chamar())
# print(funcao_chamar())

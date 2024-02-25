# Desafio 113 Reescreva a função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leia_int_g():
    def leia_int(num):
        try:
            inteiro = int(input(num))
        except ValueError:
            print('Erro, tipo de dado inserido é inválido!')
            return leia_int(num)
        except KeyboardInterrupt:
            print('Usuário não inseriu nenhum valor.')
            return leia_int(num)
        else:
            return inteiro

    numero = leia_int('Digite um valor: ')
    print(numero, 'É um número inteiro!')


def leia_float_g():
    def leia_float(num):
        flutuante = input(num)
        try:
            if '.' in flutuante:
                flutuante = float(flutuante)
        except ValueError:
            print('Erro, tipo de dado inserido é inválido!')
            return leia_float(num)
        except KeyboardInterrupt:
            print('Usuário não inseriu nenhum valor.')
            return leia_float(num)
        else:
            return flutuante

    numero = leia_float('Digite um valor: ')
    print(numero, 'É um número decimal!')


# Desafio 114 Crie um código em Python que A16_Tratamento_de_Erros_e_Exceções se o site Pudim está acessível pelo
# computador usado.
# https://pudim.com.br
def desafio114():
    import requests
    import webbrowser

    def verificar_url(url):
        try:
            response = requests.get(url)
            print(response)
            webbrowser.open('https://pudim.com.br')
            # response.raise_for_status()  # Lança uma exceção se o status da resposta for um erro
            print(f"A URL {url} está acessível.")
        except requests.ConnectionError:
            print(f"A URL {url} não está acessível: Erro {ConnectionError}")

    verificar_url('https://pudim.com.br')


# Desafio 115 Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de
# texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

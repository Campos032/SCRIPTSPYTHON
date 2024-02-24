# Interactive Help(Ajuda interativa)
# help()  # Usado para acessar a funcionalidade de algo no python, help inicia um terminal exclusivo, para sair digite
# quit


# Docstrings(String de documentação)
def exemplo_docstring():
    """
    -> Exemplo de uma docstring.
    : exemplo docstring nao recebe nenhum parâmetro
    : ela apenas executa o comando print
    """
    print()


# Argumentos opcionais
def somar(a1=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    : A - primeiro valor
    : B - segundo valor
    : C - terceiro valor
    Função de Teste
    """
    soma = a1 + b + c
    print(soma)


# somar(1, 2)


# Escopo de variáveis
def teste():
    x = 8  # É uma variável local
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


# Programa principal
n = 2  # 'n' é uma variável global


# print(f'No programa principal, n vale {n}.')
# teste()
# print(f'No programa principal, x vale {x}.')


def teste2(b):
    p1 = 8  # Variável local, então teremos duas variáveis A, uma global e uma local
    b += 4
    c = 2
    print(f'A dentro vale {p1}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a2 = 5  # Variável global


# teste2(a)


def teste3(p2):
    p2 = 2
    print(p2)


a3 = 1


# teste3(a)
# print(a)


def teste4(b):
    global a4  # Utilizando a palavra reservada global, nós utilizaremos a variável global A
    a4 = 8
    b += 4
    c = 2
    print(f'A dentro vale {a4}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a4 = 5  # Variável global


# print(a)
# teste4(a)
# print(a)  # Aqui A irá deixar de valer 5 e irá valer 8 


# Retorno de Resultados / Funções com retorno
def somar2(a=0, b=0, c=0):
    soma = a + b + c
    return soma


resposta1 = somar2(3, 2, 5)
resposta2 = somar2(2, 2)
resposta3 = somar2(6)
print(f'Os resultados foram {resposta1}, {resposta2}, {resposta3}.')


# Exemplos
def fatorial(num1=1):
    f = 1
    for c in range(num1, 0, -1):
        f += c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')


def par_ou_impar(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par_ou_impar(num):
    print(f'{num} é um número par.')
else:
    print(f'{num} é um número ímpar.')

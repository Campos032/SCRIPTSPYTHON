# Interactive Help(Ajuda interativa)
# help()  # Usado para acessar a funcionalidade de algo no python, help inicia um terminal exclusivo, para sair digite quit
# ou help(print), help(input) ou print(input.__doc__)


# Docstrings(String de documentação)
def exemplo_docstring():
    '''
    -> Exemplo de uma docstring.
    : exemplo docstring nao recebe nehum parametro
    : ela apenas execunta o comando print 
    '''
    print()


# Argumentos opcionais
def somar(a=0, b=0, c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    : A - primeiro valor
    : B - segundo valor
    : C - terceiro valor 
    Função de Teste
    '''
    soma = a + b + c
    print(soma)
# somar(1, 2)


# Escopo de variáveis
def teste():
    x = 8  # É  uma variável local
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')
# Programa principal
n = 2  # n é uma variável global
# print(f'No programa principal, n vale {n}.')
# teste()
# print(f'No programa principal, x vale {x}.')


def teste2(b):
    a = 8  # Variável local, então teremos duas variáveis A, uma global e uma local
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')
a = 5  # Variável global
# teste2(a)


def teste3(a):
    a = 2
    print(a)
a = 1
# teste3(a)
# print(a)


def teste4(b):
    global a  #  Utilizando a palavra reservada global, nós utilizaremos a variável global A
    a = 8  
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')
a = 5  # Variável global
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
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f += c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')


def parOuImpar(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if parOuImpar(num):
    print(f'{num} é um número par.')
else:
    print(f'{num} é um número ímpar.')

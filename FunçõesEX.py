# Funções sem parâmetros e com retorno
def saudacao():
    return "Olá, mundo!"


mensagem = saudacao()


# print(mensagem)


# Funções com parâmetros e sem retorno:
def somar(a, b):
    resultado1 = a + b
    print(f"A soma de {a} e {b} é: {resultado1}")


somar(3, 5)


# Funções com parâmetros e retorno:
def elevar_quadrado(numero):
    return numero ** 2


resultado = elevar_quadrado(4)
print(f"O quadrado de 4 é: {resultado}")


# Funções com parâmetros padrão
def saudacao_personalizada(nome, saudacao1="Olá"):
    return f"{saudacao1}, {nome}!"


mensagem1 = saudacao_personalizada("João")
print(mensagem1)


# Funções com parâmetros variáveis (*args)
def somar_variavel(*args):
    return sum(args)


resultado = somar_variavel(1, 2, 3, 4, 5)
print(f"A soma dos valores é: {resultado}")


# Funções com parâmetros-chave-valor (**kwargs)
def info_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


info_pessoa(nome="Maria", idade=25, cidade="São Paulo")


# Funções com docstrings:
def calcular_media(notas):
    """
    Calcula a média de uma lista de notas.

    Args:
        notas (list): Lista de notas dos alunos.

    Returns:
        float: Média das notas.
    """
    return sum(notas) / len(notas)


notas_aluno = [8, 7, 9, 10]
media = calcular_media(notas_aluno)
print(f"A média é: {media}")


# Funções com variáveis globais e locais:
variavel_global = 10


def multiplicar_por_global(numero):
    global variavel_global
    resultado2 = numero * variavel_global
    return resultado2


resultado_final = multiplicar_por_global(5)
print(f"O resultado é: {resultado_final}")


# Função principal (main):
def main():
    print("Este é o código principal.")


if __name__ == "__main__":
    main()


# Funções com manipulação de listas:
def dobrar_elementos(lista):
    return [elemento * 2 for elemento in lista]


lista_original = [1, 2, 3, 4]
nova_lista = dobrar_elementos(lista_original)
print(f"Lista original: {lista_original}")
print(f"Nova lista: {nova_lista}")


# Funções que retornam múltiplos valores:
def calcular_estatisticas(valores):
    media1 = sum(valores) / len(valores)
    soma1 = sum(valores)
    return media1, soma1


dados = [10, 15, 20, 25, 30]
media, soma = calcular_estatisticas(dados)
print(f"Média: {media}, Soma: {soma}")


# Funções recursivas:
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


resultado = fatorial(5)
print(f"O fatorial de 5 é: {resultado}")

# Funções lambda (funções anônimas):
quadrado = lambda x: x ** 2
print(f"O quadrado de 4 é: {quadrado(4)}")

soma = lambda x, y: x + y
print(f"A soma de 3 e 5 é: {soma(3, 5)}")


# Funções com tratamento de exceções
def dividir(a, b):
    try:
        resultado2 = a / b
        return resultado2
    except ZeroDivisionError:
        return "Não é possível dividir por zero."


resultado_divisao = dividir(10, 2)
print(f"Resultado da divisão: {resultado_divisao}")

resultado_divisao_por_zero = dividir(5, 0)
print(f"Resultado da divisão por zero: {resultado_divisao_por_zero}")


# Funções com argumentos opcionais:
def cumprimento(nome, saudacao1="Olá", exclamacao=False):
    mensagem2 = f"{saudacao1}, {nome}{'!' if exclamacao else ''}"
    return mensagem2


print(cumprimento("Alice"))
print(cumprimento("Bob", saudacao1="Oi"))
print(cumprimento("Charlie", exclamacao=True))


# Funções com manipulação de strings:
def inverter_string(texto):
    return texto[::-1]


string_original = "Python é divertido"
string_invertida = inverter_string(string_original)
print(f"Original: {string_original}")
print(f"Invertida: {string_invertida}")


# Funções com retorno condicional:
def verificar_paridade(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"


print(verificar_paridade(4))
print(verificar_paridade(7))


# Funções com uso de *args e **kwargs
def imprimir_argumentos(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos de palavra-chave:", kwargs)


imprimir_argumentos(1, 2, 3, nome="Ana", idade=30)


# Funções que modificam objetos mutáveis
def adicionar_elemento(lista, elemento):
    lista.append(elemento)


minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista, 4)
print(f"Lista modificada: {minha_lista}")


# Funções que recebem funções como argumento (funções de ordem superior)
def aplicar_operacao(func, x, y):
    return func(x, y)


def soma(a, b):
    return a + b


def multiplicacao(a, b):
    return a * b


print(aplicar_operacao(soma, 3, 4))
print(aplicar_operacao(multiplicacao, 2, 5))


# Funções com retorno de funções
def criar_funcao_potencia(n):
    def potencia(x):
        return x ** n

    return potencia


quadrado = criar_funcao_potencia(2)
cubo = criar_funcao_potencia(3)

print(quadrado(5))
print(cubo(2))

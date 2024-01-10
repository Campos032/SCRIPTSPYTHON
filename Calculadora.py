print('Calculadora em Python')
print('')


# print é usado para imprimir algo na tela do usuário
# def é uma função do python usada para criar outra função que não seja existente na linguagem
# print(f'') usado para imprimir as variáveis no seu print
def soma():
    print('')
    print('A soma entre dois números é igual a')
    n1 = float(input('Digite o 1° número:'))
    n2 = float(input('Digite o 2° número:'))
    resultso = n1 + n2
    # colocar as variáveis dentro de chaves ao usar print(f)
    print(f'O resultado da soma entre {n1} e {n2} é igual a {resultso}!')
    print('')


def subtração():
    print('')
    print('A subtração entre dois números é igual a')
    n1 = float(input('Digite o 1° número:'))
    n2 = float(input('Digite o 2° número:'))
    resultsu = n1 - n2
    print(f'O resultado da soma entre {n1} e {n2} é igual a {resultsu}!')
    print('')


def multiplicação():
    print('')
    print('A multiplicação entre dois números é igual a')
    n1 = float(input('Digite o 1° número:'))
    n2 = float(input('Digite o 2° número:'))
    resultm = n1 * n2
    print(f'O resultado da multiplicação entre {n1} e {n2} é igual a {resultm}!')
    print('')


# float foi usado para salvar números flutuante(float é um tipo primitivo)
def divisão():
    print('')
    print('A divisão entre dois números é igual a')
    n1 = float(input('Digite o 1° número:'))
    n2 = float(input('Digite o 2° número:'))
    if n2 == 0:
        print('Divisão por zero não é possível!')
        print('')
        return
    # return foi usado como repetidor, para retornar o programa já que foi encontrado algo não possível de ser feito
    resultd = n1 / n2
    print(f'O resultado da divisão entre {n1} e {n2} é igual a {resultd}!')
    print('')


# while true(quando verdadeiro repetir) foi usado como estrutura de repetição/loop(while e true são palavras chave)
while True:
    print('Escolha uma das ações a seguir')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print("5 - Sair")
    print('')
    # int foi usado para salvar números inteiros(int é um tipo de variável/tipo primitivo)
    escolha = int(input('Digite um número de acordo com a operação que você deseja:'))
    # if/elif/else são as condições usadas para se/senão/não(são palavras chave)
    # para comparar usamos ==(igual) >=(maior ou igual) <=(menor ou igual) >(maior) <(menor)
    # break foi usado para interromper o código(e é uma palavra chave)
    if escolha == 5:
        print('')
        print('Saindo!')
        break

    elif escolha == 1:
        soma()

    elif escolha == 2:
        subtração()

    elif escolha == 3:
        multiplicação()

    elif escolha == 4:
        divisão()

    else:
        print('Escolha inválida tente novamente!')

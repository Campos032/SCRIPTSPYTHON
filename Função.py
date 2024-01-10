# Programa Principal
print("........................")
print("Esse é o primeiro exemplo de função")


def soma(a, b):
    s = a + b
    print(s)


soma(5, 6)
print(".")
soma(7, 9)
print(".")
soma(a=0, b=7)
print(".")
soma(4.2, 9.5)
print(".")
print(".")
print("Essa foi a primeira função")
print("........................")
print(" ")
print(" ")

print("........................")
print("Esse é o segundo exemplo de função")


def soma2(a, b):
    print(f"A={a} e B={b}")
    s = a + b
    print(f"A soma entre A e B é igual a {s}")


soma2(a=1, b=3.5)
print(".")
print(".")
soma2(5, 6.7)
print(".")
print(".")
print("Esse foi o segundo exemplo de função")
print("........................")


def soma3():
    print(' ')
    print(' ')
    print("-" * 30)
    n1 = float(input('Digite algum número:'))
    n2 = float(input('Digite outro número qualquer:'))
    result = n1 + n2
    print(f"A soma entre A e B é igual a {result}")
    print("-" * 30)
    print('')
    print('')


soma3()
print("")
print("")
print("")


# Essa é uma função sem parâmetro e todas as outras com parâmetros
def lin():
    print("-----------------------")


lin()
print('Meu nome é Márcio Campos Júnior')
lin()
print('Estou aprendendo a programar, mais especificamente aprendendo sobre funções')
lin()


def titulo(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)


titulo('My name is')


# Aqui iremos empacotar parâmetros(* x), uma das exclusividades do python e que eu não tenho certeza se mais alguma
# linguagem possui essa função, ele irá se virar para verificar quantos parâmetros foi adicionado a linha
def contador(*num):
    print(num)


contador(5, 5, 6, 7, 8)
contador(2, 3.4, 5, 9.8)
contador(2, 3)


# para cada valor em num fazer escrever o valor em linha
def contador1(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


contador1(5, 5, 6, 7, 8)
contador1(2, 3.4, 5, 9.8)
contador1(2, 3)


# A função len, quando aplicada a uma string, retorna o número de caracteres da string (ou seja, o seu comprimento).
def contador2(*num1):
    tam = len(num1)
    print(f'Recebi os valores {num1} e são ao todo {tam} números!')


contador2(5, 5, 6, 7, 8)
contador2(2, 3.4, 5, 9.8)
contador2(2, 3)

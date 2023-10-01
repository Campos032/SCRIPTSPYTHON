#Podemos usar os operados aritméticos para formatação de str e aqui teremos alguns exemplos como por exemplo
print('30' * 30)
#E também temos que saber que no python tem formas diferentes de se formatar uma str dependendo da versão ,na 3.6 adiante podemos usar o
#print(f''), já anteriormente usava-se .format(x, y, u), e ainda mais antes usava-se por exemplo %f para float e %d para int
print()
#No print f podemos fazer do seguinte jeito [print(f'Seu {nome:20}')Isso irá escrever o nome em 20 espaços]
#Se usarmos {nome:<20} Isso irá alinhar a esquerda e criar 20 espaços depois
#Se usarmos {nome:>20} Isso irá alinhar a direita e criar 20 espaços antes
#Se usarmos {nome:^20} Isso irá centralizar nome, e também podemos usar nome:-^20 que irá preencher os espaços e centralizar nome
#Podemos utilizar {soma:.4f} para limitar a 4 casas decimais o resultado
#Para não quebrar a linha utilizamos end=''
#Para quebrar linha utilizamos \n, por exemplo print(f'O nome dela é \n Joana ')
nome = 'Júnior'
idade = 18  
print(f'Meu nome é \nJúnior \ne tenho 18 anos',end='!')
print('')
#Podemos utilizar aspas triplas para escrever um multilinhas já com quebra de linhas
mensagem = ''' 
O python realmente é muito legal
Mas também muito versátil
Eu recomendo
'''
print(mensagem)

def f1():
    print('')
    print('Iremos fazer alguns calculos com dois números!')
    print('')
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número:'))
    print('')
    s = n1 + n2
    sb = n1 - n2
    m = n1 * n2
    d = n1 / n2
    p = n1 ** n2
    di = n1 // n2
    dr = n1 % n2
    print(f'A soma entre {n1} e {n2} é igual a {s}!\nA subtração é igual á {sb}!\nA multiplicação é igual á {m}!\nA divisão é igual a {d}!\nA potência é igual a {p}!\nA divisão inteira é igual a {di}!\nE o resto da divisão é igual a {dr}!')



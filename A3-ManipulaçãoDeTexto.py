#Fatiamento

frase = 'Pythonn'
        #0123456 Esses são os microespaços que está armazenada a STR
print(frase) # Apenas vai printar a frase
print(frase[4])# Vai mostrar o índice 4 da STR
print(frase[:5])# Vai mostrar todos até o 5 exceto o 5
print(frase[0:3])# Vai mostrar todos do 0 ao 2 exceto o 3
print(frase[1:5])#Vai mostrar todos do 1 ao 4
print(frase[0:7:2])#Vai mostrar do 0 ao 6, contando a cada 2
print(frase[0:])#Vai mostrar todos a partir do zero
print(frase[0::2])#Vai mostrar do 0 ao 6, contando a cada 2

#Análise

frase2 = 'Python é intuitivo'
         #0123456

#len() retorna o número de caractéres em uma str
len(frase2)

#frase2.count('o') retorna a quantidade do parâmetro que você utilizou e frase2.count('o',0,13) vai mostrar quantas letras O tem de 0 a 13 exceto 13
print(frase2.count('y'))
print(frase2.count('P',1,7))

#frase2.find('Pyt') vai procurar se existe esse parâmetro na str e falar o índice em que ele começa
print(frase2.find('Pyt'))
print(frase2.find('Android')) #quando não existe na str a função retorna -1

#pode-se usar 'Pyt' in frase2(existe pyt em frase2?) e retornará true ou false, (in) é um operador e não uma função
print('Pyt' in frase2)

#Transformação

print(frase2.replace('Pyt','Day'))#isso irá trocar um pelo outro criando umanova string e não mudando a antiga
print(frase2.upper())#upper transformará todas as letras em maiúsculas
print(frase2.lower())#e lower em minúsculas
print(frase2.capitalize())#capitalize transformará apenas a 1.º letra da str em maiúscula
print(frase2.title())#title transormará todas as letras no início de cada palavra em maiúsculas
print(frase2.strip())#strip(rstrip removerá apenas os espaços da esquerda e lstrip removerá apenas os sepaços da esquerda) remove todos os espaços inúteis em uma str, tanto no começo da quanto no final

#Divisão

print(frase2.split())#split divide a str conforme o parâmetro que voce utilizou

#Junção

print('-'.join(frase2.split()))#join irá juntar/mudar os espaços por -

#uso das aspas triplas

print('''Seja bem vindo ao python
A aula de formatação de string
E continue a estudar''')


#Biblioteca Doces(Pudim, bala e etc)   Comida(Pizza, Arroz e etc)  Bebidas(Refrigerante, cerveja e etc)
#Para adicionar uma biblioteca no programa utilizamos import x (import doces)
#Se eu quiser adicionar apenas um item da biblioteca eu utilizo (from doces import pudim)
#Para buscar informações podemos ir no site python.org mais especificamente em docs
#Clicando no ctrl+space após o import conseguiremos visualizar todas as bibliotecas disponíveis sendo elas próprias do python ou externa 

import math #Biblioteca matemática ou por exemplo from math import sqrt para importar apenas uma funcionalidade, para importar mais de uma usa-se ,
#se importarmos apenas uma funcionalidade formatamos a string da seguinte forma (raiz = sqrt(num)) , se importarmos a biblioteca inteira utilizamos (raiz = math.sqrt(num))

num = int(input('Digite um número qualquer para obter sua raiz quadrada:'))
print(f'A raiz quadrada de {num} é {math.sqrt(num)}!')


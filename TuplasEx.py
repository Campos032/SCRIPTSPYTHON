# As tuplas em Python são estruturas de dados imutáveis e ordenadas. Aqui estão alguns exemplos de comandos que podem
# ser usados com tuplas:

# Criar uma Tupla:
minha_tupla = (1, 2, 3, 'a', 'b', 'c')

# Acessar Elementos:
primeiro_elemento = minha_tupla[0]
segundo_elemento = minha_tupla[1]

# Fatiar uma Tupla:
sub_tupla = minha_tupla[2:5]  # Retorna (3, 'a', 'b')

# Verificar Se um Elemento Existe:
existe_elemento = 'a' in minha_tupla

# Comprimento da Tupla:
tamanho_tupla = len(minha_tupla)

# Concatenar Tuplas:
nova_tupla = minha_tupla + (4, 5, 6)

# Repetir Elementos:
tupla_repetida = (1, 2) * 3  # Retorna (1, 2, 1, 2, 1, 2)

# Encontrar o Índice de um Elemento:
indice_a = minha_tupla.index('a')  # Retorna o índice do primeiro 'a'

# Contar a Ocorrência de um Elemento:
contagem_a = minha_tupla.count('a')  # Retorna o número de ocorrências de 'a'

# Desempacotar uma Tupla:
a, b, c = minha_tupla[:3]  # Desempacota os três primeiros elementos

# Lembre-se de que, como as tuplas são imutáveis, você não pode modificar seus elementos após a criação. Caso precise
# de uma estrutura de dados mutável, considere usar listas em vez de tuplas.

# Criar uma Tupla Vazia:
tupla_vazia = ()

# Criar uma Tupla com um Único Elemento (necessário vírgula):
tupla_com_um_elemento = (42,)

# Desempacotar Elementos no Final da Tupla:
primeiro, *restante = minha_tupla  # Desempacota o primeiro elemento e o restante como uma lista

# Verificar o Máximo e Mínimo de uma Tupla de Números:
max_valor = max((1, 2, 3, 4, 5))
min_valor = min((1, 2, 3, 4, 5))

# Converter uma Lista em Tupla:
lista = [1, 2, 3]
tupla_da_lista = tuple(lista)

# Iterar sobre uma Tupla:
for elemento in minha_tupla:
    print(elemento)

# Verificar se Todos os Elementos Atendem a uma Condição:
todos_positivos = all(x > 0 for x in minha_tupla)

# Verificar se Pelo Menos um Elemento Atende a uma Condição:
algum_positivo = any(x > 0 for x in minha_tupla)

# Converter uma Tupla em uma String:
tupla_string = str(minha_tupla)

# Ordenar uma Tupla de Números:
tupla_ordenada = tuple(sorted((3, 1, 4, 1, 5, 9, 2, 6, 5)))

# Verificar a Existência de uma Tupla Dentro de Outra:
tupla_contida = (1, 2) in ((1, 2), (3, 4), (5, 6))

# Criar uma Tupla a partir de Variáveis:
x = 10
y = 20
tupla_variaveis = (x, y)

# Criar uma Tupla com Range de Números:
tupla_range = tuple(range(1, 6))  # Retorna (1, 2, 3, 4, 5)

# Remover uma Tupla Específica de uma Lista de Tuplas:
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
lista_sem_tupla = [tupla for tupla in lista_tuplas if tupla != (3, 4)]

# Inverter uma Tupla:
tupla_invertida = minha_tupla[::-1]

# Encontrar a Soma de uma Tupla de Números:
soma_tupla = sum((1, 2, 3, 4, 5))

# Usar a Função map para Operar em Cada Elemento da Tupla:
tupla_dobrada = tuple(map(lambda x: x * 2, (1, 2, 3, 4, 5)))

# Verificar se uma Tupla é Vazia:
tupla_vazia = ()
esta_vazia = not bool(tupla_vazia)

# Utilizar a Função zip para Combinação de Tuplas:
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_combinada = tuple(zip(tupla1, tupla2))  # Retorna ((1, 'a'), (2, 'b'), (3, 'c'))

# Concatenar Diversas Tuplas:
tupla_concatenada = (1, 2) + (3, 4) + (5, 6)

# Unir Diversas Tuplas Utilizando o Operador +:
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla3 = ('x', 'y', 'z')
tupla_unida = tupla1 + tupla2 + tupla3

# Converter uma String em uma Tupla de Caracteres:
string = "Python"
tupla_de_chars = tuple(string)

# Criar uma Tupla com Números Aleatórios:
import random

tupla_aleatoria = tuple(random.randint(1, 100) for _ in range(5))

# Remover um Elemento Específico de uma Tupla:
tupla_original = (1, 2, 3, 4, 5)
elemento_removido = 3
tupla_sem_elemento = tuple(x for x in tupla_original if x != elemento_removido)

# Usar a Função enumerate com Tuplas:
tupla_palavras = ('maçã', 'banana', 'laranja')
for indice, palavra in enumerate(tupla_palavras):
    print(f"Índice {indice}: {palavra}")

# Criar uma Tupla de Tuplas (Tupla Aninhada):
tupla_aninhada = ((1, 2), ('a', 'b'), (True, False))

# Realizar Operações Matemáticas com Elementos da Tupla:
tupla_numeros = (2, 4, 6, 8, 10)
tupla_dobro = tuple(x * 2 for x in tupla_numeros)

# Copiar uma Tupla:
tupla_original = (1, 2, 3)
tupla_copia = tuple(tupla_original)

# Verificar se Todas as Tuplas em uma Lista têm o Mesmo Comprimento:
lista_de_tuplas = [(1, 2), ('a', 'b'), (True, False)]
mesmo_comprimento = all(len(tupla) == len(lista_de_tuplas[0]) for tupla in lista_de_tuplas)

# Filtrar Elementos de uma Tupla com a Função filter:
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_pares = tuple(filter(lambda x: x % 2 == 0, tupla_numeros))

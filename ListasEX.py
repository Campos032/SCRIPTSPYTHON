from collections import deque
import itertools
from collections import Counter
import numpy as np


# Adicionar Elementos:
# Adicionar um elemento ao final da lista:
frutas = ['maçã', 'banana', 'laranja']
# frutas.append('morango')

# Inserir um elemento em uma posição específica:
frutas.insert(1, 'kiwi')  # Insere 'kiwi' na posição 1

# Remover Elementos:
# Remover um elemento pelo valor:
frutas.remove('laranja')

# Remover um elemento pela posição:
del frutas[1]  # Remove o elemento na posição 1 (índice 1)

# Remover e retornar o último elemento:
ultimo_elemento = frutas.pop()

# Ordenação:
# Ordenar a lista em ordem crescente:
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort()

# Ordenar a lista em ordem decrescente:
numeros.sort(reverse=True)

# Inverter a Ordem:
frutas.reverse()

# Obter o Comprimento da Lista:
tamanho = len(frutas)


# Verificar se um Elemento Existe na Lista:
if 'banana' in frutas:
    print("Banana está na lista!")

# Criar Listas com Compreensão:
# Criar uma lista de quadrados dos números de 0 a 9:
quadrados = [x**2 for x in range(10)]

# Filtrar Elementos com Compreensão:
# Criar uma lista de números pares:
pares = [x for x in range(10) if x % 2 == 0]

# União de Listas:
# Unir duas listas:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
uniao = lista1 + lista2
# Ou usando o método extend():
lista1.extend(lista2)

# Filtrar Elementos com Função Lambda:
# Criar uma lista de números pares usando uma função lambda:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Mapear Elementos com Função Lambda:
# Criar uma lista de quadrados usando uma função lambda:
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))

# Listas de Listas (Matriz):
# Criar uma matriz e calcular a soma de cada coluna:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
somas_colunas = [sum(coluna) for coluna in zip(*matriz)]

# List Comprehension com Condição:
# Criar uma lista contendo apenas os números pares de 0 a 9:
pares = [x for x in range(10) if x % 2 == 0]


# Listas Aninhadas com Compreensão:
# Criar uma matriz usando list comprehension:
matriz = [[i*j for j in range(3)] for i in range(4)]

# Remover Duplicatas de uma Lista:
duplicatas = [1, 2, 2, 3, 4, 4, 5]
sem_duplicatas = list(set(duplicatas))

# Contar a Ocorrência de Elementos:
numeros = [1, 2, 2, 3, 4, 2, 5, 2]
contagem = {numero: numeros.count(numero) for numero in set(numeros)}


# Listas como Argumentos de Funções:
def adicionar_elemento(lista, elemento):
    lista.append(elemento)


minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista, 4)


# Listas de Compreensão Aninhadas:
# Criar uma lista de todas as combinações possíveis de pares de números:
numeros = [1, 2, 3]
combinacoes = [(x, y) for x in numeros for y in numeros if x != y]

# Enumeração de Elementos:
# Obter índices e valores durante a iteração:
frutas = ['maçã', 'banana', 'laranja']
for indice, valor in enumerate(frutas):
    print(f"Índice: {indice}, Valor: {valor}")

# Verificar se Todos os Elementos Satisfazem uma Condição:
# Verificar se todos os números em uma lista são positivos:
numeros = [1, 2, 3, -4, 5]
todos_positivos = all(num > 0 for num in numeros)

# Verificar se Pelo Menos um Elemento Satisfaz uma Condição:
# Verificar se há pelo menos um número positivo na lista:
numeros = [1, 2, 3, -4, 5]
pelo_menos_um_positivo = any(num > 0 for num in numeros)

# Copiar uma Lista:
# Criar uma cópia superficial (shallow copy) ou profunda (deep copy) de uma lista:
original = [1, 2, 3]
copia_superficial = original.copy()
copia_profunda = original[:]

# Fatiamento (Slicing):
# Selecionar uma parte específica de uma lista:
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista = numeros[2:7]  # Seleciona elementos do índice 2 ao 6

# Combinar Duas Listas em um Dicionário:
chaves = ['a', 'b', 'c']
valores = [1, 2, 3]
dicionario = dict(zip(chaves, valores))

# Remover Elementos Duplicados Mantendo a Ordem:
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sem_duplicatas = list(dict.fromkeys(numeros))

# Utilizar collections.Counter para Contagem de Elementos:
# from collections import Counter
numeros = [1, 2, 2, 3, 4, 2, 5, 2]
contagem = Counter(numeros)

# Dividir uma Lista em Partes (Chunks):
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tamanho_do_chunk = 3
chunks = [numeros[i:i + tamanho_do_chunk] for i in range(0, len(numeros), tamanho_do_chunk)]

# Converter Lista de Strings para Inteiros:
# Se você tiver uma lista de strings representando números e desejar convertê-las em inteiros:
numeros_como_strings = ['1', '2', '3']
numeros_como_inteiros = list(map(int, numeros_como_strings))

# Obter Elementos Únicos e Repetidos:
# Encontrar elementos únicos e repetidos em uma lista:
numeros = [1, 2, 2, 3, 4, 2, 5, 2]
unicos = list(set(numeros))
repetidos = [item for item, count in Counter(numeros).items() if count > 1]

# Ordenação Personalizada:
# Ordenar uma lista de strings com base no comprimento das strings:
palavras = ['maçã', 'banana', 'laranja', 'uva']
ordenado_por_comprimento = sorted(palavras, key=len)

# Remover Elementos pela Condição:
# Remover todos os elementos menores que 3 de uma lista:
numeros = [1, 2, 3, 4, 5]
numeros = [num for num in numeros if num >= 3]

# Dividir uma String em uma Lista de Caracteres:
texto = "Python"
caracteres = list(texto)

# Juntar Listas:
# Juntar várias listas em uma única lista:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
lista_completa = lista1 + lista2 + lista3

# Compreensão de Lista para Filtrar e Transformar:
# Criar uma lista contendo os quadrados dos números pares de uma lista original:
numeros = [1, 2, 3, 4, 5]
quadrados_pares = [x**2 for x in numeros if x % 2 == 0]

# Manipulação de Listas com Numpy:
# Se você estiver trabalhando com operações matemáticas em listas, o Numpy é uma biblioteca poderosa:
# import numpy as np
numeros = [1, 2, 3, 4, 5]
quadrados = np.square(numeros)

# Remover Elementos de uma Lista enquanto Itera:
# Evitar a modificação de uma lista durante a iteração usando uma cópia:
frutas = ['maçã', 'banana', 'laranja', 'uva']
for fruta in frutas[:]:  # Cópia da lista
    if len(fruta) < 5:
        frutas.remove(fruta)

# Interseção e Diferença entre Listas:
# Encontrar elementos comuns e diferentes entre duas listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
intersecao = list(set(lista1) & set(lista2))
diferenca = list(set(lista1) - set(lista2))

# Filtrar e Mapear com Expressões Lambda:
# Filtrar números pares e calcular o quadrado dos ímpares usando expressões lambda:
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares_quadrados = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numeros)))

# Dividir Lista em Partes com Tamanho Fixo:
# Dividir uma lista em partes de tamanho fixo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tamanho_do_chunk = 3
chunks = [numeros[i:i + tamanho_do_chunk] for i in range(0, len(numeros), tamanho_do_chunk)]

# Converter Lista em String:
# Converter uma lista de palavras em uma única string:
palavras = ['Python', 'é', 'poderoso']
texto = ' '.join(palavras)

# Compreensão de Lista para Criar Dicionário:
# Criar um dicionário usando compreensão de lista:
chaves = ['a', 'b', 'c']
valores = [1, 2, 3]
dicionario = {chave: valor for chave, valor in zip(chaves, valores)}

# Usar enumerate e zip para Iterar Duas Listas Simultaneamente:
# Iterar sobre duas listas ao mesmo tempo usando enumerate e zip:
frutas = ['maçã', 'banana', 'laranja']
precos = [1.0, 0.5, 0.8]
for indice, (fruta, preco) in enumerate(zip(frutas, precos)):
    print(f"{indice + 1}. {fruta}: R${preco}")

# Ordenação Personalizada com Função de Chave:
# Ordenar uma lista de strings pelo número de vogais:
palavras = ['Python', 'é', 'poderoso']
ordenado_por_vogais = sorted(palavras, key=lambda x: sum(1 for char in x if char.lower() in 'aeiou'))

# Listas com Valores Padrão:
# Criar uma lista com valores padrão usando o operador de repetição:
valores_padrao = [0] * 10

# Usar itertools.product para Obter o Produto Cartesiano de Listas:
# Obter o produto cartesiano de duas listas:
# import itertools
lista1 = ['A', 'B']
lista2 = [1, 2]
produto_cartesiano = list(itertools.product(lista1, lista2))

# Filtrar Elementos Únicos em Ordem:
# Filtrar elementos únicos mantendo a ordem original:
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unicos = sorted(set(numeros), key=numeros.index)

# Manipulação de Listas com collections.deque:
# Usar deque para operações eficientes de inserção e remoção em ambos os extremos:
# from collections import deque
fila = deque([1, 2, 3])
fila.append(4)  # Adiciona no final
fila.appendleft(0)  # Adiciona no início
elemento_removido = fila.popleft()  # Remove do início

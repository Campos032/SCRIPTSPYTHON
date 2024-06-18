# A programação funcional é um paradigma de programação que trata a computação como uma avaliação de funções
# matemáticas e evita a mudança de estados e a mutação de dados. Ela enfatiza o uso de funções puras, que não têm
# efeitos colaterais e retornam sempre o mesmo resultado para os mesmos argumentos, tornando o código mais
# previsível, testável e fácil de raciocinar.

# Principais conceitos da programação funcional incluem:

# Imutabilidade: Dados são tratados como imutáveis. Em vez de alterar os dados existentes, funções criam novos dados.

# Funções de primeira classe: Funções são tratadas como valores de primeira classe, o que significa que podem ser
# atribuídas a variáveis, passadas como argumentos para outras funções e retornadas como valores de outras funções.

# Recursão: Em vez de laços iterativos, a recursão é comumente usada para repetição.

# Funções de ordem superior: Funções que recebem outras funções como argumentos ou retornam funções como resultados.

# Transparência referencial: A transparência referencial garante que uma função sempre retorne o mesmo resultado para
# os mesmos argumentos, sem efeitos colaterais.o

# https://www.youtube.com/watch?v=BWFpUHPqh1g&t=2s
# https://www.youtube.com/watch?v=BxbHGPivjdc
# https://www.alura.com.br/artigos/programacao-funcional-o-que-e
# https://pt.wikipedia.org/wiki/Programação_funcional

# Função de ordem superior que recebe uma função e uma lista como argumentos
def aplica_funcao_a_lista(funcao, lista):
    return [funcao(elemento) for elemento in lista]


# Função que recebe um número e retorna o seu quadrado
def quadrado(x):
    return x ** 2


# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplica a função quadrado a cada elemento da lista usando a função de ordem superior
quadrados = aplica_funcao_a_lista(quadrado, numeros)

# Imprime os quadrados
print(quadrados)  # Output: [1, 4, 9, 16, 25]

# Neste exemplo, a função aplica_funcao_a_lista é uma função de ordem superior que recebe uma função e uma lista como
# argumentos. Ela aplica a função recebida a cada elemento da lista e retorna uma nova lista com os resultados. A
# função quadrado é passada como argumento para aplica_funcao_a_lista, e ela é aplicada a cada elemento da lista
# numeros, resultando em uma lista de quadrados.

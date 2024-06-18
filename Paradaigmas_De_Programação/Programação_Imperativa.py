# A programação imperativa é um paradigma de programação que se concentra na manipulação direta do estado de um
# programa. No estilo imperativo, os programas são compostos por uma sequência de instruções que especificam como o
# computador deve executar uma determinada tarefa. Essas instruções modificam o estado do programa, que consiste em
# variáveis, estruturas de dados e outros elementos.

# Em programação imperativa, os programas são escritos em termos de comandos que alteram o estado do programa. Os
# comandos podem incluir atribuições de variáveis, estruturas de controle (como loops e condicionais), chamadas de
# procedimentos e manipulação direta da memória.

# Um dos conceitos fundamentais da programação imperativa é o conceito de "estado". O estado de um programa refere-se
# ao conjunto de valores armazenados nas variáveis e estruturas de dados em um determinado momento. As instruções do
# programa modificam esse estado, levando o programa de um estado para outro.

# https://www.youtube.com/watch?v=gRYNq5E8g5E
# https://www.youtube.com/watch?v=CIxPWb7S530
# pt.wikipedia.org/wiki/Programação_imperativa


# Exemplo de programa imperativo em Python
# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# Função principal
def main():
    numero = int(input("Digite um número para calcular o fatorial: "))
    resultado_fatorial = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado_fatorial)


# Chamada da função principal
main()

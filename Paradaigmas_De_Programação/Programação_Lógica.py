# Programação Lógica é um paradigma de programação que se baseia na lógica de predicados e na inferência. O principal
# modelo de programação lógica é a linguagem Prolog (Programming in Logic), onde os programas são especificados em
# termos de relações lógicas entre objetos.

# A Programação Lógica se concentra em declarar relações entre entidades e permitir ao interpretador inferir
# resultados dessas relações. A base da Programação Lógica é a resolução de consultas sobre essas relações por
# unificação e busca em profundidade.

# A unificação é o processo central na Programação Lógica, onde duas expressões lógicas são combinadas de modo a
# tornarem-se idênticas. Isso é fundamental para a resolução de consultas.

# Um dos usos mais comuns da Programação Lógica é em sistemas de inteligência artificial, sistemas especialistas,
# processamento de linguagem natural e análise de dados.

# Implementação de um pequeno programa em lógica de predicados usando Python

# Neste exemplo simples, temos relações definidas entre pais, mães e filhos. Utilizando essas relações, definimos
# predicados para determinar se duas pessoas são irmãs ou irmãos. Em seguida, fazemos algumas consultas para verificar
# essas relações.

# https://www.youtube.com/watch?v=PjONeLBQCqk&pp=ygUfcGFyYWRpZ21hIHByb2dyYW1hw6fDo28gbMOzZ2ljYQ%3D%3D
# https://www.youtube.com/watch?v=iVniYDxKl9U&pp=ygUfcGFyYWRpZ21hIHByb2dyYW1hw6fDo28gbMOzZ2ljYQ%3D%3D

# Relações
def pai(X, Y):
    return (X == 'joao' and Y == 'maria') or \
           (X == 'joao' and Y == 'pedro') or \
           (X == 'pedro' and Y == 'lucas')


def mae(X, Y):
    return (X == 'ana' and Y == 'pedro') or \
           (X == 'ana' and Y == 'maria')


def irmao(X, Y):
    for Z in ['joao', 'pedro']:
        if pai(Z, X) and pai(Z, Y) and X != Y:
            return True
    return False


def irma(X, Y):
    for Z in ['ana']:
        if mae(Z, X) and mae(Z, Y) and X != Y:
            return True
    return False


# Consultas
print(irmao('maria', 'pedro'))  # True
print(irma('maria', 'pedro'))   # False
print(irma('ana', 'maria'))     # True

# Neste exemplo simples, temos relações definidas entre pais, mães e filhos. Utilizando essas relações, definimos
# predicados para determinar se duas pessoas são irmãs ou irmãos. Em seguida, fazemos algumas consultas para verificar
# essas relações.

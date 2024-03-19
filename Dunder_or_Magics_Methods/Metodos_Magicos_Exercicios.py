# Escreva uma classe ContadorPalavras que permita contar o número de palavras em uma frase.
import random


class ContaPalavras:
    def __init__(self, frase: str):
        self.frase = frase

    def __len__(self):
        return len(self.frase.split(' '))


frase1 = ContaPalavras('Claramente Dois')
# print(len(frase1))  # Retorna 2


# Implemente uma classe Vetor que represente um vetor matemático e permita a soma de dois vetores.
class Vetor:
    def __init__(self, lista: list):
        self.vetor = lista

    def __add__(self, other: list):
        # O que faz função zip()
        # self.elementos = [1, 2, 3]
        # other.elementos = ['a', 'b', 'c']
        # resultado = zip(self.elementos, other.elementos)
        # Neste caso, resultado conterá[(1, 'a'), (2, 'b'), (3, 'c')].
        return [a + b for a, b in zip(self.vetor, other)]
        # return self.vetor + other como eu tinha feito


v1 = Vetor([1, 3, 5])
# print(v1 + [2, 4, 6])  # Retorna [3, 7, 11]


# Crie uma classe Pessoa que represente uma pessoa com nome e idade e implemente os métodos mágicos para comparação
# entre pessoas com base na idade.
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __eq__(self, other):
        return self.idade == other.idade


p1 = Pessoa('João', 19)
p2 = Pessoa('José', 20)
# print(p1 == p2)


# Escreva uma classe Matriz que represente uma matriz e permita a multiplicação escalar.
class Matriz:
    def __init__(self, matriz: list):
        self.matriz = matriz

    def __mul__(self, other):
        nova_matriz = [linha[:] for linha in self.matriz]
        for indice_linha, linha in enumerate(nova_matriz):
            for indice_num, num in enumerate(linha):
                nova_matriz[indice_linha][indice_num] = num * other
        return nova_matriz


m1 = Matriz([[1, 2], [3, 4]])
multiply_escaling = m1 * 2
# print(multiply_escaling)
# print(m1.matriz)


# Implemente uma classe que permita a iteração reversa sobre uma sequência de elementos.
class ReverseIter:
    def __init__(self, *args: int):
        self.args = list(args)

    def __iter__(self):
        return iter(reversed(self.args))


r1 = ReverseIter(1, 2, 3)
# print(r1.args)
# for num in r1:
#     print(num, end=' ')
# print()
# print(r1.args)


# Crie uma classe que represente uma lista que combine elementos de duas listas de entrada de maneira alternada.
class CombinaLista:
    def __init__(self, lista1: list, lista2: list):
        self.lista = lista1 + lista2

    def __str__(self):
        return str(sorted(self.lista))


lista_combinada = CombinaLista([1, 2, 3], [4, 5, 6])
# print(lista_combinada)


# Escreva uma classe que represente um objeto com hashing personalizado. Você pode usar métodos mágicos para definir
# como esse objeto é convertido em um hash.
class HashModify:
    def __init__(self, valor):
        self.valor = valor

    def __hash__(self):
        novo_hash = int(hash(self.valor) + random.randint(0, 30))
        return novo_hash


# Exemplo de uso
objeto1 = HashModify('42')
objeto2 = HashModify(100)
# print(hash(objeto1))  # Imprime o hash do objeto1
# print(hash(objeto2))  # Imprime o hash do objeto2


# Implemente uma classe que atue como um gerenciador de contexto, permitindo a execução de ações antes e depois de um
# bloco de código.
class AbreArquivo:
    def __init__(self, archive):
        self.arquivo = archive

    def __enter__(self):
        try:
            self.arquivo_aberto = open(self.arquivo, 'r')
        except FileNotFoundError:
            print(f'O arquivo "{self.arquivo}" não foi encontrado')
            return None
        else:
            print(f'O arquivo "{self.arquivo}" foi aberto')
            return self.arquivo_aberto

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.arquivo_aberto:
            self.arquivo_aberto.close()
            print(f'O arquivo "{self.arquivo}" foi fechado')


# Os métodos __enter__ e __exit__ são executados automaticamente quando você utiliza um objeto de uma classe que atua
# como gerenciador de contexto num bloco with
# Exemplo de uso:
# with AbreArquivo('teste.txt') as arquivo:
#     if arquivo:
#         conteudo = arquivo.read()
#         print(conteudo)


# Crie uma classe que represente uma sequência de elementos e permita embaralhá-los. Use métodos mágicos para definir o
# comportamento do embaralhamento.
class Embaralhar:
    def __init__(self, *args):
        self.args = list(args)

    def __call__(self):
        self.nova_args = self.args.copy()
        random.shuffle(self.nova_args)
        return self.nova_args

    def __str__(self):
        return f"{self.args}"


embaralho = Embaralhar(1, 4, 7, 9, 1)
# print(embaralho())
# print(embaralho)


# Escreva uma classe que represente um número e permita a execução de operações matemáticas personalizadas, como adição,
# subtração, multiplicação e divisão.
class Calculadora:
    def __init__(self, num: int):
        self.num = num

    def __add__(self, other):
        return self.num + int(other)

    def __sub__(self, other):
        return self.num - int(other)

    def __mul__(self, other):
        return self.num * int(other)

    def __truediv__(self, other):
        return int(self.num / int(other))


calcula = Calculadora(2)
# print(calcula + 1)
# print(calcula - 1)
# print(calcula * 2)
# print(calcula / 2)


# Implemente uma classe que permita a serialização personalizada de objetos em diferentes formatos, como JSON, XML
# ou YAML.
import json
import xml.etree.ElementTree as Et
import yaml


# Esse exercício foi copiado, eu não fazia a mínima ideia de como utilizar os pacotes importados, principalmente o xml
class Serializador:
    def __init__(self, dicionario: dict):
        self.objeto = dicionario

    def serializar_json(self):
        return json.dumps(self.objeto)

    def serializar_xml(self):
        root = Et.Element("objeto")
        self._serializar_para_xml(root, self.objeto)
        return Et.tostring(root, encoding="unicode")

    def _serializar_para_xml(self, elemento_pai, objeto):
        if isinstance(objeto, dict):
            for chave, valor in objeto.items():
                sub_elemento = Et.SubElement(elemento_pai, chave)
                self._serializar_para_xml(sub_elemento, valor)
        elif isinstance(objeto, (list, tuple)):
            for item in objeto:
                sub_elemento = Et.SubElement(elemento_pai, "item")
                self._serializar_para_xml(sub_elemento, item)
        else:
            elemento_pai.text = str(objeto)

    def serializar_yaml(self):
        return yaml.dump(self.objeto)


# Exemplo de uso:
dados = {"nome": "João", "idade": 30, "hobbies": ["leitura", "esportes"]}

serializador = Serializador(dados)

# Serialização para JSON
json_serializado = serializador.serializar_json()
# print("JSON:", json_serializado)

# Serialização para XML
xml_serializado = serializador.serializar_xml()
# print("XML:", xml_serializado)

# Serialização para YAML
yaml_serializado = serializador.serializar_yaml()
# print("YAML:", yaml_serializado)


# Crie uma classe que represente um subconjunto de um conjunto maior e implemente métodos mágicos para comparar e
# manipular esses subconjuntos.
from typing import Union


class CompSubConjunto:
    def __init__(self, subconjunto: Union[list, dict, str]):  # O método Union permite definir mais de uma opção para
        self.subconjunto = set(subconjunto)  # o parâmetro, e set defini como um conjunto, removendo as duplicatas

    def __str__(self):
        return str(self.subconjunto)

    def __eq__(self, other):
        return self.subconjunto == set(other)

    def __ne__(self, other):
        return self.subconjunto != set(other)

    def __lt__(self, other):
        return self.subconjunto < set(other)

    def __gt__(self, other):
        return self.subconjunto > set(other)

    def __le__(self, other):
        return self.subconjunto <= set(other)

    def __ge__(self, other):
        return self.subconjunto >= set(other)


subgrupo = CompSubConjunto([1, 2, 3, 3, 4, 5])
# print(subgrupo < [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9])
# print(subgrupo == [2, 1, 3, 3, 4, 5])
# print(subgrupo != [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9])
# print(subgrupo > [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9])
# print(subgrupo <= [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9])
# print(subgrupo >= [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9])
# print(subgrupo)

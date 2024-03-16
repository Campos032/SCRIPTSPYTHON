# Introdução a classes
class ControleRemoto:
    # características:
    #     - cor
    #     - altura
    #     - profundidade
    #     - largura

    # Toda classe em python deve ter uma função __init__ que define as características da classe
    def __init__(self, cor, altura, profundidade, largura):
        # Self é igual o nome da classe, portanto Cor do ControleRemoto = Preto
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.lista_canais = [1, 2, 3, 4, 5]
        self.canal = 1
        self.volume = 50

    def passar_canal(self, botao):
        if botao == '+':
            if self.canal == 5:
                self.canal = 1
            else:
                self.canal += 1
            print('Aumentar canal')
        elif botao == '-':
            if self.canal == 1:
                self.canal = 5
            else:
                self.canal -= 1
            print('Diminuir canal')

    def alterar_volume(self, botao_volume):
        if self.volume == 100 and botao_volume == '+':
            print('Volume Máximo')
        elif self.volume == 0 and botao_volume == '-':
            print('Volume Mínimo')
        else:
            if botao_volume == '+':
                self.volume += 1
            elif botao_volume == '-':
                self.volume -= 1
    # métodos do controle remoto:
    #     - passar de canal
    #     - alterar no volume
    #     - abrir a netflix
    #     - desligar tv


# O que é POO #
# POO, ou Programação Orientada a Objetos, é um paradigma de programação que se baseia no conceito de "objetos". Em
# vez de escrever um programa como uma série de instruções lineares, na programação orientada a objetos, os programas
# são construídos em torno de objetos que representam entidades reais. Cada objeto é uma instância de uma
# classe, que define suas características (atributos) e comportamentos (métodos).

# Definindo uma classe
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dirigir(self):
        print(f"O {self.marca} {self.modelo} está sendo dirigido.")


# A POO visa principalmente organizar o código de forma mais modular, facilitando a reutilização, manutenção
# e escalabilidade do software. Ela ajuda os desenvolvedores a escreverem programas mais claros, flexíveis e
# eficientes, ao permitir a modelagem de sistemas complexos de forma mais intuitiva, através da criação de abstrações
# que refletem a estrutura do problema a ser resolvido.

# Criando instâncias de objetos (instanciando a classe):
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

carro1.dirigir()
carro2.dirigir()


# Além disso, a POO promove conceitos fundamentais como encapsulamento, herança e polimorfismo, que contribuem para a
# criação de código mais robusto e extensível. Esses conceitos permitem que os desenvolvedores construam sistemas
# modulares, onde as diferentes partes do código são independentes umas das outras, facilitando a manutenção e
# evolução do software ao longo do tempo.

# Encapsulamento é o conceito de restringir o acesso direto aos atributos e métodos de uma classe, e
# controlar o acesso por meio de métodos de interface. Isso ajuda a proteger os dados da classe e fornece um nível de
# abstração.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo


class MinhaClasse:
    def __init__(self):
        self._atributo_protegido = 10  # Indica que a variável deve ser privada, mas não a torna privada no Python
        self.__atributo_privado = 20  # Name Mangling, privar uma variável dentro do interpretador, utilizando __


objeto = MinhaClasse()

# Acesso ao atributo protegido (convenção)
print(objeto._atributo_protegido)  # Saída: 10

# Tentativa de acesso ao atributo privado (name mangling)
# Isso, na verdade, não vai funcionar diretamente.
print(objeto.__atributo_privado)  # Vai resultar em um AttributeError

# Acesso ao atributo privado com name mangling
print(objeto._MinhaClasse__atributo_privado)  # Saída: 20


# Herança é o conceito de criar uma nova classe baseada em uma classe existente, aproveitando seus atributos e
# métodos. A classe nova (derivada) pode adicionar novos comportamentos ou modificar os existentes.
class Animal:
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")


class Gato(Animal):
    def fazer_som(self):
        print("Miau!")


dog = Cachorro()
cat = Gato()


# Polimorfismo é o conceito de que objetos de diferentes classes podem ser tratados de maneira uniforme se tiverem uma
# interface comum.
def fazer_som_animais(animals):
    for animal in animals:
        animal.fazer_som()


animais = [Cachorro(), Gato()]
fazer_som_animais(animais)

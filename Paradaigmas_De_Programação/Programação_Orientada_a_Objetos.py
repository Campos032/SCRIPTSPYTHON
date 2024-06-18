# A Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" para representar dados
# e métodos associados. Em vez de focar em ações e lógica, a POO organiza software em torno de objetos, que podem ser
# manipulados para realizar diversas operações.
#
# Principais Conceitos da POO: Classe: Uma classe é uma blueprint ou um molde para criar objetos. Define atributos (
# dados) e métodos (funções) que os objetos criados a partir da classe terão.
#
# Objeto: Uma instância de uma classe. Representa uma entidade real ou abstrata com estado e comportamento definidos
# pela classe. Por exemplo, um objeto "Carro" pode ter atributos como cor e modelo, e métodos como acelerar e frear.
#
# Atributos: Variáveis que armazenam dados pertencentes a uma classe ou objeto. Por exemplo, um objeto "Pessoa" pode
# ter atributos como nome e idade.
#
# Métodos: Funções definidas numa classe que descrevem os comportamentos dos objetos daquela classe. Por
# exemplo, um objeto "ContaBancaria" pode ter métodos como depositar e sacar.

# Encapsulamento: O princípio de esconder os detalhes internos de um objeto e expor apenas o que é necessário.
# Atributos e métodos são encapsulados dentro da classe, e o acesso a eles é controlado por meio de modificadores de
# acesso como público, privado e protegido.

# Herança: Um mecanismo onde uma classe (subclasse) pode herdar atributos e métodos de outra classe (superclasse).
# Promove a reutilização de código e a criação de uma hierarquia de classes.

# Polimorfismo: A capacidade de objetos de diferentes classes serem tratados de forma unificada. Permite que o mesmo
# método ou operador funcione de diferentes maneiras para diferentes classes. Por exemplo, um método "desenhar" pode
# se comportar de forma diferente em classes "Circulo" e "Quadrado".

# Abstração: O processo de simplificar a complexidade ocultando detalhes desnecessários e expondo apenas as
# características essenciais. Facilita a modelagem de sistemas complexos focando apenas nos aspectos mais relevantes.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")


# Herança: ContaCorrente e ContaPoupanca
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente, mesmo considerando o limite.")


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0, juros=0.01):
        super().__init__(titular, saldo)
        self.juros = juros

    def render_juros(self):
        self.saldo += self.saldo * self.juros
        print(f"Juros de {self.juros * 100}% aplicados. Novo saldo: R${self.saldo}")


# Polimorfismo
def realizar_operacao(conta, operacao, valor=0):
    if operacao == "depositar":
        conta.depositar(valor)
    elif operacao == "sacar":
        conta.sacar(valor)
    elif operacao == "exibir_saldo":
        conta.exibir_saldo()
    elif operacao == "render_juros" and isinstance(conta, ContaPoupanca):
        conta.render_juros()
    else:
        print("Operação inválida ou não suportada para esta conta.")


# Criando objetos e testando o sistema
conta1 = ContaCorrente("João", 1000, 500)
conta2 = ContaPoupanca("Maria", 2000)

realizar_operacao(conta1, "depositar", 200)  # Depósito de R$200 realizado com sucesso.
realizar_operacao(conta1, "sacar", 1500)  # Saque de R$1500 realizado com sucesso.
realizar_operacao(conta1, "exibir_saldo")  # Saldo atual: R$-300
realizar_operacao(conta2, "render_juros")  # Juros de 1.0% aplicados. Novo saldo: R$2020.0
realizar_operacao(conta2, "exibir_saldo")  # Saldo atual: R$2020.0

# Classe (Classe Base): ContaBancaria é a classe base que define os atributos e métodos comuns a todas as contas
# bancárias. Objetos: conta1 e conta2 são instâncias das classes ContaCorrente e ContaPoupanca, respectivamente.
# Herança: ContaCorrente e ContaPoupanca herdam de ContaBancaria e adicionam ou modificam comportamentos específicos.
# Encapsulamento: Atributos como saldo e métodos como depositar e sacar estão encapsulados dentro das classes,
# permitindo o controle de acesso e manipulação. Polimorfismo: A função realizar_operacao aceita objetos de
# diferentes tipos (ContaCorrente e ContaPoupanca) e realiza operações com base no tipo de conta, mostrando a
# flexibilidade do polimorfismo. Abstração: A complexidade interna de cada operação (depósito, saque, rendimentos) é
# ocultada, expondo apenas as interfaces necessárias para o usuário interagir com o sistema de contas bancárias.

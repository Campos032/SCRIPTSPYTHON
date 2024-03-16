# Criar uma classe Retângulo:
# Crie uma classe chamada Retângulo que tenha atributos largura e altura. Implemente métodos para calcular a área e o
# perímetro do retângulo.
import datetime

from A16_Tratamento_de_Erros_e_Exceções.MinhaSolução.Desafio115.modulo import leia_int


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return f"A área do retângulo é {self.largura * self.altura}m²"

    def perimetro(self):
        return f"O perímetro do retângulo é {self.largura + self.altura}m"


# largura_retangulo = leia_int('Digite a largura do retângulo(m): ')
# altura_retangulo = leia_int('Digite a altura do retângulo(m): ')
# retangulo1 = Retangulo(largura_retangulo, altura_retangulo)
# print(retangulo1.area())
# print(retangulo1.perimetro())


# Criar uma classe ContaBancaria: Crie uma classe chamada ContaBancaria com atributos saldo e titular. Implemente
# métodos para depositar, sacar e verificar o saldo da conta.
class ContaBancaria:
    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        return f"Deposito Efetuado com Sucesso. Saldo Atual R${self.saldo}\n"

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque
            return f"Saque Efetuado Com Sucesso. Saldo atual R${self.saldo}\n"
        else:
            return f"Saque Não Efetuado. Valor Do Saque É Maior Que O Saldo Disponível\n"

    def ver_saldo(self):
        return f"Saldo atual R${self.saldo}"


# titular_conta = str(input('Digite seu nome:'))
# deposito_inicial = leia_int('Digite o valor do seu depósito inicial(R$): ')
# pessoa1 = ContaBancaria(titular_conta, deposito_inicial)
# print(f"\nTitular Da Conta: {pessoa1.titular}\nSaldo Disponível: R${pessoa1.saldo}\n")
# segundo_deposito = leia_int('Digite o valor do depósito(R$): ')
# print(pessoa1.depositar(segundo_deposito))
# valor_saque = leia_int('Digite o valor do saque(R$): ')
# print(pessoa1.sacar(valor_saque))
# ver_saldo_ou_nao = leia_int('1 - Ver Saldo'
#                             '\n2 - Não Ver Saldo'
#                             '\nDigite sua opção: ')
# if ver_saldo_ou_nao == 1:
#     print(pessoa1.ver_saldo())
# else:
#     print('\nSaindo...')


# Criar uma classe Carro: Crie uma classe chamada Carro com atributos marca, modelo e ano. Implemente métodos para
# ligar o carro, desligar o carro e acelerar.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.carro = ['Desligado', 'Ligado']
        self.estado_carro = ['Acelerar', 'Parar']
        self.ignicao = 'Desligado'
        self.movimento = 'Parar'

    def ligar(self):
        if self.ignicao == 'Desligado':
            self.ignicao = 'Ligado'
            return f"O Carro Foi Ligado"
        else:
            return f"O Carro Já Está Ligado"

    def desligar(self):
        if self.ignicao == 'Ligado':
            self.ignicao = 'Desligado'
            return f"O Carro Foi Desligado"
        else:
            return f"O Carro Já Está Desligado"

    def acelerar(self):
        if self.movimento == 'Parar':
            self.movimento = 'Acelerar'
            return f"O Carro Está em Aceleração"
        else:
            return f"O Carro Já Está Acelerado"

    def parar(self):
        if self.movimento == 'Acelerar':
            self.movimento = 'Parar'
            return f"O Carro Está Desacelerando"
        else:
            return f"O Carro Já Está Parado"


# carro1 = Carro('Volkswagen', 'Gol GTS', 1994)
# print(f"Marca: {carro1.marca} / Modelo: {carro1.modelo} / Ano: {carro1.ano}")
# print(carro1.desligar())
# print(carro1.ligar())
# print(carro1.desligar())
# print(carro1.parar())
# print(carro1.acelerar())
# print(carro1.parar())

# Criar uma classe Círculo: Crie uma classe chamada Circulo com um atributo raio. Implemente métodos para calcular a
# área e o perímetro do círculo.
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):  # A=πr²
        return f"A Área Do Circulo É {3.14 * self.raio ** 2: .2f}m²"

    def perimetro(self):  # P=2πr
        return f"O Perímetro Do Circulo É {2 * 3.14 * self.raio: .2f}m"


# circulo1 = Circulo(5)
# print(circulo1.area())
# print(circulo1.perimetro())

# Criar uma classe Pessoa: Crie uma classe chamada Pessoa com atributos nome, idade e cidade. Implemente métodos para
# atualizar a idade da pessoa e mostrar informações sobre ela.
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def update_year_old(self, new_year_old):
        self.idade = new_year_old
        return (f"Nome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nCidade: {self.cidade}")

    def update_city(self, new_city: str):
        self.cidade = new_city
        return (f"Nome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nCidade: {self.cidade}")


# pessoa1 = Pessoa('Márcio Campos Júnior', 18, 'Senhora Dos Remédios')
# print(f"{pessoa1.nome}\n{pessoa1.idade} Anos\n{pessoa1.cidade}")
# print(pessoa1.update_year_old(19))
# print(pessoa1.update_city('Rio de Janeiro'))

# Criar uma classe ContaCorrente: Crie uma classe chamada ContaCorrente que herde da classe ContaBancaria (do
# exercício 2). Adicione um atributo limite e modifique o método de saque para considerar o limite da conta-corrente.
class ContaCorrente(ContaBancaria):
    def __init__(self, titular: str, saldo: int, limite_saque: int):
        super().__init__(titular, saldo)
        self.limite_saque = limite_saque

    def sacar(self, saque: int):
        if self.saldo > saque <= self.limite_saque:
            self.saldo -= saque
            return f"Saque Efetuado Com Sucesso. Saldo atual R${self.saldo}\n"
        else:
            return f"Saque Não Efetuado. Valor Do Saque É Maior Que Seu Saldo Ou Limite De Saque\n"


# pessoa_corrente = ContaCorrente('Márcio', 500, 250)
# print(f"{pessoa_corrente.titular}\nSaldo: R${pessoa_corrente.saldo}\nLimite Saque: R${pessoa_corrente.limite_saque}")
# print(pessoa_corrente.sacar(20))

# Criar uma classe Livro: Crie uma classe chamada Livro com atributos titulo, autor e ano de publicação. Implemente
# métodos para verificar se o livro é antigo (publicado há mais de 50 anos) e para mostrar informações sobre o livro.
class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def ver_livro(self):
        return (f"Título: {self.titulo}"
                f"\nAutor: {self.autor}"
                f"\nAno Publicação: {self.ano_publicacao}")

    def antigo_ou_novo(self):
        idade_livro = datetime.date.today().year - self.ano_publicacao
        if idade_livro >= 50:
            return f"O livro é antigo pois possui mais de 50 anos ({idade_livro} Anos)"
        else:
            return f"O livro é novo pois possui menos de 50 anos ({idade_livro} Anos)"


# livro1 = Livro('Crônicas De Nárnia', 'Sthen BodyKit', 1900)
# info_livro = livro1.ver_livro()
# print(info_livro)
# idade_livro = livro1.antigo_ou_novo()
# print(idade_livro)

# Criar uma classe Triângulo: Crie uma classe chamada Triangulo com atributos lado1, lado2 e lado3. Implemente
# métodos para verificar se os lados formam um triângulo válido e para calcular a área e o perímetro do triângulo.
class Triangulo:
    def __init__(self, lado1: int, lado2: int, lado3: int):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def validar_triangulo(self):
        if self.lado1 > self.lado2:
            print('As Medidas Inseridas Formam Um Triângulo')
            return True
        else:
            print(f"As Medidas Inseridas Não Formam Um Triângulo")
            return False

    def perimetro(self):
        if self.validar_triangulo():
            pr = self.lado1 + self.lado2 + self.lado3
            return f"O Perímetro do Triângulo é {pr}m"
        else:
            return f"As Medidas Inseridas Não Formam Um Triângulo"


# Criar uma classe Aluno: Crie uma classe chamada Aluno com atributos nome, idade, curso e nota. Implemente métodos
# para atualizar a nota do aluno e para verificar se ele foi aprovado (nota maior ou igual a 6).
class Aluno:
    def __init__(self, nome: str, idade: int, curso: str, nota: float):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def ver_aluno(self):
        return (f"Nome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nCurso: {self.curso}"
                f"\nNota: {self.nota}")

    def atualizar_nota(self, nova_nota: float):
        nota_antiga = self.nota
        self.nota = nova_nota
        return f"Nota atualizada, {nota_antiga: .2f} -> {self.nota: .2f}"


# aluno1 = Aluno('Campos', 18, 'Eletroeletrônica', 6.75)
# print(aluno1.ver_aluno())
# print(aluno1.atualizar_nota(8))

# Criar uma classe Animal: Crie uma classe chamada Animal com atributos especie e nome. Implemente métodos para
# emitir um som característico do animal e para mostrar informações sobre ele.
class Animal:
    lista_especies = ['Cachorro', 'Gato']

    def __init__(self, especie: str, nome: str):
        self.especie = especie
        self.nome = nome

    dicionario_animais = [{'Cachorro': ['Som: AuAu!', 'Características: Amigável, Rápido, Forte, Boa visão']},
                          {'Gato': ['Som: Miau!', 'Características: Amigável, 7 Vidas, Fofinhos ']}]

    def som(self):
        for animal in self.dicionario_animais:
            for chave, valor in animal.items():
                if self.especie == chave:
                    for x in valor:
                        print(f'{x}\n')
                    print(f'Essas São Minhas Informações Sobre Essa Espécie.')
                    return True
        else:
            print(f'Não Encontrei Essa Espécie.')
            return False


animal1 = Animal('Cachorro', 'José')
animal1.som()

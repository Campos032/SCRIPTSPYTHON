# Gerenciamento de Contas Bancárias:
# Um sistema de gerenciamento de contas bancárias pode ser um bom exemplo. Você pode ter uma classe ContaBancaria que
# possui métodos para depositar, sacar e verificar o saldo. As subclasses podem incluir ContaCorrente e
# ContaPoupança, cada uma com suas próprias regras específicas.
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def verificar_saldo(self):
        print("Saldo:", self.saldo)


# Exemplo de uso:
conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.verificar_saldo()


# Jogo com Personagens:
# Você pode criar um jogo com diferentes personagens com habilidades e características únicas. Cada personagem
# pode ser uma classe separada que herda de uma classe base Personagem. Por exemplo, você pode ter classes para
# Guerreiro, Mago e Arqueiro.
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def verificar_saldo(self):
        print("Saldo:", self.saldo)


# Exemplo de uso:
conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.verificar_saldo()


# Sistema de Cadastro de Funcionários:
# Um sistema de cadastro de funcionários pode ser implementado usando classes para representar diferentes tipos de
# funcionários, como Funcionário, Gerente, Vendedor, etc. Cada classe pode ter métodos para calcular salário,
# benefícios, etc.
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self):
        return self.salario


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario * 1.2  # Gerentes têm um bônus de 20%


# Exemplo de uso:
funcionario = Funcionario("João", 3000)
gerente = Gerente("Maria", 4000)
print(funcionario.calcular_salario())
print(gerente.calcular_salario())


# Aplicativo de Agenda:
# Um aplicativo de agenda pode ser dividido em classes como Evento, Lembrete, Tarefa, etc. Cada classe pode ter
# métodos para adicionar, excluir e visualizar eventos, lembretes ou tarefas.
class Evento:
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

    def visualizar(self):
        print("Título:", self.titulo)
        print("Data:", self.data)


class Lembrete(Evento):
    def __init__(self, titulo, data, mensagem):
        super().__init__(titulo, data)
        self.mensagem = mensagem

    def visualizar(self):
        super().visualizar()
        print("Mensagem:", self.mensagem)


# Exemplo de uso:
evento = Evento("Reunião", "2024-03-15")
evento.visualizar()
lembrete = Lembrete("Compras", "2024-03-20", "Comprar leite e pão")
lembrete.visualizar()


# Sistema de Compras Online:
# Um sistema de compras online pode ser modelado com classes para representar produtos, carrinhos de compras e
# usuários. Você pode ter classes como Produto, Carrinho, Usuário e métodos para adicionar/remover itens do carrinho,
# realizar pagamentos, etc.
class Evento:
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

    def visualizar(self):
        print("Título:", self.titulo)
        print("Data:", self.data)


class Lembrete(Evento):
    def __init__(self, titulo, data, mensagem):
        super().__init__(titulo, data)
        self.mensagem = mensagem

    def visualizar(self):
        super().visualizar()
        print("Mensagem:", self.mensagem)


# Exemplo de uso:
evento = Evento("Reunião", "2024-03-15")
evento.visualizar()
lembrete = Lembrete("Compras", "2024-03-20", "Comprar leite e pão")
lembrete.visualizar()


# Simulação de Tráfego de Rede:
# Uma simulação de tráfego de rede pode ser implementada com classes para representar dispositivos de rede,
# como roteadores, switches e computadores. Cada classe pode ter métodos para enviar e receber dados, verificar o
# status da conexão, etc.
class DispositivoRede:
    def __init__(self, endereco_ip):
        self.endereco_ip = endereco_ip

    def enviar_dados(self, dados):
        pass

    def receber_dados(self, dados):
        pass


class Roteador(DispositivoRede):
    def encaminhar_dados(self, destino, dados):
        print("Encaminhando dados para", destino.endereco_ip)
        destino.receber_dados(dados)


class Computador(DispositivoRede):
    def enviar_dados(self, dados):
        print("Enviando dados para o roteador")
        roteador = Roteador("192.168.1.1")
        roteador.encaminhar_dados(self, dados)


# Exemplo de uso:
computador = Computador("192.168.1.2")
roteador = Roteador("192.168.1.1")
dados = "Dados importantes"
computador.enviar_dados(dados)

# Aplicativo de Busca de Livros #
# Imagine que você está criando um aplicativo que permite aos usuários pesquisar livros por título. Você pode usar a API
# do Google Books para obter informações sobre os livros.
import requests


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


def pesquisar_livros_por_titulo(titulo):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle: {titulo}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        livros = []
        for item in dados["items"]:
            info = item["volumeInfo"]
            titulo = info.get("title", "Desconhecido")
            autores = info.get("authors", ["Desconhecido"])
            autor = ", ".join(autores)
            livros.append(Livro(titulo, autor))
        return livros
    else:
        print("Falha ao buscar livros.")
        return []


# Exemplo de uso
livros = pesquisar_livros_por_titulo("Hacking")
for livro in livros:
    print(f"Título: {livro.titulo}, Autor(es): {livro.autor}")

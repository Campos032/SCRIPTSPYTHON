# Exercício 1: Sistema de Biblioteca
# Crie um sistema de gerenciamento de biblioteca que permita adicionar livros, gerenciar empréstimos e devoluções.
import uuid


# Classe Base: Livro

# Atributos: título, autor, ISBN, disponibilidade
# Métodos: emprestar, devolver

# Classe: Usuario

# Atributos: nome, ID de usuário, livros emprestados (lista de livros)
# Métodos: pegar livro emprestado, devolver livro

# Classe: Biblioteca

# Atributos: nome da biblioteca, lista de livros, lista de usuários
# Métodos: adicionar livro, remover livro, registrar usuário, remover usuário, listar livros disponíveis

class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.username = None
        self.user_id = None
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidade = True

    def emprestar(self, nome: str, id_de_usuario: str):
        if self.disponibilidade:
            self.username = nome
            self.user_id = id_de_usuario
            self.disponibilidade = False
            return print("Livro emprestado!")
        return print("Livro não disponível!")

    def devolver(self):
        if self.disponibilidade:
            return "O Livro já está disponível!"
        self.username = None
        self.user_id = None
        self.disponibilidade = True
        return print("Livro devolvido com sucesso!")

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nome: str, id_de_usuario: str = None):
        self.nome = nome
        self.id_de_usuario = id_de_usuario or str(uuid.uuid4())
        self.livros_emprestados = []

    def pegar_livro(self, isbnuser, library):
        for livro in library.lista_livros:
            if livro.isbn == isbnuser:
                resultado = livro.emprestar(self.nome, self.id_de_usuario)
                if resultado == "Livro emprestado!":
                    self.livros_emprestados.append(livro)
                    return print("Livro Emprestado")
                return resultado
        return print("Livro não encontrado")

    def devolver_livro(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}, Id_Usuário: {self.id_de_usuario}, Livros A Devolver: {self.livros_emprestados}"


class Biblioteca:
    def __init__(self, nome_biblioteca: str):
        self.nome_biblioteca = nome_biblioteca
        self.lista_livros = []
        self.lista_usuarios = []

    def adicionar_livro(self, titulo: str, autor: str, isbn: str):
        livro = Livro(titulo, autor, isbn)
        for book in self.lista_livros:
            if book.isbn == isbn:
                return print("Livro já cadastrado!")
        self.lista_livros.append(livro)
        return print("Livro adicionado a biblioteca!")

    def remover_livro(self, isbn: str):
        livro_a_remover = None
        for livro in self.lista_livros:
            if livro.isbn == isbn:
                livro_a_remover = livro
        self.lista_livros.remove(livro_a_remover)
        return print("livro removido!")

    def registrar_usuario(self, nome: str, id_de_usuario: str = None):
        usuario = Usuario(nome, id_de_usuario)
        for user in self.lista_usuarios:
            if user.nome == usuario.nome:
                return print("Usuário já cadastrado!")
        self.lista_usuarios.append(usuario)
        return print("Usuário registrado!")

    def remover_usuario(self, nome: str):
        usuario_a_remover = None
        for user in self.lista_usuarios:
            if user.nome == nome:
                usuario_a_remover = user
                break
        if usuario_a_remover:
            self.lista_usuarios.remove(usuario_a_remover)
            return print("Usuário removido!")
        return print("Usuário não encontrado!")

    def listar_livros(self):
        for livro in self.lista_livros:
            print(livro)

    def livros(self):
        return self.lista_livros


# # Exemplo de uso
# biblioteca = Biblioteca("Biblioteca Teste!")
#
# # Registrar um usuário
# print(biblioteca.registrar_usuario("Carlos"))
# usuario_carlos = biblioteca.lista_usuarios[0]
#
# # Adicionar livros
# print(biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-3-16-148410-0"))
# print(biblioteca.adicionar_livro("1984", "George Orwell", "978-0-452-28423-4"))
#
# # Listar livros
# biblioteca.listar_livros()
#
# # Emprestar livro
# print(usuario_carlos.pegar_livro("978-3-16-148410-0", biblioteca))
#
# # Listar livros novamente para ver as mudanças
# biblioteca.listar_livros()
#
# # Devolver livro
# # print(usuario_carlos.devolver_livro("978-3-16-148410-0", biblioteca))
#
# # Listar livros novamente para ver as mudanças
# biblioteca.listar_livros()


# Exercício 2: Sistema de Gerenciamento de Veículos
# Desenvolva um sistema de gerenciamento de uma frota de veículos.

# Classe Base: Veiculo
# Atributos: marca, modelo, ano, quilometragem
# Métodos: dirigir (aumenta a quilometragem)

# Classes Derivadas: Carro, Caminhao, Moto
# Atributos específicos: capacidade de carga (para Caminhao), tipo de combustível (para Carro), tipo de motor (para
# Moto)

# Classe: Frota
# Atributos: lista de veículos
# Métodos: adicionar veículo, remover veículo, listar veículos

class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, quilometragem: int, id_veiculo: str):
        self.id_veiculo = id_veiculo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def dirigir(self, distancia_percorrida: int):
        self.quilometragem += distancia_percorrida
        return print(f"Quilometragem atualizada, {self.quilometragem}Km")


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, quilometragem: int, id_veiculo: str, tipo_combustivel: str):
        super().__init__(marca, modelo, ano, quilometragem, id_veiculo)
        self.tipo_combustivel = tipo_combustivel

    def alterar_combustivel(self, novo_combustivel: str):
        self.tipo_combustivel = novo_combustivel
        return print("Combustível atualizado")


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, quilometragem: int, id_veiculo: str, cilindradas: int):
        super().__init__(marca, modelo, ano, quilometragem, id_veiculo)
        self.cilindradas = cilindradas

    def alterar_cilindradas(self, nova_cilindrada: int):
        self.cilindradas = nova_cilindrada
        return print("Cilindrada atualizada")


class Caminhao(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, quilometragem: int, id_veiculo: str,
                 capacidade_de_carga: int):
        super().__init__(marca, modelo, ano, quilometragem, id_veiculo)
        self.capacidade_de_carga = capacidade_de_carga

    def alterar_capacidade(self, nova_capacidade: int):
        self.capacidade_de_carga = nova_capacidade
        return print("Capacidade atualizada")


class Frota:
    def __init__(self):
        self.lista_veiculos = []

    def adicionar_veiculo(self, veiculo: Carro | Caminhao | Moto):
        for componente in self.lista_veiculos:
            if componente.id_veiculo == veiculo.id_veiculo:
                return print("Veículo já adicionado")
        self.lista_veiculos.append(veiculo)
        return print("Veículo cadastrado")

    def remover_veiculo(self, id_veiculo: str):
        for veiculo in self.lista_veiculos:
            if veiculo.id_veiculo == id_veiculo:
                self.lista_veiculos.remove(veiculo)
                print("Veículo removido!")
                return True
        print("Veículo não encontrado")
        return False

    def listar_veiculos(self):
        for veiculo in self.lista_veiculos:
            print(f"Marca: {veiculo.marca}, Modelo: {veiculo.modelo}, Ano: {veiculo.ano}, Id: {veiculo.id_veiculo}")
        return self.lista_veiculos

    def __str__(self):
        lista = ""
        for veiculo in self.lista_veiculos:
            lista += f"Marca: {veiculo.marca}, Modelo: {veiculo.modelo}, Ano: {veiculo.ano}, Id: {veiculo.id_veiculo}\n"
        return lista


# Testando a classe Veiculo e suas funções
# veiculo1 = Veiculo(marca="Toyota", modelo="Corolla", ano=2010, quilometragem=120000, id_veiculo="V001")
# veiculo1.dirigir(100)

# Testando a classe Carro e suas funções
# carro = Carro(marca="Honda", modelo="Civic", ano=2015, quilometragem=50000, id_veiculo="C001", tipo_combustivel="Gasolina")
# carro.dirigir(200)
# carro.alterar_combustivel("Etanol")

# Testando a classe Moto e suas funções
# moto = Moto(marca="Yamaha", modelo="YZF-R3", ano=2020, quilometragem=10000, id_veiculo="M001", cilindradas=321)
# moto.dirigir(50)
# moto.alterar_cilindradas(400)

# Testando a classe Caminhão e suas funções
# caminhao = Caminhao(marca="Volvo", modelo="FH", ano=2018, quilometragem=150000, id_veiculo="CA001", capacidade_de_carga=18000)
# caminhao.dirigir(300)
# caminhao.alterar_capacidade(20000)

# Testando a classe Frota e suas funções
# frota = Frota()
# frota.adicionar_veiculo(carro)
# frota.adicionar_veiculo(moto)
# frota.adicionar_veiculo(caminhao)

# frota.listar_veiculos()
# frota.remover_veiculo("C001")
# frota.listar_veiculos()
# print(frota)


# Exercício 3: Sistema de Gerenciamento de Funcionários
# Crie um sistema para gerenciar funcionários de uma empresa.

# Classe Base: Funcionario

# Atributos: nome, ID, salário
# Métodos: aumentar salário

# Classes Derivadas: Gerente, Engenheiro, Vendedor

# Atributos específicos: departamento (para Gerente), área de especialização (para Engenheiro), comissão (para Vendedor)
# Métodos específicos: implementar métodos específicos de cada tipo de funcionário

# Classe: Empresa

# Atributos: nome da empresa, lista de funcionários
# Métodos: contratar funcionário, demitir funcionário, listar funcionários, calcular folha de pagamento

class Funcionario:
    def __init__(self, nome: str, id: str, salario: float):
        self.nome = nome
        self.id = id
        self.salario = salario

    def aumentar_salario(self, novo_salario: float):
        self.salario = novo_salario
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome: str, id: str, salario: float, departamento: str):
        super().__init__(nome, id, salario)
        self.departamento = departamento

    def mudar_departamento(self, novo_departamento: str):
        self.departamento = novo_departamento
        return self.departamento


class Engenheiro(Funcionario):
    def __init__(self, nome: str, id: str, salario: float, area_de_especializacao: str):
        super().__init__(nome, id, salario)
        self.area_de_especializacao = area_de_especializacao

    def mudar_area_de_especializacao(self, nova_area: str):
        self.area_de_especializacao = nova_area


class Vendedor(Funcionario):
    def __init__(self, nome: str, id: str, salario: float, comissao: float):
        super().__init__(nome, id, salario)
        self.comissao = comissao

    def mudar_comissao(self, nova_comissao: float):
        self.comissao = nova_comissao
        return self.comissao


class Empresa:
    def __init__(self, nome_empresa: str):
        self.nome = nome_empresa
        self.funcionarios = []

    def contratar_funcionario(self, funcionario: Gerente | Engenheiro | Vendedor):
        self.funcionarios.append(funcionario)
        return "Funcionário Contratado!"

    def demitir_funcionario(self, id: str):
        for funcionario in self.funcionarios:
            if funcionario.id == id:
                self.funcionarios.remove(funcionario)
                return "Funcionário Demitido!"
        return "Funcionário Não Encontrado"

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            funcao = "Funcionário"
            if isinstance(funcionario, Gerente):
                funcao = "Gerente"
            if isinstance(funcionario, Engenheiro):
                funcao = "Engenheiro"
            if isinstance(funcionario, Vendedor):
                funcao = "Vendedor"
            print(
                f"Nome: {funcionario.nome} | Id: {funcionario.id} | Salário: R${funcionario.salario:.2f} | Função: {funcao}")

    def folha_de_pagamento_total(self):
        folha_de_pagamento = 0
        for funcionario in self.funcionarios:
            folha_de_pagamento += funcionario.salario
        print(f"Folha de Pagamento: R${folha_de_pagamento:.2f}")
        return folha_de_pagamento


# Testando a classe Funcionario e suas funções
# funcionario1 = Funcionario(nome="Carlos", id="F001", salario=3000.0)
# print(funcionario1.aumentar_salario(3500.0))  # Esperado: 3500.0

# Testando a classe Gerente e suas funções
# gerente = Gerente(nome="Alice", id="G001", salario=5000.0, departamento="Vendas")
# print(gerente.aumentar_salario(5500.0))  # Esperado: 5500.0
# print(gerente.mudar_departamento("Marketing"))  # Esperado: "Marketing"

# Testando a classe Engenheiro e suas funções
# engenheiro = Engenheiro(nome="Bruno", id="E001", salario=4000.0, area_de_especializacao="Software")
# print(engenheiro.aumentar_salario(4500.0))  # Esperado: 4500.0
# engenheiro.mudar_area_de_especializacao("Hardware")
# print(engenheiro.area_de_especializacao)  # Esperado: "Hardware"

# Testando a classe Vendedor e suas funções
# vendedor = Vendedor(nome="Daniela", id="V001", salario=2500.0, comissao=5.0)
# print(vendedor.aumentar_salario(3000.0))  # Esperado: 3000.0
# print(vendedor.mudar_comissao(7.0))  # Esperado: 7.0

# Testando a classe Empresa e suas funções
# empresa = Empresa(nome_empresa="TechCorp")
# print(empresa.contratar_funcionario(gerente))  # Esperado: "Funcionário Contratado!"
# print(empresa.contratar_funcionario(engenheiro))  # Esperado: "Funcionário Contratado!"
# print(empresa.contratar_funcionario(vendedor))  # Esperado: "Funcionário Contratado!"

# empresa.listar_funcionarios()
# Esperado:
# Nome: Alice | Id: G001 | Salário: 5500.0 | Função: Gerente
# Nome: Bruno | Id: E001 | Salário: 4500.0 | Função: Engenheiro
# Nome: Daniela | Id: V001 | Salário: 3000.0 | Função: Vendedor

# print(empresa.demitir_funcionario("G001"))  # Esperado: "Funcionário Demitido!"
# print(empresa.demitir_funcionario("F002"))  # Esperado: "Funcionário Não Encontrado"

# empresa.listar_funcionarios()
# Esperado:
# Nome: Bruno | Id: E001 | Salário: 4500.0 | Função: Engenheiro
# Nome: Daniela | Id: V001 | Salário: 3000.0 | Função: Vendedor

# print(empresa.folha_de_pagamento_total())  # Esperado: Folha de Pagamento: R$7500.00


# Exercício 4: Sistema de Gestão de Curso Online
# Desenvolva um sistema para gerenciar cursos online.

# Classe Base: Curso

# Atributos: nome do curso, código do curso, lista de alunos
# Métodos: adicionar aluno, remover aluno, listar alunos

# Classe: Aluno

# Atributos: nome, ID do aluno, cursos matriculados (lista de cursos)
# Métodos: matricular em curso, cancelar matrícula

# Classe: Plataforma

# Atributos: nome da plataforma, lista de cursos
# Métodos: adicionar curso, remover curso, listar cursos
class Aluno:
    def __init__(self, nome: str, id: str):
        self.nome = nome
        self.id = id
        self.cursos = []

    def matricular(self, curso):
        if not isinstance(curso, Curso):
            return "Erro: Não é uma instância da classe Curso"
        for course in self.cursos:
            if course.nome == curso.nome:
                return "Já matriculado nesse curso"
        self.cursos.append(curso)
        return f"Matriculado no curso {curso.nome}"

    def desmatricular(self, codigo_curso: str):
        for course in self.cursos:
            if course.codigo.lower() == codigo_curso.lower():
                self.cursos.remove(course)
                return f"Desmatricula do curso [{course.nome}] confirmada"
        return f"Curso não encontrado"


class Curso:
    def __init__(self, nome: str, codigo_curso: str):
        self.nome = nome
        self.codigo = codigo_curso
        self.lista_alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        for estudante in self.lista_alunos:
            if estudante.id == aluno.id:
                return "Aluno já cadastrado"
        self.lista_alunos.append(aluno)
        return "Aluno Cadastrado"

    def remover_aluno(self, id_aluno: str):
        for aluno in self.lista_alunos:
            if aluno.id == id_aluno:
                self.lista_alunos.remove(aluno)
                return "Aluno Removido"
        return "Aluno não encontrado"

    def listar_alunos(self):
        for aluno in self.lista_alunos:
            if len(aluno.cursos) == 0:
                print(f"Nome: {aluno.nome} | Id: {aluno.id} | Cursos Matriculados: Nenhum")
                return
            cursos_matriculados = ""
            for curso in aluno.cursos:
                if len(cursos_matriculados) == 0:
                    cursos_matriculados += f"{curso.nome.capitalize()}"
                else:
                    cursos_matriculados += f" | {curso.nome.capitalize()}"
            print(f"Nome: {aluno.nome} | Id: {aluno.id} | Cursos Matriculados: {cursos_matriculados}")
        return self.lista_alunos


class Plataforma:
    def __init__(self, nome_plataforma: str):
        self.nome = nome_plataforma
        self.lista_cursos = []

    def adicionar_curso(self, curso: Curso):
        for course in self.lista_cursos:
            if (course.codigo.lower() == curso.codigo.lower() or
                    course.nome.lower().replace(" ", "") == curso.nome.lower().replace(" ", "")):
                return "Curso já cadastrado"
        self.lista_cursos.append(curso)
        return "Curso Cadastrado"

    def remover_curso(self, codigo_curso: str):
        for course in self.lista_cursos:
            if (course.codigo.lower() == codigo_curso.lower() or
                    course.nome.lower().replace(" ", "") == codigo_curso.lower().replace(" ", "")):
                self.lista_cursos.remove(course)
                return "Curso Removido da Plataforma"
        return "Curso Não Encontrado"

    def listar_cursos(self):
        for course in self.lista_cursos:
            print(f"Nome: {course.nome} | Id: {course.codigo} | Qnt. Alunos: {len(course.lista_alunos)}")
        return self.lista_cursos


# Criando instâncias da classe Curso
# curso1 = Curso(nome="Matemática", codigo_curso="MAT101")
# curso2 = Curso(nome="História", codigo_curso="HIS101")
# curso3 = Curso(nome="Física", codigo_curso="FIS101")

# Criando instância da classe Plataforma
# plataforma = Plataforma(nome_plataforma="EducaOnline")

# Adicionar cursos à plataforma
# print(plataforma.adicionar_curso(curso1))  # Saída esperada: Curso Cadastrado
# print(plataforma.adicionar_curso(curso2))  # Saída esperada: Curso Cadastrado
# print(plataforma.adicionar_curso(curso1))  # Saída esperada: Curso já cadastrado
# print(plataforma.adicionar_curso(curso3))  # Saída esperada: Curso Cadastrado

# Listar cursos na plataforma
# plataforma.listar_cursos()
# Saída esperada:
# Nome: Matemática | Id: MAT101 | Qnt. Alunos: 0
# Nome: História | Id: HIS101 | Qnt. Alunos: 0
# Nome: Física | Id: FIS101 | Qnt. Alunos: 0

# Remover cursos da plataforma
# print(plataforma.remover_curso("MAT101"))  # Saída esperada: Curso Removido da Plataforma
# print(plataforma.remover_curso("MAT101"))  # Saída esperada: Curso Não Encontrado

# Listar cursos após remoção
# plataforma.listar_cursos()
# Saída esperada:
# Nome: História | Id: HIS101 | Qnt. Alunos: 0
# Nome: Física | Id: FIS101 | Qnt. Alunos: 0

# Adicionar um aluno ao curso
# aluno1 = Aluno(nome="João", id="A001")
# print(curso2.adicionar_aluno(aluno1))  # Saída esperada: Aluno Cadastrado

# Listar cursos após adicionar aluno
# plataforma.listar_cursos()
# Saída esperada:
# Nome: História | Id: HIS101 | Qnt. Alunos: 1
# Nome: Física | Id: FIS101 | Qnt. Alunos: 0

# Exercício 5: Sistema de Controle de Estoque
# Crie um sistema para gerenciar o estoque de uma loja.

# Classe Base: Produto

# Atributos: nome do produto, código do produto, quantidade em estoque, preço
# Métodos: adicionar ao estoque, remover do estoque, ajustar preço

# Classe: Fornecedor

# Atributos: nome do fornecedor, lista de produtos fornecidos
# Métodos: fornecer produto (aumenta o estoque)

# Classe: Loja

# Atributos: nome da loja, lista de produtos, lista de fornecedores Métodos: adicionar produto, remover produto,
# listar produtos, adicionar fornecedor, remover fornecedor, listar fornecedores

class Produto:
    def __init__(self, nome: str, codigo: str, qnt_estoque: int, preco: float):
        self.nome = nome
        self.codigo = codigo
        self.qnt_estoque = qnt_estoque
        self.preco = preco

    def adicionar_ao_estoque(self, quantidade: int):
        self.qnt_estoque += quantidade
        return self.qnt_estoque

    def remover_do_estoque(self, quantidade: int):
        self.qnt_estoque += quantidade
        return self.qnt_estoque

    def ajustar_preco(self, novo_preco: float):
        self.preco += novo_preco
        return self.preco


class Fornecedor:
    def __init__(self, nome_do_fornecedor: str, lista_de_produtos_fornecidos: list[str]):
        self.nome = nome_do_fornecedor
        self.produtos_fornecidos = lista_de_produtos_fornecidos

    def fornecer_produto(self, produto: Produto, quantidade: int):
        if produto.nome in self.produtos_fornecidos:
            produto.qnt_estoque += quantidade
        return produto.qnt_estoque


class Loja:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_de_produtos = []
        self.lista_de_fornecedores = []

    def adicionar_produto(self, produto: Produto):
        if len(self.lista_de_produtos) == 0:
            self.lista_de_produtos.append(produto)
            return self.lista_de_produtos
        for product in self.lista_de_produtos:
            if product.codigo == produto.codigo:
                return "Produto Já Cadastrado"
        self.lista_de_produtos.append(produto)
        return self.lista_de_produtos

    def remover_produto(self, codigo_produto: str):
        if len(self.lista_de_produtos) == 0:
            return "Lista Vazia!"
        for product in self.lista_de_produtos:
            if product.codigo == codigo_produto:
                self.lista_de_produtos.remove(product)
                return "Produto Removido!"
        return "Produto Não Encontrado!"

    def listar_produtos(self):
        for produto in self.lista_de_produtos:
            print(f"Nome: {produto.nome} | Código: {produto.codigo} | Qnt. Estoque: {produto.qnt_estoque}"
                  f" | Preço: R${produto.preco:.2f}")
        return self.lista_de_produtos

    def adicionar_fornecedor(self, fornecedor: Fornecedor):
        if len(self.lista_de_fornecedores) == 0:
            self.lista_de_fornecedores.append(fornecedor)
            return self.lista_de_fornecedores
        for provider in self.lista_de_fornecedores:
            if provider.nome.lower() == fornecedor.nome.lower():
                return "Produto Já Cadastrado"
        self.lista_de_produtos.append(fornecedor)
        return self.lista_de_fornecedores

    def remover_fornecedor(self, nome_fornecedor: str):
        for fornecedor in self.lista_de_fornecedores:
            if fornecedor.nome == nome_fornecedor:
                self.lista_de_fornecedores.remove(fornecedor)
                return "Fornecedor Removido!"
        return "Fornecedor não encontrado!"

    def listar_fornecedores(self):
        for fornecedor in self.lista_de_fornecedores:
            lista_de_produtos = ""
            for produto in fornecedor.produtos_fornecidos:
                if len(lista_de_produtos) == 0:
                    lista_de_produtos = produto.capitalize()
                lista_de_produtos += f" | {produto}"
            print(f"None Fornecedor: {fornecedor.nome}, Produtos Fornecidos: {lista_de_produtos}")

# Dicas para Resolver os Exercícios:
# Planejamento: Antes de começar a codificar, planeje as classes e seus atributos/métodos. Faça um diagrama de
# classes se necessário. Modularidade: Mantenha seu código modular, criando classes separadas para diferentes
# entidades. Testes: Após implementar cada classe e método, escreva testes para garantir que eles funcionem
# corretamente. Refatoração: Revise e refatore seu código para melhorar a legibilidade e a eficiência.

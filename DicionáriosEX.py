# Exemplo 1: Criando um Dicionário e Acessando Valores
# Criando um dicionário
pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'Wonderland'
}
# Acessando valores usando chaves
print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")

# Exemplo 2: Modificando Valores em um Dicionário
# Modificando valores
pessoa['idade'] = 31
pessoa['cidade'] = 'Outra Cidade'
# Exibindo o dicionário atualizado
print(pessoa)

# Exemplo 3: Adicionando Novos Pares Chave-Valor
# Adicionando um novo par chave-valor
pessoa['profissao'] = 'Desenvolvedor'
# Exibindo o dicionário atualizado
print(pessoa)

# Exemplo 4: Iterando sobre Chaves e Valores
# Iterando sobre chaves
for chave in pessoa:
    print(chave)
# Iterando sobre valores
for valor in pessoa.values():
    print(valor)
# Iterando sobre pares chave-valor
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Exemplo 5: Verificando se uma Chave Existe
# Verificando se uma chave existe
if 'idade' in pessoa:
    print("A chave 'idade' existe no dicionário.")

# Exemplo 6: Removendo um Par Chave-Valor
# Removendo um par chave-valor
del pessoa['cidade']
# Exibindo o dicionário atualizado
print(pessoa)

# Exemplo 7: Agenda Telefônica
agenda = {
    'Alice': '123-456-7890',
    'Bob': '987-654-3210',
    'Charlie': '555-123-4567'
}
# Acessando números de telefone
print(f"Número de telefone de Alice: {agenda['Alice']}")

# Exemplo 8: Contagem de Palavras em um Texto
texto = "Python é uma linguagem de programação poderosa e fácil de aprender."
# Contagem de palavras usando um dicionário
contagem_palavras = {}
palavras = texto.split()  # Cria uma lista com as palavras separadas conforme os espaços
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1  # Retorna o valor associado à chave palavra no
    # Dicionário contagem_palavras. Se a chave não existir, retorna 0 (o valor padrão fornecido como segundo argumento).
    # contagem_palavras[palavra] = ... + 1: Incrementa o valor associado à chave palavra em 1. Se a palavra ainda
    # não estiver no dicionário, cria uma nova entrada com o valor 1.
print(contagem_palavras)

# Exemplo 9: Configurações de Aplicativo
configuracoes_app = {'idioma': 'portugues', 'tema_escuro': True, 'fonte': 'Arial', 'tamanho_fonte': 16}
# Modificando configurações
configuracoes_app['tamanho_fonte'] = 16
# Exibindo configurações
print(configuracoes_app)

# Exemplo 10: Registro de Compras
registro_compras = [
    {'produto': 'Notebook', 'preco': 1200.00, 'quantidade': 1},
    {'produto': 'Mouse', 'preco': 20.00, 'quantidade': 2},
    {'produto': 'Teclado', 'preco': 40.00, 'quantidade': 1}
]
# Calculando o total da compra
total = sum(item['preco'] * item['quantidade'] for item in registro_compras)
print(f"Total da compra: R${total:.2f}")

# Exemplo 11: Controle de Estoque
estoque = {
    'Laptop': 10,
    'Smartphone': 20,
    'Tablet': 15
}
# Adicionando itens ao estoque
estoque['Impressora'] = 5
# Atualizando a quantidade de itens vendidos
estoque['Laptop'] -= 2
# Exibindo estoque
print(estoque)

# Exemplo 12: Votação em uma Enquete
enquete = {}
# Simulação de votos em uma enquete
votos = ['opcao1', 'opcao2', 'opcao1', 'opcao3', 'opcao2', 'opcao1']
for voto in votos:
    enquete[voto] = enquete.get(voto, 0) + 1
# Exibindo resultados
for opcao, votos in enquete.items():
    print(f"{opcao}: {votos} votos")

# Exemplo 13: Gerenciamento de Notas de Estudantes
alunos = {
    'Alice': [85, 90, 92],
    'Bob': [78, 80, 88],
    'Charlie': [92, 95, 89]
}
# Calculando médias dos alunos
for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno}: Média = {media:.2f}")

# Exemplo 14: Dados de Usuários em um Sistema
usuarios = {
    'alice123': {'nome': 'Alice', 'idade': 28, 'email': 'alice@example.com'},
    'bob456': {'nome': 'Bob', 'idade': 35, 'email': 'bob@example.com'}
}
# Acessando dados de usuários
usuario_id = 'alice123'
print(f"Nome: {usuarios[usuario_id]['nome']}, Idade: {usuarios[usuario_id]['idade']}")

# Exemplo 15: Registro de Reservas em um Hotel
reservas_hotel = {
    'quarto101': {'nome_cliente': 'Alice', 'noites': 3, 'total_pago': 300},
    'quarto102': {'nome_cliente': 'Bob', 'noites': 2, 'total_pago': 200}
}
# Adicionando nova reserva
reservas_hotel['quarto103'] = {'nome_cliente': 'Charlie', 'noites': 4, 'total_pago': 400}
# Exibindo informações de reservas
for quarto, reserva in reservas_hotel.items():
    print(f"Quarto: {quarto}, Cliente: {reserva['nome_cliente']}, Noites: {reserva['noites']}, Total Pago: "
          f"{reserva['total_pago']}")

# Exemplo 16: Controle de Estoque de uma Loja de Roupas
estoque_roupas = {
    'camisetas': {'quantidade': 100, 'preco_unitario': 20.0},
    'calcas': {'quantidade': 50, 'preco_unitario': 40.0},
    'blusas': {'quantidade': 75, 'preco_unitario': 30.0}
}
# Calculando o valor total do estoque
total_estoque = sum(item['quantidade'] * item['preco_unitario'] for item in estoque_roupas.values())
print(f"Valor total do estoque: R${total_estoque:.2f}")

#  17: Rastreamento de Entregas
entregas = {
    'pedido123': {'status': 'em_transito', 'data_entrega': None},
    'pedido124': {'status': 'entregue', 'data_entrega': '2022-03-01'},
    'pedido125': {'status': 'pendente', 'data_entrega': None}
}
# Atualizando status e datas de entrega
entregas['pedido123']['status'] = 'entregue'
entregas['pedido123']['data_entrega'] = '2022-03-02'
# Exibindo informações de entregas
for pedido, info_entrega in entregas.items():
    print(f"Pedido: {pedido}, Status: {info_entrega['status']}, Data de Entrega: {info_entrega['data_entrega']}")

# Exemplo 18: Configurações de Aplicativo (Atualizado)
configuracoes_app = {
    'idioma': 'portugues',
    'tema_escuro': True,
    'fonte': 'Arial',
    'tamanho_fonte': 14
}
# Modificando configurações
configuracoes_app.update({'tamanho_fonte': 16, 'novo_recurso': True})
# Exibindo configurações
for chave, valor in configuracoes_app.items():
    print(f"{chave.capitalize()}: {valor}")

# Exemplo 19: Análise de Dados de Vendas
dados_vendas = [
    {'produto': 'Laptop', 'quantidade_vendida': 10, 'preco_unitario': 1200.00},
    {'produto': 'Mouse', 'quantidade_vendida': 20, 'preco_unitario': 20.00},
    {'produto': 'Teclado', 'quantidade_vendida': 15, 'preco_unitario': 40.00}
]
# Calculando receita total
receita_total = sum(item['quantidade_vendida'] * item['preco_unitario'] for item in dados_vendas)
print(f"Receita total: R${receita_total:.2f}")

# Exemplo 20: Catálogo de Livros em uma Biblioteca
catalogo_livros = {
    'ISBN123': {'titulo': 'Aventuras no Mundo da Programação', 'autor': 'Coder', 'ano_publicacao': 2021, 'genero':
        'Tecnologia'},
    'ISBN456': {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano_publicacao': 1954, 'genero':
        'Fantasia'},
    'ISBN789': {'titulo': 'Ponto de Inflexão', 'autor': 'Malcolm Gladwell', 'ano_publicacao': 2000, 'genero':
        'Não Ficção'}
}
# Exibindo informações do catálogo
for isbn, livro_info in catalogo_livros.items():
    print(f"ISBN: {isbn}")
    print(f"Título: {livro_info['titulo']}")
    print(f"Autor: {livro_info['autor']}")
    print(f"Ano de Publicação: {livro_info['ano_publicacao']}")
    print(f"Gênero: {livro_info['genero']}")
    print(40 * '=')

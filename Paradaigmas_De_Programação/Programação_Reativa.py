# Programação Reativa é um paradigma de programação focado em trabalhar com fluxos de dados assíncronos e a propagação
# de mudanças. Em vez de tratar eventos individuais como ocorrências isoladas, a programação reativa permite que você
# defina uma série de transformações e reações a fluxos contínuos de dados.

# Princípios Básicos Fluxos de Dados: Sequências de eventos que ocorrem ao longo do tempo. Observáveis: Fontes de
# dados que emitem eventos aos quais você pode se inscrever (observer pattern). Observadores: Entidades que se
# inscrevem para receber eventos de um observável. Operadores Reativos: Ferramentas que permitem manipular, combinar,
# e transformar fluxos de dados (e.g., map, filter, merge).

# Vantagens
# Assincronismo: Facilita a gestão de operações assíncronas e concorrentes.
# Composição: Permite compor fluxos de dados de maneira declarativa.
# Escalabilidade: Adequado para sistemas distribuídos e aplicações com alto volume de eventos.

# Exemplos de Uso Interfaces de Usuário: Atualizar a UI em resposta a eventos de entrada do usuário sem bloquear o
# fluxo principal de execução. Aplicações Web: Gestão de streams de dados contínuos, como feeds de notícias ou
# atualizações em tempo real. Sistemas de Monitoramento: Coleta e análise contínua de dados de sensores ou logs.
# Programação Reativa em Python Uma biblioteca popular para programação reativa em Python é o RxPy (ReactiveX for
# Python). Vou demonstrar alguns exemplos básicos usando RxPy.

# Instalação
# Para instalar o RxPy, você pode usar o pip:
# pip install rx

# Exemplo 1: Fluxo Simples de Dados
import rx
from rx import operators as ops

# Criar um observável que emite uma sequência de números
observable = rx.from_([1, 2, 3, 4, 5])

# Definir um observador que imprime os valores recebidos
observer = observable.pipe(
    ops.map(lambda x: x * 2),
    ops.filter(lambda x: x > 5)
)

# Subscrição ao observável
observer.subscribe(
    on_next=lambda x: print(f"Recebido: {x}"),
    on_error=lambda e: print(f"Erro: {e}"),
    on_completed=lambda: print("Concluído")
)

# Exemplo 2: Integração com Tempo (Intervalos)
import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler
import time

# Função para criar um intervalo de tempo
observable = rx.interval(1.0)  # Emite um valor a cada segundo

# Definir um observador que imprime os valores recebidos
observer = observable.pipe(
    ops.map(lambda x: x * 2),
    ops.filter(lambda x: x % 3 == 0)
)

# Subscrição ao observável
subscription = observer.subscribe(
    on_next=lambda x: print(f"Recebido: {x}"),
    on_error=lambda e: print(f"Erro: {e}"),
    on_completed=lambda: print("Concluído")
)

# Deixar o programa rodando por um tempo para observar a saída
time.sleep(10)
subscription.dispose()  # Cancelar a subscrição

# Conclusão
# A programação reativa facilita a criação de aplicações que respondem eficientemente a eventos assíncronos e fluxos de
# dados contínuos. Em Python, bibliotecas como RxPy fornecem ferramentas poderosas para implementar esses padrões de
# maneira limpa e declarativa.

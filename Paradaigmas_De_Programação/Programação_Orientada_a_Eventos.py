# A Programação Orientada a Eventos (POE) é um paradigma de programação no qual o fluxo de controle é determinado por
# eventos, como ações do usuário, entradas de dados, ou notificações de sistemas externos. Em vez de um fluxo de
# execução linear típico, onde as instruções são executadas sequencialmente, na POE, o programa responde a eventos
# que ocorrem durante sua execução.

# Principais conceitos da POE incluem:

# Evento: Um acontecimento significativo que ocorre durante a execução do programa. Pode ser desencadeado por
# interações do usuário, mudanças de estado do sistema, ou outras fontes.

# Ouvinte (Listener): Um objeto que espera por eventos específicos e responde a eles executando uma ação ou função
# correspondente.

# Despachante de Eventos (Event Dispatcher): Componente responsável por receber eventos e encaminhá-los aos ouvintes
# registrados para processamento.

# Loop de Eventos (Event Loop): Estrutura de controle responsável por aguardar eventos, encaminhá-los ao despachante
# de eventos e executar as ações associadas a eles.

# Gatilho (Trigger): Uma ação que inicia a ocorrência de um evento.

import tkinter as tk


def on_button_click():
    label.config(text="O botão foi clicado!")


# Criando a janela
window = tk.Tk()
window.geometry("300x200")

# Criando um rótulo
label = tk.Label(window, text="Pressione o botão")
label.pack(pady=20)

# Criando um botão
button = tk.Button(window, text="Clique aqui", command=on_button_click)
button.pack()

# Iniciando o loop de eventos
window.mainloop()

# Implementação Básica de um Despachante de Eventos: Escreva uma classe EventDispatcher que permita registrar
# ouvintes para eventos específicos e despachar eventos aos ouvintes correspondentes.
import random
from tkinter import Tk, Frame, Label, Entry, Button


class EventDispatcher:
    def __init__(self, master):
        self.lista = []

        # Padrão App
        master.geometry("680x480")
        master.title('Agenda de Eventos')
        master.iconbitmap("icon.png")

        # Container Geral
        self.widget1 = Frame(master)
        self.widget1.pack()

        # Titulo
        self.msg = Label(self.widget1, text="Adicionar ou Remover Eventos da Agenda")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        # Nome do evento
        self.eventolabel = Label(self.widget1, text="Evento")
        self.eventolabel.pack()

        self.evento = Entry(self.widget1)
        self.evento["width"] = 30
        self.evento["font"] = ("Verdana", "10", "italic", "bold")
        self.evento.pack()

        # Adicionar Evento
        self.add_event_button = Button(self.widget1)
        self.add_event_button["text"] = "Adicionar Evento a Agenda"
        self.add_event_button["font"] = ("Calibri", "10")
        self.add_event_button["width"] = 30
        self.add_event_button["command"] = self.add_event
        self.add_event_button.pack()

        # Remover Evento
        self.remove_event_button = Button(self.widget1)
        self.remove_event_button["text"] = "Remover Evento a Agenda"
        self.remove_event_button["font"] = ("Calibri", "10")
        self.remove_event_button["width"] = 30
        self.remove_event_button["command"] = self.remove_event
        self.remove_event_button.pack()

        # Exit Button
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 30
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

        # Mensagem do Evento
        self.mensagem = Label(self.widget1, text="")
        self.mensagem.pack()

        # Mostrar eventos
        self.mostrar_eventos = Button(self.widget1)
        self.mostrar_eventos["text"] = "Mostra eventos"
        self.mostrar_eventos["font"] = ("Calibri", "10")
        self.mostrar_eventos["width"] = 30
        self.mostrar_eventos["command"] = self.show_events_list
        self.mostrar_eventos.pack()

        # Mostra eventos
        self.mostra_evento = Label(self.widget1, text="")
        self.mostra_evento.pack()

    def add_event(self):
        evento = self.evento.get().lower().strip()
        if evento not in self.lista:
            self.lista.append(evento)
            self.mensagem["text"] = "Adicionado com Sucesso"
            return f'Adicionado com Sucesso'
        self.mensagem["text"] = "Evento já existe"
        return f'Evento já existe'

    def remove_event(self):
        evento = self.evento.get().lower().strip()
        if evento in self.lista:
            self.lista.remove(evento)
            self.mensagem["text"] = "Removido com Sucesso"
            return f'Removido com Sucesso'
        self.mensagem["text"] = "Evento não Encontrado"
        return f'Evento não encontrado'

    def show_events_list(self):
        self.mostra_evento["text"] = str(self.lista)


# root = Tk()
# EventDispatcher(root)
# root.mainloop()


# Simulação de Controle de Tráfego: Escreva um programa que simule o controle de tráfego de veículos em um
# cruzamento. Cada veículo é representado por um evento que precisa ser despachado para o despachante de eventos
# quando se aproxima do cruzamento.
# Rua disposta em y, -y, x, -x
class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.tempo_pro_cruzamento = 300 / velocidade


# Sistema de Notificações: Implemente um sistema de notificações que permita que diferentes partes de um programa se
# comuniquem por meio de eventos. Por exemplo, uma parte do programa pode gerar um evento quando uma tarefa é
# concluída, e outra parte pode ser notificada desse evento para tomar uma ação apropriada.


# Jogo de Aventura Textual com Eventos: Crie um jogo de aventura textual onde os eventos representam ações do jogador
# e do ambiente. Por exemplo, o jogador pode digitar comandos como "ir para o norte" ou "pegar item",
# e o jogo responderá gerando eventos correspondentes.

# Simulação de Sistema de Automação Residencial: Escreva um programa que simule um sistema de automação residencial,
# onde os eventos representam a detecção de movimento, mudanças de temperatura, ou acionamento de dispositivos. Os
# ouvintes podem ser configurados para responder a esses eventos ligando ou desligando dispositivos domésticos,
# como luzes ou termostatos.
class Residencia:
    def __init__(self):
        self.luz1 = 'apagada'
        self.televisao = 'desligada'


class App:
    def __init__(self, master):
        casa = Residencia()
        # Regras Padrão
        master.geometry("680x480")
        master.title('Automação Residencial')
        master.iconbitmap("icon.png")

        # Container Geral
        self.widget1 = Frame(master)
        self.widget1.pack()

        # Titulo
        self.msg = Label(self.widget1, text="Minha Casa")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        # Apaga/Acende Lâmpada
        self.add_event_button = Button(self.widget1)
        self.add_event_button["text"] = "Acende Lâmpada"
        self.add_event_button["font"] = ("Calibri", "10")
        self.add_event_button["width"] = 30
        self.add_event_button["command"] = self.interage_lampada
        self.add_event_button.pack()

        # Lig/Des Televisão
        self.add_event_button_tv = Button(self.widget1)
        self.add_event_button_tv["text"] = "Liga TV"
        self.add_event_button_tv["font"] = ("Calibri", "10")
        self.add_event_button_tv["width"] = 30
        self.add_event_button_tv["command"] = self.interage_televisao
        self.add_event_button_tv.pack()

        # Mostra eventos
        self.mostra_evento = Label(self.widget1, text="")
        self.mostra_evento.pack()

    def interage_lampada(self):
        if self.add_event_button["text"] == "Acende Lâmpada":
            self.add_event_button["text"] = "Apaga Lâmpada"
            self.mostra_evento["text"] = "Lâmpada Acesa"
        elif self.add_event_button["text"] == "Apaga Lâmpada":
            self.add_event_button["text"] = "Acende Lâmpada"
            self.mostra_evento["text"] = "Lâmpada Apagada"

    def interage_televisao(self):
        if self.add_event_button_tv["text"] == "Liga TV":
            self.add_event_button_tv["text"] = "Desliga TV"
            self.mostra_evento["text"] = "TV LIGADA"
        elif self.add_event_button_tv["text"] == "Desliga TV":
            self.add_event_button_tv["text"] = "Liga TV"
            self.mostra_evento["text"] = "TV DESLIGADA"


# principal = Tk()
# App(principal)
# principal.mainloop()


# Monitor de Arquivos em Tempo Real: Crie um programa que monitore um diretório em busca de alterações em arquivos.
# Use eventos para notificar quando um novo arquivo é criado, modificado ou excluído
class PopUp:
    def __init__(self, master):
        # Regras Padrão
        master.geometry("680x480")
        master.title('Automação Residencial')
        master.iconbitmap("icon.png")

        # Container Geral
        self.widget1 = Frame(master)
        self.widget1.pack()

        # Titulo
        self.msg = Label(self.widget1, text="Minha Casa")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        # Apaga/Acende Lâmpada
        self.add_event_button = Button(self.widget1)
        self.add_event_button["text"] = "Acende Lâmpada"
        self.add_event_button["font"] = ("Calibri", "10")
        self.add_event_button["width"] = 30
        self.add_event_button["command"] = self.interage_lampada
        self.add_event_button.pack()

        # Lig/Des Televisão
        self.add_event_button_tv = Button(self.widget1)
        self.add_event_button_tv["text"] = "Liga TV"
        self.add_event_button_tv["font"] = ("Calibri", "10")
        self.add_event_button_tv["width"] = 30
        self.add_event_button_tv["command"] = self.interage_televisao
        self.add_event_button_tv.pack()

        # Mostra eventos
        self.mostra_evento = Label(self.widget1, text="")
        self.mostra_evento.pack()

    def interage_lampada(self):
        if self.add_event_button["text"] == "Acende Lâmpada":
            self.add_event_button["text"] = "Apaga Lâmpada"
            self.mostra_evento["text"] = "Lâmpada Acesa"
        elif self.add_event_button["text"] == "Apaga Lâmpada":
            self.add_event_button["text"] = "Acende Lâmpada"
            self.mostra_evento["text"] = "Lâmpada Apagada"

    def interage_televisao(self):
        if self.add_event_button_tv["text"] == "Liga TV":
            self.add_event_button_tv["text"] = "Desliga TV"
            self.mostra_evento["text"] = "TV LIGADA"
        elif self.add_event_button_tv["text"] == "Desliga TV":
            self.add_event_button_tv["text"] = "Liga TV"
            self.mostra_evento["text"] = "TV DESLIGADA"


popup = Tk()
PopUp(popup)
popup.mainloop()

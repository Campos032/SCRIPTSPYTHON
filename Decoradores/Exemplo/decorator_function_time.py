import time

import requests


def cronometro_de_funcao(funcao):
    def cronometro(*args, **kwargs):
        inicio = time.time()
        funcao(*args, **kwargs)
        fim = time.time()
        tempo_de_exec = fim - inicio
        return print(f"Demorou {tempo_de_exec: .2f} segundos")

    return cronometro


@cronometro_de_funcao
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])


pegar_cotacao_dolar()

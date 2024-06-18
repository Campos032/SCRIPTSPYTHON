# A Programação Orientada a Aspectos (POA) é um paradigma de programação que visa separar preocupações transversais,
# como logging, tratamento de exceções, segurança, etc., das preocupações principais de um programa. Ela permite
# modularizar e reutilizar aspectos específicos do código, melhorando a manutenção e a legibilidade do mesmo.

# Em POA, as preocupações transversais são encapsuladas em "aspectos", que são módulos independentes do código
# principal. Estes aspectos são então "tecidos" (ou "weaved") no código principal durante a compilação ou em tempo
# de execução, dependendo da implementação.

# https://www.youtube.com/watch?v=1uvgqbPw-04&pp=ygUicHJvZ3JhbWHDp8OjbyBvcmllbnRhZGEgYSBhc3BlY3Rvcw%3D%3D
# https://pt.wikipedia.org/wiki/Programação_orientada_a_aspecto

import time


# Classe para o aspecto de medição de tempo
class TimeExecutionAspect:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tempo de execução: {execution_time} segundos")
        return result


# Classe alvo
class MinhaClasse:
    def __init__(self):
        pass

    # Método alvo decorado com o aspecto de medição de tempo
    @TimeExecutionAspect
    def meu_metodo(self, arg1, arg2):
        print(f"Executando meu_metodo com argumentos {arg1} e {arg2}")
        time.sleep(1)  # Simulando uma operação que leva tempo


# Criando uma instância da classe
obj1 = MinhaClasse()

# Chamando o método
# obj1.meu_metodo(2, 3, 4)

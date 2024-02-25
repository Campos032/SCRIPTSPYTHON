# Exemplo Básico:
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que é executado se uma exceção do tipo ZeroDivisionError for gerada
    print("Erro: Divisão por zero.")

# Exemplo com else:
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 2
except ZeroDivisionError:
    # Código que é executado se uma exceção do tipo ZeroDivisionError for gerada
    print("Erro: Divisão por zero.")
else:
    # Código que é executado se nenhuma exceção for gerada
    print("Resultado:", resultado)

# Exemplo com finally:
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 2
except ZeroDivisionError:
    # Código que é executado se uma exceção do tipo ZeroDivisionError for gerada
    print("Erro: Divisão por zero.")
else:
    # Código que é executado se nenhuma exceção for gerada
    print("Resultado:", resultado)
finally:
    # Código sempre executado, independentemente de uma exceção ser gerada ou não
    print("Fim do bloco try-except.")

# Exemplo com múltiplos tipos de exceção:
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que é executado se uma exceção do tipo ZeroDivisionError for gerada
    print("Erro: Divisão por zero.")
except TypeError:
    # Código que é executado se uma exceção do tipo TypeError for gerada
    print("Erro: Tipo de dado inválido.")


# Exemplo com raise:
def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero.")
    return a / b


try:
    resultado = divisao(10, 0)
except ZeroDivisionError as e:
    print(e)


# Exemplo com except genérico:
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except Exception as e:
    # Código que é executado se qualquer exceção for gerada
    print("Erro:", e)

# Exemplo com finally sem except:
try:
    # Código que não gera exceção
    resultado = 10 / 2
finally:
    # Código sempre executado, independentemente de uma exceção ser gerada ou não
    print("Fim do bloco try-finally.")

# Exemplo com else e finally sem except:
try:
    # Código que não gera exceção
    resultado = 10 / 2
except ZeroDivisionError:
    # Código que é executado se uma exceção do tipo ZeroDivisionError for gerada
    print("Erro: Divisão por zero.")
else:
    # Código que é executado se nenhuma exceção for gerada
    print("Resultado:", resultado)
finally:
    # Código sempre executado, independentemente de uma exceção ser gerada ou não
    print("Fim do bloco try-except-finally.")

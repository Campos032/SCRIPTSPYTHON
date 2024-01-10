# O comando break é usado para interromper a execução de um loop, mesmo que a condição associada ao loop (while True
# neste caso) ainda seja verdadeira. Aqui estão alguns exemplos de como você pode usar break em estruturas while True:

#
# Exemplo 1: Sair com base em uma condição específica:
while True:
    resposta = input("Digite 'sair' para encerrar o loop: ")

    if resposta.lower() == 'sair':
        print("Encerrando o loop.")
        break

    print("Continuando o loop...")

# Neste exemplo, o loop continua indefinidamente até que o usuário digite "sair". Quando "sair" é digitado, o loop é
# interrompido com o uso de break.
#

#
# Exemplo 2: Sair após um número específico de iterações:
contador = 0

while True:
    print("Executando iteração", contador)

    contador += 1

    if contador >= 5:
        print("Número máximo de iterações alcançado. Encerrando o loop.")
        break

# Neste exemplo, o loop é interrompido após cinco iterações. O break é acionado quando o contador atinge ou excede 5.
#

#
# Exemplo 3: Sair com base em uma condição composta:
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        print("Encerrando o loop.")
        break

    quadrado = numero ** 2
    print("O quadrado de", numero, "é", quadrado)

# Neste exemplo, o loop continua até que o usuário digite 0. Quando 0 é digitado, o loop é interrompido com o break.
#

# O uso do break em loops while True é comum quando você deseja criar um loop infinito que pode ser encerrado com base
# em condições específicas. Certifique-se de usar o break com cuidado para evitar loops infinitos involuntários.

# Desafios 107 e 108
def aumentar(numero, porcento):
    return porcento / 100 * numero + numero


def diminuir(numero, porcento):
    return numero - porcento / 100 * numero


def dobro(num):
    return 2 * num


def metade(num):
    return num / 2


def moeda(num):
    valor = f'R${num:.2f}'
    com_virgula = valor.replace('.', ',')
    return com_virgula

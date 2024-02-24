# A partir do desafio 109
def aumentar(numero, porcento, formatar=True):
    aumento = porcento / 100 * numero + numero
    if formatar:
        return moeda(aumento)
    else:
        return aumento


def diminuir(numero, porcento, formatar=True):
    subtraido = numero - porcento / 100 * numero
    if formatar:
        return moeda(subtraido)
    else:
        return subtraido


def dobro(num, formatar=True):
    dobrado = 2 * num
    if formatar:
        return moeda(dobrado)
    else:
        return dobrado


def metade(num, formatar=True):
    dividido = num / 2
    if formatar:
        return moeda(dividido)
    else:
        return dividido


def moeda(num):
    valor = f'R${num:.2f}'
    com_virgula = valor.replace('.', ',')
    return com_virgula


def resumo(num=0, porcento_mais=0, porcento_menos=0):
    print(33 * '-')
    print(8 * ' ', 'RESUMO DO VALOR')
    print(33 * '-')
    print(f'Preço Analisado: {moeda(num).rjust(14)}')
    print(f'Dobro do preço: {dobro(num).rjust(16)}')
    print(f'Metade do preço: {metade(num).rjust(14)}')
    print(f'{porcento_mais}% de Aumento: {aumentar(num, porcento_mais).rjust(15)}')
    print(f'{porcento_menos}% de Diminuição: {diminuir(num, porcento_menos).rjust(12)}')
    print(33 * '-')

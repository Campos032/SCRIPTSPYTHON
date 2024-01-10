# Variável Composta, Tuplas(São imutáveis)

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')  # Pode-se usar parênteses ou não

for comida in lanche:
    print(f'Eu vou comer {comida}!')

for cont in range(0, len(lanche)):
    print(f'E vou comer {lanche[cont]} na posição {cont}!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}!')

print('Comi pra caramba!')

print(sorted(lanche))  # Mostra a tupla em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)  # irá concatenar
print(c.index(8))  # irá mostrar a primeira posição em que o item aparece
print(sum(c))  # irá somar os itens da tupla

teste = (99, 87, 'Clarêncio')
del teste  # A tupla pode ser modificada apenas a deletando, usando a função del
# print(teste)  # irá retornar erro, pois como a tupla foi deletada ela não existe mais na memória

exemplo = ('Caio', 20, 'M', 78)  # As tuplas em python diferentemente de algumas outras linguagens, suporta mais de
# um tipo de dados

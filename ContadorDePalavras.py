# split() foi usado para dividir uma str em palavras levando em consideração os espaços como divisória , mas também podemos definir dentro dos () o que sera o divisor das palavras como por exemplo ('-')
# e len() nos mostra quantos caracteres tem 
def conta_palavras(texto):
    conta_palavras = texto.split()
    qnt_palavras = len(conta_palavras)
    print(f'Essa frase tem {qnt_palavras} palavras!')


# input é uma função usada para o usuário inserir algo no programa
frase = input('Escreva uma frase:')
print('')
conta_palavras(frase)

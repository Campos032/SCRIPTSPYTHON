def leia_dinheiro():
    num = input('Digite um valor R$: ')
    num1 = num[:]
    num = num.replace(',', '')
    num = num.replace('.', '')
    if num.isnumeric():
        if ',' in num1:
            num1 = num1.replace(',', '.')
        return float(num1)
    else:
        print(f'ERRO: "{num1}" é um preço inválido!')
        return leia_dinheiro()

# Estrutura de repetição com teste lógico

"""c = 1
while c < 11:
    print(c)
    c += 1
print('Fim!')"""

'''n = 1
while n != 0:
    n = int(input('Digite um número:'))
print('Fim!')'''

'''r = 'S'
while r == 'S':
    num = int(input('Digite um número:'))
    r = str(input('Se quer continuar digite [S] ou [N] pra sair:')).upper()
print('Fim!')'''

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')'''

'''contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("Fim!")'''

'''soma = 0
numero = 1
while numero <= 10:
    soma += numero
    numero += 1
print(f"A soma dos números de 1 a 10 é: {soma}")'''

'''numero_secreto = 42
tentativas = 0
while True:
    palpite = int(input("Adivinhe o número: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente.")'''

'''senha_correta = "senha123"
tentativas = 3
while tentativas > 0:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == senha_correta:
        print("Senha correta. Acesso permitido.")
        break
    else:
        print(f"Senha incorreta. Restam {tentativas-1} tentativas.")
        tentativas -= 1'''

'''saldo_conta = 1000
taxa_juros = 0.05
anos = 0
while saldo_conta < 2000:
    saldo_conta += saldo_conta * taxa_juros
    anos += 1

print(f"Demorou {anos} anos para o saldo atingir 2000.")'''








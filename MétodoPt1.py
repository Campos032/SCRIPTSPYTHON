#Input será uma string podendo ter números, letras ou qualquer tipo de caractere, isnumeric é um método usado para verificar se o que tem ná str pode ser convertido em apenas números inteiros, se tiver letras e número isso não poderá acontecer e retornara falso no programa


def se_str_num_int():
  print('')
  num = input('Digite apenas números:') # 1.° Exemplo, 5 pode ser convertido em apenas número inteiro
  print(num.isnumeric())
  print('')


def se_str_alpha():
  print('')
  num = input('Digite apenas letras:')# 2.° Exemplo, A pode ser convertido em apenas letra
  print(num.isalpha())
  print('')


def se_str_alpha_num():
  print('')
  num = input('Digite letras e números:')# 3.° Exemplo, A5 pode ser convertido em apenas letras e números inteiros
  print(num.isalnum())
  print('')


def se_str_alphaupper():
  print('')
  num = input('Digite letras e números:')# 4.° Exemplo, A pode ser convertido em apenas letra maiúscula
  print(num.isupper())
  print('')
#Tem outros tipos de métodos também, que podem ser usadas em outras oportunidades, lembrando que estamos usando os métodos em uma string
  
  
while True:
 print('')
 print('1-Testar se a STRING pode ser convertido em apenas números inteiros.')
 print('2-Testar se a STRING pode ser convertido em apenas letras.')
 print('3-Testar se a STRING pode ser convertida em letras e números.')
 print('4-Testar se a STRING pode ser convertida em letras maiúsculas.')
 print('5-Sair.')
 print('')
 escolha = float(input('Digite o número da operação que você quer executar:'))
 print('')

 if escolha == 5:
  print('Saindo!')
  break
  
 elif escolha == 1:
  se_str_num_int()

 elif escolha == 2:
   se_str_alpha()

 elif escolha == 3:
   se_str_alpha_num()

 elif escolha == 4:
   se_str_alphaupper()

 else:
  print('Escolha inválida, Tente novamente!')
  


 


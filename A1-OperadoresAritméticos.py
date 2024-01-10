# Os operadores em python são +(Soma) -(Subtração) *(Multiplicação) /(Divisão que retorna um número float) **(Potência) 
# //(Divisão inteira 5//2=2) %(Divide e Retorna o Resto)
# Ordem de precedência (), (**), (* / // %), (+-).

def ex_num():
 print('')
 print('Expressão Numérica/Ordem de precedência')
 print('')
 ex1 = 5+3*5
 print('5+3*5 =',ex1)
 ex2 = 3*5+4**2
 print('3*5+4**2 =',ex2)
 ex3 = 3*(5+4)**2
 print('3*(5+4)**2 =',ex3)
 ex4 = 4**3
 print('4**3 =',ex4)
 ex5 = 16%2
 print('16%2 =',ex5)
 ex6 = 16**(1/2)#Fazendo assim conseguimos descobrir a raiz quadrada de 16 se fosse 16**(1/3) teríamos a raiz cúbica e
 # assim por diante
 print('16**(1/2) =',ex6)
 ex7 = pow(2, 5)#pow é uma função do python usada para calcular a potência
 print('pow(2, 5) =',ex7)
 print('')




from pacotes.numeros import operações_matemáticas
from pacotes.strings import strings

print(4 * ' ', 'Operações Matemática Básica')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(f'A soma de {num1} e {num2} é {operações_matemáticas.soma(num1, num2)}')
print(f'A subtração de {num1} e {num2} é {operações_matemáticas.subtracao(num1, num2)}')
print(f'A multiplicação de {num1} e {num2} é {operações_matemáticas.multiplicacao(num1, num2)}')
print(f'A divisão de {num1} e {num2} é {operações_matemáticas.divisao(num1, num2):.2f}')
print()


print(4 * ' ', 'Manipulação de Texto')
frase = str(input('Digite uma frase: '))
print(f'A frase com todas as letras maiúsculas fica da seguinte forma ({strings.maiuscula(frase)})')
print(f'A frase com todas as letras minúsculas fica da seguinte forma ({strings.minuscula(frase)})')

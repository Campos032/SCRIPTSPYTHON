# Código escape ANSI pode ser usado para determinas cores, sendo gerado da seguinte forma \033[0;33;44m
# O 0 corresponde a estilo da letra 0=None 1=Bold 4=Sublinhada 7=Negativa
# O 33 corresponde as cores do texto de 30=Branco 31=Vermelho 32=Verde 33=Amarelo 34=Azul 35=Roxo 36=AzulClaro 37=Cinza
# O 44 corresponde as cores do fundo indo de 40 a 47 na mesma ordem das cores do texto
# Pode se também usar bibliotecas como a (colorama e termcolor)

# Exemplo de como formatar
print('\033[1;30mPython é Foda!\033[m')
print('\033[7;30mPython é foda!\033[m')
print('\033[4;35mPython é foda!\033[m')
# p1 = float(input('\033[1;31mDigite um número\033[m:'))
# p2 = float(input('\033[1;31mDigite outro número\033[m:'))
# print(f'O primeiro número é \033[1;31m{p1}\033[m e o segundo número é \033[1;31m{p2}\033[m!')

# Criando um 'dicionário' das cores
# As cores variam conforme o tema da IDE

cores = {"branco": '\033[0;30m',
         "vermelho": '\033[0;31m',
         "verde": '\033[0;32m',
         "amarelo": '\033[0;33m',
         "azul": '\033[34m',
         "roxo": '\033[0;35m',
         "azulclaro": '\033[0;36m',
         "cinza": '\033[0;37m',
         "fundobranco": '\033[0;40m',
         "fundovermelho": '\033[0;41m',
         "fundoverde": '\033[0;42m',
         "fundoamarelo": '\033[0;43m',
         "fundoazul": '\033[0;44m',
         "fundoroxo": '\033[0;45m',
         "fundoazulclaro": '\033[0;46m',
         "fundocinza": '\033[0;47m',
         "termina": '\033[m',
         "pretoebranco": '\033[7;30m'}  # e etc

print(f'{cores["fundoazulclaro"]}Pythonando{cores["termina"]}')

print('')
print('Verificador de STR')
print('')
alway = input('Digite algo:')
print('')
print('Qual o tipo primitivo?',type(alway))
print('É numérico?', alway.isnumeric())
print('É alfabético?', alway.isalpha())
print('É letra maiúscula?', alway.isupper())
print('É letra minúscula?', alway.islower())
print('Está capitalizada(Começo das palavras em maiúsculo e o restante em minúsculo)?', alway.istitle())
print('É alfanumérico?', alway.isalnum())
print('É somente espaço vazio?', alway.isspace())



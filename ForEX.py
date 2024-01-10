# Certamente, aqui estão alguns exemplos de laços 'for' em Python:

# 1. **Iterando sobre uma Lista
# python
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

# 2. **Usando a Função `range`:**
# python
for i in range(5):
    print(i)

# 3. **Iterando sobre uma String:**
# python
palavra = 'Python'
for letra in palavra:
    print(letra)

# 4. **Desempacotando Tuplas:**
# python
coordenadas = [(1, 2), (3, 4), (5, 6)]
for x, y in coordenadas:
    print(f'x: {x}, y: {y}')

# 5. **Usando `enumerate` para Obter Índices:**
# python
cores = ['vermelho', 'verde', 'azul']
for indice, cor in enumerate(cores):
    print(f'Índice: {indice}, Cor: {cor}')

# 6. **Iterando sobre Dicionários:**
# ```python
estudante_notas = {'Alice': 90, 'Bob': 80, 'Charlie': 95}
for aluno, nota in estudante_notas.items():
    print(f'{aluno}: {nota}')

# Estes são apenas alguns exemplos, e o 'for' em Python é bastante flexível, podendo ser utilizado em várias situações
# para iterar sobre diferentes tipos de dados.

frase = str(input('Escreva uma frase:')).lower()
frase_sem_espaços = frase.replace(' ', '')
reversestr = ''
for letras in range(len(frase_sem_espaços) - 1, -1, -1):
    reversestr += frase_sem_espaços[letras]
print(reversestr)

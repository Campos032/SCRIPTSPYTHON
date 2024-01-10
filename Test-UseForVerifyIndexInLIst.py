# Criar uma lista de elementos
minha_lista = [10, 20, 30, 40, 20, 50, 60, 70, 20]

# Definir o elemento que deseja encontrar
elemento = 20

# Usar uma lista para armazenar os índices
indices = []

# Iterar sobre a lista e verificar cada elemento
for indice, valor in enumerate(minha_lista):
    if valor == elemento:
        indices.append(indice)

# Imprimir o resultado
if indices:
    print(f"O elemento {elemento} aparece nos índices: {indices}")
else:
    print(f"O elemento {elemento} não está na lista.")

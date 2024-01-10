from datetime import datetime

data_str = input("Digite a data no formato YYYY-MM-DD: ")

# Tentar converter a string para um objeto datetime
try:
    data = datetime.strptime(data_str, "%Y-%m-%d")
    print("Data inserida:", data)
except ValueError:
    print("Formato de data inválido. Certifique-se de usar o formato YYYY-MM-DD.")

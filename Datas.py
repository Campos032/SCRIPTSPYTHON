# Iremos usar a Biblioteca datetime, mais precisamente a classe datetime dentro da biblioteca datetime

from datetime import datetime, timedelta
import zoneinfo

# Datas

datahoje = datetime.now()  # Now data atual na máquina

# datahoje se tornará um obj que poderemos extrair apenas mês, hora e etc, como, por exemplo (datahoje.day -
# datahoje.month - datahoje.hour e etc)

# Para fazer a soma de datas ou manipulá-las usaremos a função timedelta

# Variação de datas
amanha = datahoje + timedelta(days=1)  # Irá somar 1 dia
semana = datahoje + timedelta(weeks=1)  # Irá somar 1 semana

# print(f'{amanha.date()} \n{semana.date()}')

# Criar data / Manipular

datacontrato = datetime(year=2023, month=5, day=12, )

# print(datacontrato.date())

diferença = datahoje - datacontrato

# print(diferença.days,'DIAS')

# Datas em outros formatos

dataformatobrasil = "23/12/2023"

dataformatoUSA = datetime.strptime(dataformatobrasil, "%d/%m/%Y")

# print(dataformatoUSA.date())
# print(dataformatobrasil)


# print(datahoje.strftime("%d-%m-%Y"))# Mudando o formato para padrão brasileiro
# print(datahoje.strftime("%A"))# O nome do dia da semana

# Fuso Horário
# usar o timedelta para ajustar ou usar a biblioteca zoneinfo que irá demonstrar os fusos e ajustar automaticamente

# print(zoneinfo.available_timezones())# Demonstra todas os fusos, UTC(Universal Time Coordinates),GMT(Greenwich Mean
# Time Zone)

belizetime = zoneinfo.ZoneInfo('America/Belize')
belizenow = datahoje.astimezone(belizetime)

# print(belizenow)

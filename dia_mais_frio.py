import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("./data/IOT-temp.csv")

# Converter a coluna de data para o formato correto
df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")

# Criar uma nova coluna apenas com a data (sem horário)
df["date"] = df["noted_date"].dt.date

# Agrupar por dia e pegar a maior e menor temperatura registrada em cada dia
daily_max_temps = df.groupby("date")["temp"].max()
daily_min_temps = df.groupby("date")["temp"].min()

# Encontrar o dia com a temperatura mais alta
day_hottest = daily_max_temps.idxmax()
max_temp = daily_max_temps.max()

# Encontrar o dia com a temperatura mais baixa
day_coldest = daily_min_temps.idxmin()
min_temp = daily_min_temps.min()

print(f"O dia mais quente foi {day_hottest} com {max_temp}°C.")
print(f"O dia mais frio foi {day_coldest} com {min_temp}°C.")

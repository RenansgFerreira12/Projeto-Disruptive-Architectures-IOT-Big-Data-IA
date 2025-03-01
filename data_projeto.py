import pandas as pd
try:


 df = pd.read_csv('data/IOT-temp.csv') # Importando o datase
except FilenotFoundError:
 print ("Arquivo nao foi encvontrado =(. ")
# finally:
    # print("Arquivo encontrado com sucesso! =)")

df.head () # Mostrando as 5 primeiras linhas do dataset 

df_bronze = df.copy() # Criando uma cópia do dataset original

# Usando o csv para criar  uam consulta de em python , qual dia foi o mais quente do ano ?  

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("./data/IOT-temp.csv")

# Converter a coluna de data para o formato correto
df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")

# Criar uma nova coluna apenas com a data (sem horário)
df["date"] = df["noted_date"].dt.date

# Agrupar por dia e pegar a maior temperatura registrada em cada dia
daily_max_temps = df.groupby("date")["temp"].max()

# Encontrar o dia com a temperatura mais alta
day_hottest = daily_max_temps.idxmax()
max_temp = daily_max_temps.max()

print(f"O dia mais quente foi {day_hottest} com {max_temp}°C.")

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("./data/IOT-temp.csv")

# Converter a coluna de data para o formato correto
df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")

# Criar novas colunas com a data e o mês
df["date"] = df["noted_date"].dt.date
df["month"] = df["noted_date"].dt.month

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

# Identificar os 10 maiores períodos de seca (dias consecutivos sem chuva)
if "precipitation" in df.columns:
    df_rain = df.groupby("date")["precipitation"].sum()
    dry_days = (df_rain == 0).astype(int)
    dry_streaks = dry_days.groupby((dry_days != dry_days.shift()).cumsum()).cumsum()
    top_10_dry_periods = dry_streaks.max().nlargest(10)
    print("Os 10 maiores períodos de seca foram:")
    print(top_10_dry_periods)
else:
    print("Coluna de precipitação não encontrada no dataset.")

# Encontrar os meses mais quentes do ano
monthly_avg_temps = df.groupby("month")["temp"].mean()
hottest_months = monthly_avg_temps.nlargest(3)
print("Os 3 meses mais quentes do ano foram:")
print(hottest_months)

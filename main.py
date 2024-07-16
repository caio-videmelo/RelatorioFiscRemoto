import pandas as pd
# Criar DataFrame com os dados fornecidos
data = {
    "Subsedes": ["Alto-Tiete", "Assis", "Baixada", "Bauru", "Campinas", "Sorocaba", "Metropolitana", "Grande-ABC", "Ribeirao-Preto", "SJRP", "Vale"],
    "Numero-fisc-rem": [2, 6, 3, 1, 2, 4, 3, 5, 2, 3, 3],
    "Eco-tempo": ["5 horas e 40 minutos", "35 horas e 10 minutos", "12 horas e 30 minutos", "1 hora e 30 minutos", "3 horas e 20 minutos", "19 horas", "7 horas", "5 horas e 10 minutos", "8 horas e 20 minutos", "3 horas e 20 minutos", "5 horas e 10 minutos"],
    "Eco-fin": ["$ 747.64", "$ 11,482.34", "$ 2,948.00", "$ 711.92", "$ 1,294.00", "$ 5,989.92", "$ 473.36", "$ 324.46", "$ 3,106.11", "$ 950.48", "$ 1,315.00"]
}
df = pd.DataFrame(data)
# Função para converter "Eco-tempo" para minutos
def convert_to_minutes(time_str):
    parts = time_str.split()
    hours = int(parts[0])
    minutes = int(parts[3]) if len(parts) > 3 else 0
    return hours * 60 + minutes
# Converter "Eco-fin" para numérico
df["Eco-fin"] = df["Eco-fin"].replace('[\$,]', '', regex=True).astype(float)
# Aplicar a função de conversão de tempo
df["Eco-tempo-minutos"] = df["Eco-tempo"].apply(convert_to_minutes)
# Realizar a análise descritiva
descriptive_stats = df.describe()
df, descriptive_stats
print(df)
print(descriptive_stats)

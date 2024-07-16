pip install matplotlib

import matplotlib.pyplot as plt

# Dados
subsedes = ["Alto-Tiete", "Assis", "Baixada", "Bauru", "Campinas", "Sorocaba", "Metropolitana", "Grande-ABC", "Ribeirao-Preto", "SJRP", "Vale"]
numero_fisc_rem = [2, 6, 3, 1, 2, 4, 3, 5, 2, 3, 3]
eco_tempo_minutos = [340, 2110, 750, 90, 200, 1140, 420, 310, 500, 200, 310]
eco_fin = [747.64, 11482.34, 2948.00, 711.92, 1294.00, 5989.92, 473.36, 324.46, 3106.11, 950.48, 1315.00]

# Gráfico 1: Número de Fiscalizações Remotas
plt.figure(figsize=(10, 5))
plt.bar(subsedes, numero_fisc_rem, color='blue')
plt.xlabel('Subsedes')
plt.ylabel('Número de Fiscalizações Remotas')
plt.title('Número de Fiscalizações Remotas por Subsede')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2: Economia de Tempo em Minutos
plt.figure(figsize=(10, 5))
plt.bar(subsedes, eco_tempo_minutos, color='green')
plt.xlabel('Subsedes')
plt.ylabel('Economia de Tempo (minutos)')
plt.title('Economia de Tempo em Minutos por Subsede')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 3: Economia Financeira (R$)
plt.figure(figsize=(10, 5))
plt.bar(subsedes, eco_fin, color='red')
plt.xlabel('Subsedes')
plt.ylabel('Economia Financeira (R$)')
plt.title('Economia Financeira por Subsede')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

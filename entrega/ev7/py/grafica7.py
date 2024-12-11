#Grafica de calor 7

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ruta = r"C:\Users\lortizp\Documents\INVESTIGACION ARIEL\csv\Grafica7.csv"
df = pd.read_csv(ruta)

for column in df.columns[1:]:
    df[column] = df[column].str.replace('%', '').astype(float)

df.set_index('Framework', inplace=True)

plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', cbar=True, fmt=".1f", linewidths=.5)

plt.title('Gráfica de Calor: Opiniones sobre Frameworks', fontsize=16)
plt.xlabel('Opiniones', fontsize=14)
plt.ylabel('Frameworks', fontsize=14)

plt.tight_layout()
plt.show()
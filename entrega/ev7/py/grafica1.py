#Grafica 1

import pandas as pd
import matplotlib.pyplot as plt

ruta = r"C:\Users\lortizp\Documents\INVESTIGACION ARIEL\csv\Grafica1.csv"
df = pd.read_csv(ruta)

print(df.head())

df_melted = df.melt(id_vars='Aplicaciones móviles y de escritorio',
                     var_name='Categoría',
                     value_name='Porcentaje')

df_melted.rename(columns={'Aplicaciones móviles y de escritorio': 'Herramienta'}, inplace=True)

plt.figure(figsize=(12, 6))

for category in df_melted['Categoría'].unique():
    subset = df_melted[df_melted['Categoría'] == category]
    plt.plot(subset['Herramienta'], subset['Porcentaje'], marker='o', label=category)

plt.xticks(rotation=45, ha='right')
plt.title('Porcentaje de Uso de Herramientas de Desarrollo')
plt.xlabel('Herramienta')
plt.ylabel('Porcentaje (%)')
plt.ylim(-5, 40)
plt.legend(title='Categoría')
plt.grid()
plt.tight_layout()

plt.show()
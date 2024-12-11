#Grafica 8 Dispersion

import pandas as pd
import matplotlib.pyplot as plt


ruta = r"C:\Users\lortizp\Documents\INVESTIGACION ARIEL\csv\Grafica8.csv"
df = pd.read_csv(ruta)

for column in ['Lo usaría de nuevo', 'Me interesa']:
    df[column] = df[column].str.replace('%', '').astype(float)

plt.figure(figsize=(12, 8))
plt.scatter(df['Lo usaría de nuevo'], df['Me interesa'], color='blue', alpha=0.6, s=100)

plt.title('Gráfica de Dispersión: Lo usaría de nuevo vs Me interesa', fontsize=16)
plt.xlabel('Lo usaría de nuevo (%)', fontsize=14)
plt.ylabel('Me interesa (%)', fontsize=14)

for i in range(len(df)):
    plt.annotate(df['Framework'][i],
                 (df['Lo usaría de nuevo'][i] + 0.5, df['Me interesa'][i] + 0.5),
                 fontsize=9, ha='right')

plt.grid()
plt.tight_layout()
plt.show()
#Grafica Lineas 8 

import pandas as pd
import matplotlib.pyplot as plt

ruta = r"C:\Users\lortizp\Documents\INVESTIGACION ARIEL\csv\Grafica8.csv"
df = pd.read_csv(ruta)

print(df.head())

plt.figure(figsize=(12, 6))
for column in df.columns[1:]:
    plt.plot(df['Framework'], df[column], marker='o', label=column)

# Personalizar la gráfica
plt.title('Gráfica de Líneas de Frameworks')
plt.xlabel('Frameworks')
plt.ylabel('Porcentaje')
plt.xticks(rotation=45)
plt.legend(title='Valores')
plt.grid()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
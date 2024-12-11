#Grafica 3

import pandas as pd
import matplotlib.pyplot as plt

ruta = r"C:\Users\lortizp\Documents\INVESTIGACION ARIEL\csv\Grafica3.csv"
df = pd.read_csv(ruta)

print(df.head())

plt.figure(figsize=(12, 6))
plt.plot(df['Lenguaje Programacion'], df['Popularidad'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title('Popularidad de Lenguajes de Programación')
plt.xlabel('Lenguaje de Programación')
plt.ylabel('Popularidad')
plt.grid()
plt.tight_layout()
plt.show()
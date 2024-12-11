import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
ruta = r"C:\Users\lortizp\Documents\INVESTIGACION ARIEL\csv\Grafica4.csv"
df = pd.read_csv(ruta)

# Limpieza y transformación de datos
df['Uso'] = df['Uso'].str.replace('%', '').astype(float)

df['Popularidad del lenguaje en el último año'] = df['Popularidad del lenguaje en el último año'].astype(str)
cambios = df['Popularidad del lenguaje en el último año'].str.extract(r'(\+\d+\.\d+)|(\-\d+\.\d+)')[0]
df['Cambio'] = cambios.astype(float)

# Crear gráfica
plt.figure(figsize=(12, 6))
plt.bar(df['Lenguaje'], df['Uso'], color='blue', alpha=0.7)

# Títulos y etiquetas
plt.title('Gráfica de Barras: Uso de Lenguajes de Programación')
plt.xlabel('Lenguaje de Programación')
plt.ylabel('Uso (%)')

# Agregar valores encima de las barras
for i in range(len(df)):
    plt.text(i, df['Uso'][i] + 0.5, f"{df['Uso'][i]}%", ha='center', fontsize=8)

# Estilo de los ejes
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()

# Mostrar gráfica
plt.show()
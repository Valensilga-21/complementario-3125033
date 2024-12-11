#Grafica 10

import matplotlib.pyplot as plt
import numpy as np

# Datos
herramientas = [
    "webpack", "Parcel", "Gulp", "Rollup", "Browserify", "tsc CLI",
    "Rome", "Snowpack", "SWC", "esbuild", "Vite", "WMR"
]
anios = ["2016", "2017", "2020", "2021"]
data_retencion = [
    [1, 1, 4, 7],
    [None, None, 5, 6],
    [2, 3, 9, 12],
    [None, 2, 6, 5],
    [3, 4, 10, 11],
    [None, None, 3, 4],
    [None, None, 8, 10],
    [None, None, 2, 9],
    [None, None, 7, 3],
    [None, None, 1, 2],
    [None, None, None, 1],
    [None, None, None, 8]
]

x = np.arange(len(herramientas))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

for i, anio in enumerate(anios):
    valores = [row[i] if i < len(row) and row[i] is not None else 0 for row in data_retencion]
    ax.bar(x + i * bar_width, valores, bar_width, label=anio)

# Etiquetas y título
ax.set_xlabel("Herramientas")
ax.set_ylabel("Rango de Retención")
ax.set_title("Comparación de Rango de Retención por Año")
ax.set_xticks(x + bar_width * (len(anios) - 1) / 2)
ax.set_xticklabels(herramientas, rotation=45, ha="right")
ax.legend(title="Año")

# Mostrar el gráfico
plt.tight_layout()
plt.show()
#Grafica 6

import pandas as pd
import matplotlib.pyplot as plt

# Datos
data = {
    'Year': [2016, 2017, 2018, 2019, 2020, 2021],
    'React': [1, 1, 2, 1, 2, 3],
    'Vue.js': [2, 2, 1, 3, 3, 4],
    'Angular': [3, 3, 5, 5, 8, 9],
    'Preact': [None, 3, 4, 5, 7, None],
    'Ember': [4, 4, 4, 6, 9, 10],
    'Svelte': [None, None, 2, 1, 2, None],
    'Alpine.js': [None, None, 4, 5, None, None],
    'Lit': [None, None, 6, 6, None, None],
    'Stimulus': [None, None, 7, 8, None, None],
    'Solid': [None, None, 1, None, 2, None]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

plt.figure(figsize=(12, 6))
for framework in df.columns:
    plt.plot(df.index, df[framework], marker='o', label=framework)

plt.title('Rango de Retención de Frameworks (2016-2021)')
plt.xlabel('Año')
plt.ylabel('Rango')
plt.xticks(df.index)
plt.legend(title='Frameworks')
plt.grid()
plt.show()
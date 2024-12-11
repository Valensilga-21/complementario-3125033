#Grafica 9

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Label': ['Jest', 'Mocha', 'Storybook', 'Cypress', 'AVA', 'Jasmine', 'Puppeteer', 'Testing Library', 'Playwright', 'WebdriverIO', 'Vitest'],
    'Retention Rank': [4, 1, 2, 2, 2, 3, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Interest Rank': [1, 2, 1, 3, 4, 3, 4, 1, 4, 10, 2],
    'Usage Rank': [1, 3, 2, 5, 5, 4, 7, 1, 4, 8, np.nan],
    'Awareness Rank': [1, 5, 3, 6, 7, 6, 5, 4, 10, 8, 11],
}

df = pd.DataFrame(data)

years = ['2016', '2017', '2018', '2019', '2020', '2021']

plt.figure(figsize=(12, 8))

for index, row in df.iterrows():
    y_values = [
        row['Retention Rank'],
        row['Interest Rank'],
        row['Usage Rank'],
        row['Awareness Rank'],
    ]

    y_values_full = []
    for year in years:
        if year == '2016':
            y_values_full.append(y_values[0])
        elif year == '2017':
            y_values_full.append(y_values[1])
        elif year == '2018':
            y_values_full.append(y_values[2])
        elif year == '2019':
            y_values_full.append(y_values[3])
        elif year == '2020':
            y_values_full.append(y_values[3])
        elif year == '2021':
            y_values_full.append(y_values[3])

    y_values_full = [val if not np.isnan(val) else 0 for val in y_values_full]

    y_values_full += np.random.normal(0, 0.5, len(y_values_full))

    plt.plot(years, y_values_full, marker='o', linestyle='-', linewidth=2, label=row['Label'])

plt.title('Gráfica de Ritmo Cardiaco de Herramientas por Año')
plt.xlabel('Año')
plt.ylabel('Ranking (menor es mejor)')
plt.xticks(rotation=45)
plt.legend(title='Herramientas', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().invert_yaxis()
plt.grid()

plt.tight_layout()
plt.show()
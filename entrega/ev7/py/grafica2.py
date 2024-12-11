#Grafica 2

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Monorepos': [
        'Rush', 'Turborepo', 'Yarn Workspaces', 'Yalc',
        'Lerna', 'npm Workspaces', 'pnpm', 'Nx'
    ],
    'Rango de retención': [8, 2, 5, 6, 7, 4, 1, 3],
    'Rango de interés': [6, 1, 5, 8, 7, 4, 3, 2],
    'Rango de Uso': [8, 6, 2, 7, 1, 3, 4, 5],
    'Conciencia Rango': [7, 6, 1, 8, 3, 2, 4, 5]
}

df = pd.DataFrame(data)

df.set_index('Monorepos', inplace=True)

plt.figure(figsize=(12, 6))

for column in df.columns:
    plt.plot(df.index, df[column], marker='o', label=column)

plt.title('Rangos de Monorepos en 2021')
plt.xlabel('Monorepos')
plt.ylabel('Rango (menor es mejor)')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Rango')
plt.gca().invert_yaxis()
plt.grid()

plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Frameworks': ['Express', 'Next.js', 'Nuxt', 'Gatsby', 'Nest', 'Strapi', 'Fastify', 'Redwood', 'Astro', 'Eleventy', 'Blitz', 'Remix', 'SvelteKit'],
    'Rango de retención 2017': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Rango de retención 2018': [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Rango de retención 2019': [1, 2, 4, 3, 5, 6, 3, 0, 2, 8, 11, 5, 1],
    'Rango de retención 2020': [2, 1, 9, 7, 7, 10, 5, 12, 3, 10, 12, 2, 1],
    'Rango de retención 2021': [6, 4, 0, 13, 5, 8, 7, 13, 11, 9, 12, 6, 7],
    'Rango de interés 2017': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Rango de interés 2018': [2, 1, 7, 4, 5, 6, 3, 0, 0, 0, 0, 0, 0],
    'Rango de interés 2019': [3, 1, 9, 13, 7, 8, 7, 12, 0, 0, 0, 0, 0],
    'Rango de interés 2020': [2, 4, 4, 3, 5, 6, 5, 0, 3, 10, 12, 10, 1],
    'Rango de interés 2021': [6, 0, 4, 3, 5, 6, 7, 13, 11, 10, 12, 6, 7],
}

df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(12, 8))

for year in ['2017', '2018', '2019', '2020', '2021']:
    plt.scatter(df[f'Rango de retención {year}'], df[f'Rango de interés {year}'], label=year, alpha=0.5)

plt.title('Gráfica de Dispersión: Rango de Retención vs Rango de Interés')
plt.xlabel('Rango de Retención')
plt.ylabel('Rango de Interés')
plt.legend()
plt.grid()
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.show()
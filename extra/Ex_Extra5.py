import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

# region = ds[:, :2]
# gdp = ds[1:, 8]
# print(region)
# print(gdp)

content = ds[1:, [0, 1, 8]]
print(content)

america = content[np.where(content[:, 1] == 'LATIN AMER. & CARIB    ')]
print(america)

maxGdp = america[1:, 2].astype(float)
maxGdp = maxGdp.max()
print(maxGdp)

country = america[np.where(content[:, 2] == 35000.0)]
print(country)
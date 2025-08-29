import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

allRegion = ds[:,1]
region = np.unique(allRegion) #valores unicos, sem repetir
print(region)

qtdRegion = len(region)
print(qtdRegion)
import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

literacy = ds[1:, 9] #pegando a partir da primeira linha para pegar só valores e não cabeçalho
print(literacy)

literacy = literacy.astype(float)
print(literacy.mean())


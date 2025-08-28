import numpy as np

ds = np.loadtxt('../space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

empresa = ds[1:, 2]

empresas, contagens = np.unique(empresa, return_counts=True)

resultado = np.column_stack((empresas, contagens))
print(resultado)

import numpy as np

ds = np.loadtxt('../space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')
local = ds[1:, 2]

qtdUSA = np.sum(np.char.find(local, "USA") >= 0)
print(qtdUSA)


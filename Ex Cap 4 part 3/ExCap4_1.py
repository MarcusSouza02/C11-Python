import numpy as np

ds = np.loadtxt('../space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

status = ds[1:, 7]
sucessos = np.sum(status == "Success")
qtdStatus = len(status)
total = ((sucessos/qtdStatus) * 100)
print(total)
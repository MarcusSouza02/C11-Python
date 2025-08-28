import numpy as np

ds = np.loadtxt('../space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

ds_cost = ds[1:, 6]

ds_cost = ds_cost.astype(float)

print(ds_cost[ds_cost > 0].mean())
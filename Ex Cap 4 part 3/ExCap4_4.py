import numpy as np

ds = np.loadtxt('../space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

ds_cost = ds[1:, 6]

mask_spacex = ds_cost == "SpaceX"
print(cost[mask_spacex].max())
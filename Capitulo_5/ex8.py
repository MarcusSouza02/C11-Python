import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(
    index=['A','B','C','D','E'],
    columns=['W','X','Y','Z'],
    data=np.random.randint(1, 50, [5, 4])
)

results = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print('Slicing:', results)

print('Linha A: ', results.loc['A'].sum())
print('Linha C: ', results.loc['C'].sum())
print('Linha E: ', results.loc['E'].sum())

print('Coluna X: ', results['X'].sum())
print('Coluna Y: ', results['Y'].sum())
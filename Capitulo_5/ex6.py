import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(
    index=['A','B','C','D','E'],
    columns = ['W','X','Y','Z'],
    data = np.random.randint(1, 50, [5, 4])
    )

print(df['X'][df['X'] < 30].mean())

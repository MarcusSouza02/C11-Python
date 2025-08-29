import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

print(ds[:,:4]) #dois pontos pega todas as linhas , pegando somente as quatro primeiras colunas excluise a 4
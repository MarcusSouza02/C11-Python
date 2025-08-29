import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

allRegion = ds[:, 1] #somente a coluna region

northAmerica = allRegion[np.char.find(allRegion, "NORTHERN AMERICA") >= 0] #usa a mascara de true para pegar só true
print(northAmerica)

qtdAmerica = len(northAmerica)#quantidade de true
print(qtdAmerica)

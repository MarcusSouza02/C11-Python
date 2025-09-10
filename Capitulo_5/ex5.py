import pandas as pd

dc = {'Java' : 16.25, 'C' : 16.04, 'Python' : 9.85}
dc1 = {'C' : 16.21, 'Python' : 12.12, 'Java' : 11.68}

series = pd.Series(dc)
series1 = pd.Series(dc1)
aumento = series1 - series

results = series1 + (2*aumento)
popular = results.nlargest(1)

print('O 4 ano: ', results)
print('A linguagem mais popular: ', popular)
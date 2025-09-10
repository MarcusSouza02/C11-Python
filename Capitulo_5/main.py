import pandas as pd

#criando novo series
#quando for criar uma series é necessário passar um indice e depois o valor
# indices = ['a', 'b', 'c'] #indices
# valores = [10, 20, 30]  #dados
#
# #criamos duas listas para criar uma series
# series = pd.Series(index=indices, data = valores) #index são as indices e data os valores dessas colunas
# print(series)
# print(type(series)) # usando o type para ver se a "ide" entendeu como series
# print(series[['a', 'c']]) #pegando as indices a e c e seus valores
# print(series[1:]) #slicing pra pegar da linha 1 pra frente, tira a linha zero

# dic = {'a': 10, 'b': 20, 'c': 30} # outra forma de criar uma series
# series2 = pd.Series(dic) #criando como dicionarios
# print(series2)
# print(type(series2))
# print(series['a']) # quando eu quero ver um valor dentro da "chave"(indice) a


#Condicionais
# dic = {'a': 10,'b': 20,'c': 30}
# dic2 = {'a': 10,'b': 20,'d': 40}
#
# series = pd.Series(dic)
# series2 = pd.Series(dic2)
#
# print(series <= 20) #dessa forma ele so mostra a mascara de ture e false
# print(series[series <= 20]) # dessa forma ele mostra apenas os elementos que atendem a condicao
#
# print(series[series> series.mean()]) #valores que estão acima da média


#DataFrames
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A','B','C','D','E'],
    columns = ['W','X','Y','Z'],
    data = np.random.randint(1, 50, [5, 4])
    ) # criando um dataframe, index representa as linhas, columns as colunas e data sao os elementos dentro delas
print(df)

# FAZENDO SLICINGS COM iloc (padrão Numpy - indices numéricos)
print(df.iloc[0:2, :]) # iloc continua usando os numeros como numpy

# FAZENDO SLICING COM LOC
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']]) # usando slicing como indices costumizaveis(colocados no dataframa)
print(df.loc[['A', 'B'], ['W', 'Y']]) # é possivel pegar colunas distantes apenas escolhendo pelos indices
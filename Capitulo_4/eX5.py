import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 50, 16).reshape(4, 4)

print(matriz)

media_linhas = matriz.mean(axis=1)
media_colunas = matriz.mean(axis=0)
print("\nMédias das linhas:", media_linhas)
print("Médias das colunas:", media_colunas)

maior_media_linhas = media_linhas.max()
print("\nMaior média das linhas:", maior_media_linhas)

maior_media_colunas = media_colunas.max()
print("\nMaior média das colunas:", maior_media_colunas)

valores, contagens = np.unique(matriz, return_counts=True)
print("\nContagem de cada número na matriz:")
for valor, cont in zip(valores, contagens):
    print(f"{valor} aparece {cont} vez(es)")

numeros_2x = valores[contagens == 2]
print("\nNúmeros que aparecem duas vezes:", numeros_2x)


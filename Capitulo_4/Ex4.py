import numpy as np

matriz = np.random.randint(0, 30, 12).reshape(4,3)

linhas, colunas = matriz.shape
print(f"A matriz tem {linhas} linhas e {colunas} colunas.")

total_elementos = linhas * colunas
print(f"Número total de elementos: {total_elementos}")

if total_elementos % 2 == 0:
    print("O vetor unidimensional teria um número par de elementos.")
else:
    print("O vetor unidimensional teria um número ímpar de elementos.")

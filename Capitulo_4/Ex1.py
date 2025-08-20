import numpy as np

array_ones = np.ones(8, dtype=int)
array_random = np.random.randint(0, 10, 8)

array_result = array_ones + array_random

print("Array de 1:", array_ones)
print("Array aleatório:", array_random)
print("Array resultante:", array_result)


soma = np.sum(array_result)
print("\nSoma dos arrays:", soma)
if soma >= 40:
    novo_array = array_result.reshape(4, 2)
    print("\nMatriz com mais linhas do que colunas (4x2):")
else:
    novo_array = array_result.reshape(2, 4)
    print("\nMatriz com mais colunas do que linhas (2x4):")

print(novo_array)

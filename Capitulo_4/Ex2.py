import numpy as np

array1 = np.arange(0, 52, 2)

array2 = np.arange(100, 49, -2)

array_concat = np.concatenate((array1, array2))

array_sorted = np.sort(array_concat)

print(array1)
print(array2)
print("\nArray concatenado:", array_concat)
print("\nArray ordenado:", array_sorted)

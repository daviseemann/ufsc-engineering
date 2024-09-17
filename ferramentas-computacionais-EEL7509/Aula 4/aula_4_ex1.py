import numpy as np

# Criação do ndarray de 2 dimensões com valores de 1 a 16, coluna a coluna
matriz = np.arange([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16])

# Imprimindo shape, ndim, dtype, size e itemsize do array
print("Shape:", matriz.shape)
print("Ndim:", matriz.ndim)
print("Dtype:", matriz.dtype)
print("Size:", matriz.size)
print("Itemsize:", matriz.itemsize)

# Extraindo e imprimindo as duas primeiras linhas e colunas
print("Duas primeiras linhas e colunas:\n", matriz[:2, :2])

# Extraindo e imprimindo as duas últimas linhas e colunas
print("Duas últimas linhas e colunas:\n", matriz[2:, 2:])

# Extraindo e imprimindo a segunda e terceira linhas
print("Segunda e terceira linhas:\n", matriz[1:3, :])

# Extraindo e imprimindo a segunda coluna
print("Segunda coluna:\n", matriz[:, 1])

# Convertendo o array para float32 e imprimindo dtype, size e itemsize
matriz_float32 = matriz.astype(np.float32)
print("Dtype após conversão:", matriz_float32.dtype)
print("Size após conversão:", matriz_float32.size)
print("Itemsize após conversão:", matriz_float32.itemsize)

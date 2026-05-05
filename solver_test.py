import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

# Parametry
N = 500            # rozmiar macierzy
density = 0.01     # % niezerowych elementów

# Generowanie macierzy rzadkiej
A = sparse_random(N, N, density=density, format='csr', dtype=np.float64)

# Dodanie silnej diagonalnej - ważne dla stabilności
A = A + 10 * csr_matrix(np.eye(N))

# Generowanie x_true 
x_true = np.random.rand(N)

# Obliczanie b = A * x_true
b = A.dot(x_true)

# Rozwiązanie A * x = b 
x = spsolve(A, b)

# Weryfikacja
error = np.linalg.norm(x - x_true)

print("Błąd:", error)

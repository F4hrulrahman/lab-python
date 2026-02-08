"""
Chapter 5 - Bagian 1: NumPy Dasar
====================================
NumPy (Numerical Python) adalah library fundamental untuk komputasi
numerik. Menyediakan array multidimensi yang efisien dan cepat.

Install: pip install numpy
"""

import numpy as np

# ============================================
# 1. Membuat Array
# ============================================
print("=== Membuat Array ===")

# Dari list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr1}")
print(f"  dtype: {arr1.dtype}, shape: {arr1.shape}")

# 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{arr2d}")
print(f"  shape: {arr2d.shape}, ndim: {arr2d.ndim}")

# Array generator
print(f"\nnp.zeros(5)      = {np.zeros(5)}")
print(f"np.ones(5)       = {np.ones(5)}")
print(f"np.full(5, 7)    = {np.full(5, 7)}")
print(f"np.arange(0,10,2)= {np.arange(0, 10, 2)}")
print(f"np.linspace(0,1,5)= {np.linspace(0, 1, 5)}")
print(f"np.eye(3):\n{np.eye(3)}")

# Random array
np.random.seed(42)  # Reproducible
print(f"\nRandom integers (0-9): {np.random.randint(0, 10, size=5)}")
print(f"Random floats:         {np.random.rand(5).round(3)}")
print(f"Normal distribution:   {np.random.randn(5).round(3)}")

# ============================================
# 2. Indexing dan Slicing
# ============================================
print("\n=== Indexing dan Slicing ===")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(f"arr      = {arr}")
print(f"arr[0]   = {arr[0]}")
print(f"arr[-1]  = {arr[-1]}")
print(f"arr[2:5] = {arr[2:5]}")
print(f"arr[::2] = {arr[::2]}")

# 2D indexing
print(f"\narr2d:\n{arr2d}")
print(f"arr2d[0, 0] = {arr2d[0, 0]}")
print(f"arr2d[1, 2] = {arr2d[1, 2]}")
print(f"arr2d[0]    = {arr2d[0]}")  # Baris pertama
print(f"arr2d[:, 0] = {arr2d[:, 0]}")  # Kolom pertama
print(f"arr2d[0:2, 1:] =\n{arr2d[0:2, 1:]}")

# Boolean indexing
print(f"\narr > 50:          {arr > 50}")
print(f"arr[arr > 50]:     {arr[arr > 50]}")

# ============================================
# 3. Operasi Aritmatika
# ============================================
print("\n=== Operasi Aritmatika ===")
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b  = {a + b}")
print(f"a * b  = {a * b}")  # Element-wise multiplication
print(f"a ** 2 = {a**2}")
print(f"b / a  = {b / a}")

# Operasi dengan skalar (broadcasting)
print(f"\na * 10     = {a * 10}")
print(f"a + 100    = {a + 100}")

# Fungsi universal (ufunc)
print(f"\nnp.sqrt(a)  = {np.sqrt(a).round(3)}")
print(f"np.exp(a)   = {np.exp(a).round(3)}")
print(f"np.log(a)   = {np.log(a).round(3)}")
print(f"np.sin(a)   = {np.sin(a).round(3)}")

# ============================================
# 4. Fungsi Statistik
# ============================================
print("\n=== Fungsi Statistik ===")
data = np.array([23, 45, 67, 12, 89, 34, 56, 78, 90, 11])

print(f"data   = {data}")
print(f"mean   = {np.mean(data):.2f}")
print(f"median = {np.median(data):.2f}")
print(f"std    = {np.std(data):.2f}")
print(f"var    = {np.var(data):.2f}")
print(f"min    = {np.min(data)}")
print(f"max    = {np.max(data)}")
print(f"sum    = {np.sum(data)}")
print(f"argmin = {np.argmin(data)} (index dari nilai terkecil)")
print(f"argmax = {np.argmax(data)} (index dari nilai terbesar)")

# Statistik per axis (baris/kolom)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatrix:\n{matrix}")
print(f"Mean per kolom (axis=0): {np.mean(matrix, axis=0)}")
print(f"Mean per baris (axis=1): {np.mean(matrix, axis=1)}")
print(f"Sum total:               {np.sum(matrix)}")

# ============================================
# 5. Reshaping
# ============================================
print("\n=== Reshaping ===")
arr = np.arange(1, 13)
print(f"Original (12 elemen): {arr}")

reshaped = arr.reshape(3, 4)
print(f"Reshape (3x4):\n{reshaped}")

reshaped2 = arr.reshape(2, 6)
print(f"Reshape (2x6):\n{reshaped2}")

# Flatten
flat = reshaped.flatten()
print(f"Flatten:  {flat}")

# Transpose
print(f"\nTranspose (3x4 -> 4x3):\n{reshaped.T}")

# ============================================
# 6. Operasi Matriks
# ============================================
print("\n=== Operasi Matriks ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A:\n{A}")
print(f"B:\n{B}")

# Perkalian matriks (dot product)
print(f"\nA @ B (dot product):\n{A @ B}")
print(f"np.dot(A, B):\n{np.dot(A, B)}")

# Element-wise multiplication (bukan dot product)
print(f"\nA * B (element-wise):\n{A * B}")

# Determinant dan Inverse
print(f"\nDeterminant A: {np.linalg.det(A):.2f}")
print(f"Inverse A:\n{np.linalg.inv(A)}")

# ============================================
# 7. Contoh Praktis: Normalisasi Data
# ============================================
print("\n=== Contoh: Normalisasi Data ===")
np.random.seed(42)
data = np.random.randint(0, 100, size=10)
print(f"Data asli: {data}")

# Min-Max Normalization (0-1)
data_norm = (data - data.min()) / (data.max() - data.min())
print(f"Min-Max:   {data_norm.round(3)}")

# Z-Score Normalization
data_zscore = (data - data.mean()) / data.std()
print(f"Z-Score:   {data_zscore.round(3)}")

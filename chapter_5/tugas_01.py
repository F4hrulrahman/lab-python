"""
==========================================================
 TUGAS 1 - Analisis Statistik dengan NumPy
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat array 30 nilai mahasiswa (acak 40-100, seed=42)
 2. Hitung statistik dasar: mean, median, std, max/min
 3. Temukan indeks nilai tertinggi dan terendah (argmax/argmin)
 4. Hitung jumlah mahasiswa yang lulus (nilai >= 70)
 5. Lakukan normalisasi Min-Max (skala 0-1)
 6. Lakukan normalisasi Z-Score
 7. Reshape array menjadi 6x5, hitung rata-rata per baris & kolom
 8. Tampilkan semua hasil dalam format terstruktur

 Referensi:
 - Min-Max: (x - min) / (max - min)
 - Z-Score: (x - mean) / std
==========================================================
"""

import numpy as np

# Menentukan seed agar hasil angka acaknya selalu sama (sesuai instruksi)
np.random.seed(42)

# 1. Buat array NumPy berisi nilai ujian 30 mahasiswa
nilai = np.random.randint(40, 100, 30)

print("===== ANALISIS STATISTIK NILAI MAHASISWA =====")
print(f"Data (30 mahasiswa): {nilai}\n")

# 2. Statistik Deskriptif
mean = np.mean(nilai)
median = np.median(nilai)
std_dev = np.std(nilai)
max_val = np.max(nilai)
max_idx = np.argmax(nilai)
min_val = np.min(nilai)
min_idx = np.argmin(nilai)

# Hitung jumlah lulus (>= 70)
lulus_mask = nilai >= 70
jml_lulus = np.sum(lulus_mask)
persen_lulus = (jml_lulus / len(nilai)) * 100

print("--- Statistik Deskriptif ---")
print(f"Mean    : {mean:.2f}")
print(f"Median  : {median:.2f}")
print(f"Std Dev : {std_dev:.2f}")
print(f"Min     : {min_val} (index: {min_idx})")
print(f"Max     : {max_val} (index: {max_idx})")
print(f"Lulus   : {jml_lulus} dari {len(nilai)} ({persen_lulus:.1f}%)\n")

# 3. Normalisasi Min-Max (0-1)
# Rumus: (x - min) / (max - min)
norm_minmax = (nilai - min_val) / (max_val - min_val)

# 4. Normalisasi Z-Score
# Rumus: (x - mean) / std_dev
norm_zscore = (nilai - mean) / std_dev

print("--- Normalisasi ---")
print(f"Min-Max (5 pertama): {norm_minmax[:5]}")
print(f"Z-Score (5 pertama): {norm_zscore[:5]}\n")

# 5. Reshape menjadi array 2D (6 baris, 5 kolom)
data_kelas = nilai.reshape(6, 5)

print("--- Rata-rata per Kelas (reshape 6x5) ---")
# 6. Hitung rata-rata per baris (axis=1)
rata_per_kelas = np.mean(data_kelas, axis=1)
for i, r in enumerate(rata_per_kelas, 1):
    print(f"Kelas {i} : {r:.2f}")

# Hitung rata-rata per kolom (axis=0)
rata_per_matkul = np.mean(data_kelas, axis=0)
print("\n--- Rata-rata per Mata Ujian (Kolom) ---")
for i, r in enumerate(rata_per_matkul, 1):
    print(f"Ujian {i} : {r:.2f}")

"""
==========================================================
 TUGAS 3 - Handling Missing Data
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame dengan data yang sengaja memiliki NaN
    (minimal 3 kolom, 10-15 baris)
 2. Deteksi missing values: isnull().sum() per kolom
 3. Hitung persentase missing per kolom
 4. Buat 3 versi penanganan:
    - Versi 1: dropna() — hapus baris yang memiliki NaN
    - Versi 2: fillna() — isi numerik dengan mean,
               kategorikal dengan mode
    - Versi 3: fillna(method="ffill") — forward fill
 5. Bandingkan jumlah baris ketiga versi
 6. Berikan komentar kapan metode mana yang tepat digunakan

 Catatan:
 - Gunakan np.nan untuk membuat missing values
 - Buat data yang realistis (misal: data survei/kuesioner)
==========================================================
"""

import pandas as pd
import numpy as np

# Menentukan seed agar hasil tetap konsisten
np.random.seed(42)

# 1. Buat DataFrame dengan sengaja memiliki missing value (NaN)
data = {
    'Nama': ['Safriamsah', 'Budi', 'Citra', 'Dina', 'Eko', 'Fajri', 'Gita', 'Hadi', 'Indra', 'Joko', 'Kiki', 'Lulu'],
    'Usia': [22, 21, np.nan, 23, 22, np.nan, 24, 21, 22, np.nan, 23, 25],
    'IPK': [3.41, 3.2, 3.8, np.nan, 3.5, 3.0, np.nan, 3.9, 3.1, np.nan, 3.6, 2.9],
    'Jurusan': ['Informatika', 'Informatika', 'Sistem Informasi', np.nan, 'Teknik Elektro', 'Informatika', np.nan, 'Sistem Informasi', 'Informatika', 'Informatika', np.nan, 'Teknik Elektro']
}

df = pd.DataFrame(data)

print("===== DATAFRAME ASLI (DENGAN NaN) =====")
print(df)

# 2. Tampilkan jumlah NaN per kolom
print("\n--- Jumlah NaN per Kolom ---")
print(df.isnull().sum())

# 3. Tampilkan persentase data hilang
print("\n--- Persentase Data Hilang (%) ---")
print((df.isnull().sum() / len(df)) * 100)

# 4. PENANGANAN DATA HILANG

# Versi 1: dropna() -- Hapus baris yang memiliki NaN
df_v1 = df.dropna()

# Versi 2: fillna() dengan mean (numerik) dan modus (kategorikal)
df_v2 = df.copy()
df_v2['Usia'] = df_v2['Usia'].fillna(df_v2['Usia'].mean())
df_v2['IPK'] = df_v2['IPK'].fillna(df_v2['IPK'].mean())
# Modus mengembalikan Series, ambil indeks ke-0
df_v2['Jurusan'] = df_v2['Jurusan'].fillna(df_v2['Jurusan'].mode()[0])

# Versi 3: fillna() dengan method ffill (forward fill)
df_v3 = df.fillna(method='ffill')

# 5. Bandingkan jumlah baris
print("\n--- Perbandingan Jumlah Baris ---")
print(f"Data Asli : {len(df)}")
print(f"Versi 1 (dropna)  : {len(df_v1)}")
print(f"Versi 2 (fillna)  : {len(df_v2)}")
print(f"Versi 3 (ffill)   : {len(df_v3)}")

"""
PENJELASAN METODE:
1. dropna(): Gunakan jika jumlah baris yang hilang sangat sedikit (misal < 5%) 
   dan data yang tersisa masih cukup banyak untuk dianalisis.
2. fillna(mean/modus): Gunakan jika ingin mempertahankan jumlah data. 
   Mean cocok untuk data numerik yang distribusinya normal, 
   sedangkan modus untuk data kategori/string.
3. ffill: Gunakan untuk data yang memiliki urutan waktu (Time Series), 
   di mana nilai sekarang kemungkinan besar mirip dengan nilai sebelumnya.
"""

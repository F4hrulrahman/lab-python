"""
==========================================================
 TUGAS 2 - Analisis Data Mahasiswa dengan Pandas
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame 20 mahasiswa dengan kolom:
    Nama, NIM, Jurusan (3 pilihan), Semester (2-8),
    IPK (2.0-4.0), Jenis_Kelamin (L/P)
 2. Tampilkan info dasar: shape, dtypes, describe()
 3. Filter: mahasiswa IPK >= 3.5
 4. Filter: Jurusan "Informatika" DAN semester >= 5
 5. Sorting: urutkan berdasarkan IPK (descending), ambil top 5
 6. Groupby: statistik IPK per jurusan (mean, min, max, count)
 7. Groupby: jumlah mahasiswa per jenis_kelamin per jurusan
 8. Tambah kolom Predikat berdasarkan IPK
 9. Hitung distribusi predikat dengan value_counts()

 Predikat:
 | IPK >= 3.5 | Cum Laude          |
 | IPK >= 3.0 | Sangat Memuaskan   |
 | IPK >= 2.5 | Memuaskan          |
 | IPK <  2.5 | Cukup              |
==========================================================
"""

import pandas as pd
import numpy as np

# Menentukan seed agar hasil random konsisten
np.random.seed(42)

# 1. Buat DataFrame berisi data 20 mahasiswa
n = 20
jurusan_list = ['Informatika', 'Sistem Informasi', 'Teknik Elektro']

data = {
    'Nama': [f'Mahasiswa_{i}' for i in range(1, n+1)],
    'NIM': [f'10584110{i:02d}' for i in range(1, n+1)],
    'Jurusan': np.random.choice(jurusan_list, n),
    'Semester': np.random.randint(2, 9, n),
    'IPK': np.round(np.random.uniform(2.0, 4.0, n), 2),
    'Jenis_Kelamin': np.random.choice(['L', 'P'], n)
}

df = pd.DataFrame(data)

# Sisipkan nama Safriamsah ke dalam data agar sesuai identitas kamu
df.loc[0, 'Nama'] = 'FAHRUL RAHMAN'
df.loc[0, 'Jurusan'] = 'Informatika'
df.loc[0, 'IPK'] = 3.19 # Sesuai dengan IPK aslimu

print("===== DATA MAHASISWA =====")
print(df.head())

# 2. Tampilkan informasi dasar
print("\n--- Informasi Dasar ---")
print(f"Shape: {df.shape}")
print("\nData Types:")
print(df.dtypes)
print("\nStatistik Deskriptif:")
print(df.describe())

# 3. Filtering
print("\n--- Filtering: IPK >= 3.5 ---")
print(df[df['IPK'] >= 3.5])

print("\n--- Filtering: Informatika & Semester >= 5 ---")
filt = (df['Jurusan'] == 'Informatika') & (df['Semester'] >= 5)
print(df[filt])

# 4. Sorting: 5 Teratas berdasarkan IPK
print("\n--- Top 5 IPK Tertinggi ---")
print(df.sort_values(by='IPK', ascending=False).head(5))

# 5. Groupby: Statistik IPK per Jurusan
print("\n--- Statistik IPK per Jurusan ---")
stat_jurusan = df.groupby('Jurusan')['IPK'].agg(['mean', 'min', 'max', 'count'])
print(stat_jurusan)

# 6. Groupby: Jenis Kelamin per Jurusan
print("\n--- Jumlah Mahasiswa per Jenis Kelamin per Jurusan ---")
print(df.groupby(['Jurusan', 'Jenis_Kelamin']).size())

# 7. Tambahkan kolom baru Predikat
def tentukan_predikat(ipk):
    if ipk >= 3.5: return "Cum Laude"
    elif ipk >= 3.0: return "Sangat Memuaskan"
    elif ipk >= 2.5: return "Memuaskan"
    else: return "Cukup"

df['Predikat'] = df['IPK'].apply(tentukan_predikat)

# 8. Tampilkan distribusi predikat
print("\n--- Distribusi Predikat ---")
print(df['Predikat'].value_counts())

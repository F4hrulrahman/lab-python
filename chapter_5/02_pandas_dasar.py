"""
Chapter 5 - Bagian 2: Pandas Dasar
=====================================
Pandas adalah library untuk manipulasi dan analisis data tabular.
Struktur data utamanya: Series (1D) dan DataFrame (2D).

Install: pip install pandas
"""

import pandas as pd
import numpy as np

# ============================================
# 1. Series
# ============================================
print("=== Series ===")

# Membuat Series
nilai = pd.Series([85, 90, 78, 92, 88], name="Nilai")
print(f"Series:\n{nilai}\n")

# Series dengan custom index
nilai_mapel = pd.Series(
    [85, 90, 78, 92, 88],
    index=["MTK", "Fisika", "Kimia", "Bio", "Bahasa"],
    name="Nilai",
)
print(f"Dengan index custom:\n{nilai_mapel}\n")

# Akses data
print(f"nilai_mapel['MTK']     = {nilai_mapel['MTK']}")
print(f"nilai_mapel[0]         = {nilai_mapel.iloc[0]}")
print(f"nilai_mapel > 85:\n{nilai_mapel[nilai_mapel > 85]}\n")

# ============================================
# 2. DataFrame
# ============================================
print("=== DataFrame ===")

# Membuat DataFrame dari dictionary
data = {
    "Nama": ["Budi", "Ani", "Candra", "Dian", "Eka"],
    "Umur": [21, 22, 20, 23, 21],
    "Jurusan": [
        "Informatika",
        "Sistem Informasi",
        "Informatika",
        "Teknik Elektro",
        "Informatika",
    ],
    "IPK": [3.75, 3.90, 3.50, 3.85, 3.65],
    "Aktif": [True, True, False, True, True],
}

df = pd.DataFrame(data)
print(f"DataFrame:\n{df}\n")

# Informasi DataFrame
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Dtypes:\n{df.dtypes}\n")

# ============================================
# 3. Melihat Data
# ============================================
print("=== Melihat Data ===")
print(f"Head (3 baris pertama):\n{df.head(3)}\n")
print(f"Tail (2 baris terakhir):\n{df.tail(2)}\n")
print(f"Describe (statistik):\n{df.describe()}\n")
print(f"Info:")
df.info()
print()

# ============================================
# 4. Seleksi Data
# ============================================
print("=== Seleksi Data ===")

# Seleksi kolom
print(f"Kolom 'Nama':\n{df['Nama']}\n")
print(f"Beberapa kolom:\n{df[['Nama', 'IPK']]}\n")

# Seleksi baris
print(f"Baris ke-0 (iloc):\n{df.iloc[0]}\n")
print(f"Baris 1-3 (iloc):\n{df.iloc[1:4]}\n")

# loc - seleksi berdasarkan label
print(f"loc[0, 'Nama'] = {df.loc[0, 'Nama']}")
print(f"loc[0:2, 'Nama':'Jurusan']:\n{df.loc[0:2, 'Nama':'Jurusan']}\n")

# ============================================
# 5. Filtering
# ============================================
print("=== Filtering ===")

# Filter sederhana
ipk_tinggi = df[df["IPK"] >= 3.75]
print(f"IPK >= 3.75:\n{ipk_tinggi}\n")

# Filter majemuk
informatika_aktif = df[(df["Jurusan"] == "Informatika") & (df["Aktif"] == True)]
print(f"Informatika & Aktif:\n{informatika_aktif}\n")

# isin
jurusan_filter = df[df["Jurusan"].isin(["Informatika", "Teknik Elektro"])]
print(f"Jurusan Informatika/Teknik Elektro:\n{jurusan_filter}\n")

# ============================================
# 6. Menambah & Mengubah Data
# ============================================
print("=== Menambah & Mengubah ===")

# Menambah kolom baru
df["Semester"] = [5, 7, 3, 9, 5]
df["Lulus"] = df["IPK"] >= 3.70

print(f"Setelah tambah kolom:\n{df}\n")

# Mengubah nilai
df.loc[2, "Aktif"] = True
print(f"Setelah ubah Candra jadi Aktif:\n{df}\n")

# ============================================
# 7. Sorting
# ============================================
print("=== Sorting ===")

by_ipk = df.sort_values("IPK", ascending=False)
print(f"Sort by IPK (desc):\n{by_ipk}\n")

by_multi = df.sort_values(["Jurusan", "IPK"], ascending=[True, False])
print(f"Sort by Jurusan lalu IPK:\n{by_multi}\n")

# ============================================
# 8. Groupby & Agregasi
# ============================================
print("=== Groupby & Agregasi ===")

# Groupby
grouped = df.groupby("Jurusan")["IPK"].agg(["mean", "min", "max", "count"])
print(f"Statistik IPK per Jurusan:\n{grouped}\n")

# Value counts
print(f"Jumlah per Jurusan:\n{df['Jurusan'].value_counts()}\n")

# ============================================
# 9. Handling Missing Data
# ============================================
print("=== Missing Data ===")

# Buat DataFrame dengan missing data
df_missing = pd.DataFrame(
    {
        "Nama": ["Ali", "Beti", "Cici", "Dodi"],
        "Nilai": [85, np.nan, 78, np.nan],
        "Kota": ["Jakarta", "Bandung", np.nan, "Surabaya"],
    }
)
print(f"Data dengan NaN:\n{df_missing}\n")

# Cek missing data
print(f"Jumlah NaN per kolom:\n{df_missing.isnull().sum()}\n")

# Isi NaN
filled = df_missing.fillna({"Nilai": df_missing["Nilai"].mean(), "Kota": "Unknown"})
print(f"Setelah fillna:\n{filled}\n")

# Drop baris dengan NaN
dropped = df_missing.dropna()
print(f"Setelah dropna:\n{dropped}\n")

# ============================================
# 10. Contoh Praktis: Analisis Data Sederhana
# ============================================
print("=== Contoh: Analisis Data Penjualan ===")

np.random.seed(42)
penjualan = pd.DataFrame(
    {
        "Tanggal": pd.date_range("2024-01-01", periods=10, freq="D"),
        "Produk": np.random.choice(["Laptop", "Mouse", "Keyboard", "Monitor"], 10),
        "Quantity": np.random.randint(1, 20, 10),
        "Harga_Satuan": np.random.choice([15_000_000, 150_000, 500_000, 3_000_000], 10),
    }
)
penjualan["Total"] = penjualan["Quantity"] * penjualan["Harga_Satuan"]

print(f"Data Penjualan:\n{penjualan}\n")

# Ringkasan per produk
ringkasan = (
    penjualan.groupby("Produk")
    .agg(
        Total_Qty=("Quantity", "sum"),
        Total_Penjualan=("Total", "sum"),
        Rata_Rata=("Total", "mean"),
    )
    .sort_values("Total_Penjualan", ascending=False)
)

print(f"Ringkasan per Produk:\n{ringkasan}\n")
print(f"Grand Total: Rp{penjualan['Total'].sum():,.0f}")

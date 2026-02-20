"""
==========================================================
 TUGAS 4 - Analisis Data Penjualan
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame penjualan 30 hari dengan kolom:
    Tanggal (pd.date_range), Produk (acak dari 5 produk),
    Kategori, Quantity (1-50), Harga_Satuan
 2. Tambah kolom Total = Quantity * Harga_Satuan
 3. Analisis:
    - Total keseluruhan penjualan
    - Produk dengan penjualan tertinggi
    - Kategori dengan penjualan tertinggi
    - Rata-rata penjualan per hari
    - Hari dengan penjualan terbaik dan terburuk
 4. Groupby + agg: sum, mean, count per produk
 5. Tampilkan semua hasil dalam format rapi

 Produk & Kategori:
 | Produk          | Kategori    | Harga Satuan |
 |-----------------|-------------|--------------|
 | Laptop          | Elektronik  | 12_000_000   |
 | Mouse           | Elektronik  | 150_000      |
 | Buku Tulis      | ATK         | 15_000       |
 | Pulpen          | ATK         | 8_000        |
 | Flash Drive     | Elektronik  | 85_000       |
==========================================================
"""

import pandas as pd
import numpy as np

# Menentukan seed agar hasil tetap konsisten
np.random.seed(42)

# 1. Inisialisasi Data Produk dan Kategori
produk_data = {
    'Laptop': {'Kategori': 'Elektronik', 'Harga': 15000000},
    'Mouse': {'Kategori': 'Aksesoris', 'Harga': 250000},
    'Monitor': {'Kategori': 'Elektronik', 'Harga': 2500000},
    'Keyboard': {'Kategori': 'Aksesoris', 'Harga': 500000},
    'Printer': {'Kategori': 'Elektronik', 'Harga': 1200000}
}

# 2. Buat DataFrame simulasi data penjualan (30 hari)
n_hari = 30
tanggal = pd.date_range(start='2026-01-01', periods=n_hari)

# Generate data random
produk_names = list(produk_data.keys())
selected_produk = np.random.choice(produk_names, n_hari)
quantities = np.random.randint(1, 51, n_hari)

# Ambil Harga dan Kategori berdasarkan produk yang terpilih
prices = [produk_data[p]['Harga'] for p in selected_produk]
categories = [produk_data[p]['Kategori'] for p in selected_produk]

df = pd.DataFrame({
    'Tanggal': tanggal,
    'Produk': selected_produk,
    'Kategori': categories,
    'Quantity': quantities,
    'Harga_Satuan': prices
})

# 3. Tambahkan kolom Total
df['Total'] = df['Quantity'] * df['Harga_Satuan']

# 4. Analisis Data
total_keseluruhan = df['Total'].sum()
rata_harian = df['Total'].mean()

# Produk & Kategori tertinggi
produk_stats = df.groupby('Produk')['Total'].sum()
top_produk = produk_stats.idxmax()
top_produk_val = produk_stats.max()

kat_stats = df.groupby('Kategori')['Total'].sum()
top_kat = kat_stats.idxmax()

# Hari tertinggi & terendah
hari_tertinggi = df.loc[df['Total'].idxmax()]
hari_terendah = df.loc[df['Total'].idxmin()]

# 5. Ringkasan menggunakan groupby + agg
ringkasan = df.groupby('Produk').agg(
    Qty_Total=('Quantity', 'sum'),
    Total_Penjualan=('Total', 'sum'),
    Rata_Rata=('Total', 'mean')
).sort_values(by='Total_Penjualan', ascending=False)

# --- OUTPUT LAPORAN ---
print("===== LAPORAN ANALISIS PENJUALAN =====")
print(f"Periode: {tanggal.min().date()} s/d {tanggal.max().date()}\n")

print("--- Ringkasan per Produk ---")
print(f"{'Produk':<12} | {'Qty Total':<9} | {'Total Penjualan':<16} | {'Rata-Rata'}")
print("-" * 60)
for produk, row in ringkasan.iterrows():
    print(f"{produk:<12} | {int(row['Qty_Total']):<9} | Rp{int(row['Total_Penjualan']):>14,d} | Rp{row['Rata_Rata']:>12,.0f}")

print("\n--- Grand Total ---")
print(f"Total Penjualan  : Rp{total_keseluruhan:,d}")
print(f"Rata-rata/hari   : Rp{rata_harian:,.0f}")
print(f"Produk Terlaris  : {top_produk} (Rp{top_produk_val:,d})")
print(f"Kategori Utama   : {top_kat}")
print(f"Hari Tertinggi   : {hari_tertinggi['Tanggal'].date()} (Rp{hari_tertinggi['Total']:,d})")
print(f"Hari Terendah    : {hari_terendah['Tanggal'].date()} (Rp{hari_terendah['Total']:,d})")

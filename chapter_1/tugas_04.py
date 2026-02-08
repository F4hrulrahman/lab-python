"""
==========================================================
 TUGAS 4 - Menghitung Luas & Keliling Bangun Datar
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat variabel untuk dimensi: persegi, persegi panjang,
    lingkaran, dan segitiga
 2. Hitung luas dan keliling masing-masing bangun datar
 3. Gunakan konstanta PI = 3.14159 untuk lingkaran
 4. Tampilkan hasil dalam format tabel yang rapi
 5. Gunakan operator assignment (+=) untuk menghitung total luas

 Contoh Output:
 ============ LUAS & KELILING BANGUN DATAR ============
 Bangun            |    Luas   |  Keliling
 --------------------------------------------------
 Persegi           |     25.00 |     20.00
 Persegi Panjang   |     40.00 |     26.00
 Lingkaran         |     78.54 |     31.42
 Segitiga          |     24.00 |     24.00
 --------------------------------------------------
 Total Luas        |    167.54
 ======================================================
==========================================================
"""

# ── Konstanta ─────────────────────────────────────────────────────────────────
PI = 3.14159

# ── Dimensi Bangun Datar ─────────────────────────────────────────────────────
# TODO: Deklarasikan variabel dimensi untuk setiap bangun

# Persegi
sisi_persegi = ...

# Persegi Panjang
panjang = ...
lebar = ...

# Lingkaran
jari_jari = ...

# Segitiga (sisi a, b, c dan tinggi)
sisi_a = ...
sisi_b = ...
sisi_c = ...
tinggi_segitiga = ...
alas_segitiga = ...


# ── Perhitungan Luas ─────────────────────────────────────────────────────────
# TODO: Hitung luas masing-masing bangun datar
# Rumus:
#   Persegi         : sisi * sisi
#   Persegi Panjang : panjang * lebar
#   Lingkaran       : PI * jari_jari ** 2
#   Segitiga        : 0.5 * alas * tinggi

luas_persegi = ...
luas_persegi_panjang = ...
luas_lingkaran = ...
luas_segitiga = ...


# ── Perhitungan Keliling ─────────────────────────────────────────────────────
# TODO: Hitung keliling masing-masing bangun datar
# Rumus:
#   Persegi         : 4 * sisi
#   Persegi Panjang : 2 * (panjang + lebar)
#   Lingkaran       : 2 * PI * jari_jari
#   Segitiga        : sisi_a + sisi_b + sisi_c

keliling_persegi = ...
keliling_persegi_panjang = ...
keliling_lingkaran = ...
keliling_segitiga = ...


# ── Total Luas (gunakan operator +=) ─────────────────────────────────────────
# TODO: Hitung total luas menggunakan operator +=
total_luas = 0
# total_luas += luas_persegi
# total_luas += luas_persegi_panjang
# ...


# ── Tampilkan Hasil dalam Format Tabel ───────────────────────────────────────
# TODO: Tampilkan semua hasil dalam format tabel yang rapi
# Contoh:
# print("============ LUAS & KELILING BANGUN DATAR ============")
# print(f"{'Bangun':<18}| {'Luas':>9} | {'Keliling':>9}")
# print("-" * 50)
# print(f"{'Persegi':<18}| {luas_persegi:>9.2f} | {keliling_persegi:>9.2f}")
# ...


# TUGAS 4 - Menghitung Luas & Keliling (tugas_04.py)
# Chapter 1: Dasar Python
# Laboratorium Python & Dasar AI
# Universitas Muhammadiyah Makassar

import math

# ── Definisi Dimensi & Konstanta ────────────────────────
PI = 3.14159

# Dimensi Bangun Datar
sisi_persegi = 5
panjang_pp   = 8
lebar_pp     = 4
jari_lingkaran = 7
alas_segitiga  = 6
tinggi_segitiga = 8
sisi_miring_segitiga = 10 # Untuk keliling (asumsi siku-siku)

# Variabel penampung total luas (menggunakan assignment += nantinya)
total_luas = 0

# ── Perhitungan ──────────────────────────────────────────

# Persegi
luas_p = sisi_persegi * sisi_persegi
kel_p  = 4 * sisi_persegi
total_luas += luas_p

# Persegi Panjang
luas_pp = panjang_pp * lebar_pp
kel_pp  = 2 * (panjang_pp + lebar_pp)
total_luas += luas_pp

# Lingkaran
luas_l = PI * (jari_lingkaran ** 2)
kel_l  = 2 * PI * jari_lingkaran
total_luas += luas_l

# Segitiga
luas_s = 0.5 * alas_segitiga * tinggi_segitiga
kel_s  = alas_segitiga + tinggi_segitiga + sisi_miring_segitiga
total_luas += luas_s

# ── Tampilkan Hasil dalam Format Tabel ───────────────────
print("=" * 55)
print(f"{'BANGUN DATAR':<20} | {'LUAS':<15} | {'KELILING':<15}")
print("-" * 55)
print(f"{'Persegi':<20} | {luas_p:<15.2f} | {kel_p:<15.2f}")
print(f"{'Persegi Panjang':<20} | {luas_pp:<15.2f} | {kel_pp:<15.2f}")
print(f"{'Lingkaran':<20} | {luas_l:<15.2f} | {kel_l:<15.2f}")
print(f"{'Segitiga':<20} | {luas_s:<15.2f} | {kel_s:<15.2f}")
print("-" * 55)
print(f"{'TOTAL LUAS SEMUA BANGUN':<20} : {total_luas:.2f}")
print("=" * 55)

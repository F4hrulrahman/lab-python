"""
==========================================================
 TUGAS 3 - Analisis Teks dengan Set
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Definisikan 2 string kalimat (minimal 10 kata per kalimat)
 2. Konversi setiap kalimat menjadi set kata unik (lowercase)
 3. Tampilkan intersection (kata di kedua kalimat)
 4. Tampilkan difference (kata hanya di kalimat 1 / kalimat 2)
 5. Tampilkan union (semua kata unik)
 6. Tampilkan symmetric difference (kata di salah satu saja)
 7. Hitung jumlah kata unik total
==========================================================
"""

# ── Data Kalimat ─────────────────────────────────────────────────────────────
# TODO: Definisikan 2 kalimat (minimal 10 kata per kalimat)
kalimat_1 = "..."  # Ganti dengan kalimat Anda
kalimat_2 = "..."  # Ganti dengan kalimat Anda


# ── Konversi ke Set ──────────────────────────────────────────────────────────
# TODO: Konversi kalimat menjadi set kata unik (lowercase)
# Hint: set(kalimat.lower().split())
kata_set_1 = ...
kata_set_2 = ...


# ── Intersection (kata yang muncul di KEDUA kalimat) ─────────────────────────
# TODO: kata_set_1 & kata_set_2  ATAU  kata_set_1.intersection(kata_set_2)
kata_sama = ...


# ── Difference (kata HANYA di kalimat 1) ─────────────────────────────────────
# TODO: kata_set_1 - kata_set_2  ATAU  kata_set_1.difference(kata_set_2)
hanya_kalimat_1 = ...


# ── Difference (kata HANYA di kalimat 2) ─────────────────────────────────────
# TODO: kata_set_2 - kata_set_1
hanya_kalimat_2 = ...


# ── Union (SEMUA kata unik dari kedua kalimat) ──────────────────────────────
# TODO: kata_set_1 | kata_set_2  ATAU  kata_set_1.union(kata_set_2)
semua_kata = ...


# ── Symmetric Difference (kata di SALAH SATU saja) ──────────────────────────
# TODO: kata_set_1 ^ kata_set_2  ATAU  kata_set_1.symmetric_difference(kata_set_2)
kata_unik_masing = ...


# ── Tampilkan Hasil ──────────────────────────────────────────────────────────
# TODO: Tampilkan semua hasil operasi set dengan format rapi
# print(f"Kata di kedua kalimat (intersection): {kata_sama}")
# print(f"Jumlah kata unik total: {len(semua_kata)}")
# ...

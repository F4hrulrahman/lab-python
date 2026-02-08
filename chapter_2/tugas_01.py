"""
==========================================================
 TUGAS 1 - Manajemen Nilai Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat sebuah list berisi 10 nilai ujian (integer, range 0-100)
 2. Tampilkan: nilai tertinggi, terendah, rata-rata (hitung manual)
 3. Urutkan list dari terkecil ke terbesar
 4. Gunakan list comprehension untuk filter nilai >= 70 (lulus)
 5. Hitung jumlah mahasiswa lulus dan tidak lulus
 6. Tambahkan 2 nilai baru (append), hapus nilai terkecil (remove)
==========================================================
"""

# ── Data Nilai ────────────────────────────────────────────────────────────────
# TODO: Buat list berisi 10 nilai ujian
nilai = ...  # Contoh: [85, 60, 92, 45, 78, 55, 90, 73, 68, 88]


# ── Statistik Dasar (hitung manual, tanpa library) ───────────────────────────
# TODO: Hitung nilai tertinggi, terendah, dan rata-rata
# Hint: gunakan max(), min(), sum(), len()
nilai_tertinggi = ...
nilai_terendah = ...
rata_rata = ...


# ── Pengurutan ────────────────────────────────────────────────────────────────
# TODO: Urutkan list dari terkecil ke terbesar
# Hint: gunakan sorted() atau .sort()


# ── List Comprehension: Filter Nilai Lulus ────────────────────────────────────
# TODO: Gunakan list comprehension untuk membuat list nilai >= 70
nilai_lulus = ...  # [n for n in nilai if n >= 70]


# ── Hitung Lulus & Tidak Lulus ────────────────────────────────────────────────
# TODO: Hitung jumlah mahasiswa lulus dan tidak lulus
jumlah_lulus = ...
jumlah_tidak_lulus = ...


# ── Manipulasi List ──────────────────────────────────────────────────────────
# TODO: Tambahkan 2 nilai baru menggunakan append()
# TODO: Hapus nilai terkecil menggunakan remove()


# ── Tampilkan Hasil ──────────────────────────────────────────────────────────
# TODO: Tampilkan semua hasil dengan format rapi
# Contoh:
# print("===== MANAJEMEN NILAI MAHASISWA =====")
# print(f"Nilai awal   : {nilai}")
# print(f"Tertinggi    : {nilai_tertinggi}")
# ...

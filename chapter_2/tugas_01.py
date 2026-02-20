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

# ===== MANAJEMEN NILAI MAHASISWA =====

# 1. Inisialisasi list nilai
nilai = [85, 60, 92, 45, 78, 55, 90, 73, 68, 88]
print("===== MANAJEMEN NILAI MAHASISWA =====")
print(f"Nilai awal   : {nilai}")

# 2. Hitung tertinggi, terendah, dan rata-rata secara manual
tertinggi = nilai[0]
terendah = nilai[0]
total = 0

for n in nilai:
    if n > tertinggi:
        tertinggi = n
    if n < terendah:
        terendah = n
    total += n

rata_rata = total / len(nilai)

# --- PERBAIKAN DI SINI ---
print(f"Tertinggi    : {tertinggi}")
print(f"Terendah     : {terendah}") # Sudah diperbaiki dari 'terterendah'
print(f"Rata-rata    : {rata_rata}")
# -------------------------

# 3. Urutkan list (kecil ke besar)
nilai_urut = sorted(nilai)
print(f"Nilai sorted : {nilai_urut}")

# 4. List comprehension untuk nilai >= 70
nilai_lulus = [n for n in nilai if n >= 70]
print(f"Nilai lulus  : {nilai_lulus}")

# 5. Hitung jumlah lulus dan tidak lulus
jml_lulus = len(nilai_lulus)
jml_tidak_lulus = len(nilai) - jml_lulus
print(f"Lulus: {jml_lulus} | Tidak lulus: {jml_tidak_lulus}")

# 6. Tambahkan 2 nilai baru dan hapus nilai terkecil
nilai.append(95)
nilai.append(40)

# Cari nilai terkecil yang baru untuk dihapus secara manual
min_baru = nilai[0]
for n in nilai:
    if n < min_baru:
        min_baru = n

nilai.remove(min_baru)
print(f"List Final   : {nilai}")

# ── Tampilkan Hasil ──────────────────────────────────────────────────────────
# TODO: Tampilkan semua hasil dengan format rapi
# Contoh:
# print("===== MANAJEMEN NILAI MAHASISWA =====")
# print(f"Nilai awal   : {nilai}")
# print(f"Tertinggi    : {nilai_tertinggi}")
# ...

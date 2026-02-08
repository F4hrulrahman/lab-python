"""
==========================================================
 TUGAS 1 - Sistem Penilaian Akademik
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi hitung_grade(nilai) -> grade (A/B/C/D/E)
 2. Buat fungsi status_kelulusan(grade) -> "LULUS"/"TIDAK LULUS"
 3. Buat list 10 mahasiswa (nama, nilai) sebagai list of tuple
 4. Proses semua mahasiswa, tampilkan dalam format tabel
 5. Hitung jumlah lulus, tidak lulus, dan persentasenya
 6. Gunakan ternary operator minimal 1 kali

 Tabel Grade:
 | 90-100 | A | Sangat Baik    |
 | 80-89  | B | Baik           |
 | 70-79  | C | Cukup          |
 | 60-69  | D | Kurang         |
 | 0-59   | E | Sangat Kurang  |
==========================================================
"""


def hitung_grade(nilai):
    """Menentukan grade berdasarkan nilai angka (0-100).

    Args:
        nilai (int): Nilai angka mahasiswa (0-100).

    Returns:
        tuple: (grade, keterangan) misal ("A", "Sangat Baik")
    """
    # TODO: Implementasikan percabangan if/elif/else
    # 90-100 -> ("A", "Sangat Baik")
    # 80-89  -> ("B", "Baik")
    # 70-79  -> ("C", "Cukup")
    # 60-69  -> ("D", "Kurang")
    # 0-59   -> ("E", "Sangat Kurang")
    ...


def status_kelulusan(grade):
    """Menentukan status kelulusan berdasarkan grade.

    Args:
        grade (str): Grade mahasiswa (A/B/C/D/E).

    Returns:
        str: "LULUS" jika A/B/C, "TIDAK LULUS" jika D/E.
    """
    # TODO: Implementasikan (boleh gunakan ternary operator)
    ...


# ── Data Mahasiswa ────────────────────────────────────────────────────────────
# TODO: Buat list of tuple berisi 10 mahasiswa (nama, nilai)
data_mahasiswa = [
    # ("Nama Mahasiswa", nilai),
    # ...
]


# ── Proses & Tampilkan ───────────────────────────────────────────────────────
# TODO: Gunakan perulangan untuk memproses semua mahasiswa
# Contoh:
# print("=" * 65)
# print(f"{'No':>2} | {'Nama':<18} | {'Nilai':>5} | {'Grade':>5} | {'Keterangan':<14} | {'Status'}")
# print("-" * 65)
# for i, (nama, nilai) in enumerate(data_mahasiswa, 1):
#     grade, keterangan = hitung_grade(nilai)
#     status = status_kelulusan(grade)
#     print(f"{i:>2} | {nama:<18} | {nilai:>5} | {grade:>5} | {keterangan:<14} | {status}")


# ── Statistik ────────────────────────────────────────────────────────────────
# TODO: Hitung jumlah lulus, tidak lulus, dan persentase
# jumlah_lulus = ...
# jumlah_tidak_lulus = ...
# persen_lulus = jumlah_lulus / len(data_mahasiswa) * 100
# print(f"Lulus: {jumlah_lulus} ({persen_lulus:.1f}%) | Tidak Lulus: {jumlah_tidak_lulus} (...%)")

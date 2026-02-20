"""
==========================================================
 TUGAS 1 - Sistem Penilaian Akademik
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================
"""

# Fungsi hitung_grade(nilai)
def hitung_grade(nilai):
    if nilai >= 90:
        return "A", "Sangat Baik"
    elif nilai >= 80:
        return "B", "Baik"
    elif nilai >= 70:
        return "C", "Cukup"
    elif nilai >= 60:
        return "D", "Kurang"
    else:
        return "E", "Sangat Kurang"

# Fungsi status_kelulusan(grade)
def status_kelulusan(grade):
    # Menggunakan logika pengecekan grade yang lulus (A, B, C)
    if grade in ["A", "B", "C"]:
        return "LULUS"
    else:
        return "TIDAK LULUS"

# List of tuple (Nama, Nilai)
mahasiswa = [
    ("Ahmad Fauzi", 85), ("Siti Rahma", 92), ("Budi Santoso", 55),
    ("Dina Amalia", 78), ("Eko Saputra", 62), ("Fajri Ramadhan", 95),
    ("Gita Lestari", 45), ("Hadi Wijaya", 73), ("Indra Kurnia", 88),
    ("Joko Anwar", 68)
]

# Variabel penghitung
jml_lulus = 0

print("================== HASIL PENILAIAN AKADEMIK ==================")
print(f"{'No':<2} | {'Nama':<17} | {'Nilai':<5} | {'Grade':<5} | {'Keterangan':<13} | {'Status'}")
print("-" * 62)

# Perulangan untuk memproses data
for i, (nama, nilai) in enumerate(mahasiswa, 1):
    grade, ket = hitung_grade(nilai)
    status = status_kelulusan(grade)
    
# Contoh penggunaan Ternary Operator untuk menghitung jumlah lulus
    jml_lulus += 1 if status == "LULUS" else 0
    
    print(f"{i:>2} | {nama:<17} | {nilai:>5} | {grade:^5} | {ket:<13} | {status}")

# Hitung statistik
total = len(mahasiswa)
jml_tidak_lulus = total - jml_lulus
persen_lulus = (jml_lulus / total) * 100
persen_tidak_lulus = (jml_tidak_lulus / total) * 100

print("=" * 62)
print(f"Lulus: {jml_lulus} ({persen_lulus:.1f}%) | Tidak Lulus: {jml_tidak_lulus} ({persen_tidak_lulus:.1f}%)")

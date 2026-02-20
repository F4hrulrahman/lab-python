"""
==========================================================
 TUGAS 2 - Sistem Data Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================
"""

# Inisialisasi dictionary 5 mahasiswa
mahasiswa = {
    "MHS001": {
        "nama": "Ahmad",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 80}
    },
    "MHS002": {
        "nama": "Budi",
        "jurusan": "Sistem Informasi",
        "nilai": {"Algoritma": 70, "Basis Data": 75, "Jaringan": 72}
    },
    "MHS003": {
        "nama": "Citra",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 95, "Basis Data": 88, "Jaringan": 92}
    },
    "MHS004": {
        "nama": "Dina",
        "jurusan": "Teknik Komputer",
        "nilai": {"Algoritma": 80, "Basis Data": 82, "Jaringan": 85}
    },
    "MHS005": {
        "nama": "Eko",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 65, "Basis Data": 70, "Jaringan": 68}
    }
}

# Tampilkan seluruh data mahasiswa dalam format tabel rapi
print("-" * 65)
print(f"{'NIM':<8} | {'Nama':<10} | {'Jurusan':<18} | {'Rata-rata':<8}")
print("-" * 65)

# Sambil menampilkan tabel, kita akan hitung rata-rata dan cari yang tertinggi
nama_tertinggi = ""
rata_tertinggi = 0

for nim, data in mahasiswa.items():
    # Hitung rata-rata nilai setiap mahasiswa
    total_nilai = sum(data['nilai'].values())
    jumlah_matkul = len(data['nilai'])
    rata_rata = total_nilai / jumlah_matkul
    
    print(f"{nim:<8} | {data['nama']:<10} | {data['jurusan']:<18} | {rata_rata:<8.2f}")
    
    # Cari mahasiswa dengan rata-rata tertinggi
    if rata_rata > rata_tertinggi:
        rata_tertinggi = rata_rata
        nama_tertinggi = data['nama']

print("-" * 65)
print(f"Mahasiswa dengan nilai tertinggi: {nama_tertinggi} ({rata_tertinggi:.2f})")

# Tambahkan 1 mahasiswa baru
mahasiswa["MHS006"] = {
    "nama": "Fajri",
    "jurusan": "Informatika",
    "nilai": {"Algoritma": 88, "Basis Data": 85, "Jaringan": 90}
}

# Dictionary Comprehension: {nama: rata_rata_nilai}
# Kita hitung ulang untuk semua termasuk mahasiswa baru
rekap_nilai = {
    data['nama']: sum(data['nilai'].values()) / len(data['nilai']) 
    for data in mahasiswa.values()
}

print("\nRekap Nilai (Dict Comprehension):")
print(rekap_nilai)

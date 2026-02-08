"""
==========================================================
 TUGAS 2 - Sistem Data Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat dictionary berisi data 5 mahasiswa, setiap mahasiswa
    memiliki: nama, nim, jurusan, dan nilai (dict mata kuliah)
 2. Tampilkan seluruh data mahasiswa dalam format tabel rapi
 3. Hitung rata-rata nilai setiap mahasiswa
 4. Cari mahasiswa dengan rata-rata tertinggi
 5. Tambahkan 1 mahasiswa baru ke dictionary
 6. Gunakan dict comprehension untuk {nama: rata_rata_nilai}

 Contoh Struktur:
 mahasiswa = {
     "MHS001": {
         "nama": "Ahmad",
         "jurusan": "Informatika",
         "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78}
     },
     ...
 }
==========================================================
"""

# ── Data Mahasiswa ────────────────────────────────────────────────────────────
# TODO: Buat dictionary berisi data 5 mahasiswa
mahasiswa = {
    # "MHS001": {
    #     "nama": "...",
    #     "jurusan": "...",
    #     "nilai": {"Mata Kuliah 1": ..., "Mata Kuliah 2": ..., "Mata Kuliah 3": ...}
    # },
    # ... tambahkan 4 mahasiswa lagi
}


# ── Tampilkan Data dalam Format Tabel ─────────────────────────────────────────
# TODO: Tampilkan seluruh data mahasiswa dalam format tabel
# Contoh:
# for nim, data in mahasiswa.items():
#     print(f"{nim} | {data['nama']:<15} | {data['jurusan']:<15} | ...")


# ── Hitung Rata-rata Nilai Setiap Mahasiswa ──────────────────────────────────
# TODO: Hitung rata-rata nilai setiap mahasiswa
# Hint: sum(data["nilai"].values()) / len(data["nilai"])


# ── Cari Mahasiswa dengan Rata-rata Tertinggi ────────────────────────────────
# TODO: Cari dan tampilkan mahasiswa dengan rata-rata tertinggi


# ── Tambahkan Mahasiswa Baru ─────────────────────────────────────────────────
# TODO: Tambahkan 1 mahasiswa baru ke dictionary
# mahasiswa["MHS006"] = { ... }


# ── Dictionary Comprehension ─────────────────────────────────────────────────
# TODO: Buat dict baru {nama: rata_rata_nilai} menggunakan dict comprehension
# Contoh:
# ringkasan = {
#     data["nama"]: sum(data["nilai"].values()) / len(data["nilai"])
#     for nim, data in mahasiswa.items()
# }

"""
Chapter 2 - Bagian 3: Dictionary
==================================
Dictionary menyimpan data dalam pasangan key-value.
Ditulis menggunakan kurung kurawal {}.
"""

# ============================================
# 1. Membuat Dictionary
# ============================================
print("=== Membuat Dictionary ===")
mahasiswa = {
    "nama": "Budi Santoso",
    "umur": 21,
    "jurusan": "Informatika",
    "ipk": 3.75,
    "aktif": True,
}
print(f"mahasiswa = {mahasiswa}")

# Menggunakan dict()
konfigurasi = dict(host="localhost", port=8080, debug=True)
print(f"konfigurasi = {konfigurasi}")

# Dictionary kosong
kosong = {}
print(f"kosong = {kosong}")

# ============================================
# 2. Mengakses Data
# ============================================
print("\n=== Mengakses Data ===")
print(f"mahasiswa['nama']  = {mahasiswa['nama']}")
print(f"mahasiswa['ipk']   = {mahasiswa['ipk']}")

# Menggunakan get() - lebih aman (tidak error jika key tidak ada)
print(f"mahasiswa.get('umur')      = {mahasiswa.get('umur')}")
print(f"mahasiswa.get('alamat')    = {mahasiswa.get('alamat')}")  # None
print(f"mahasiswa.get('alamat', '-') = {mahasiswa.get('alamat', '-')}")  # Default value

# ============================================
# 3. Menambah & Mengubah Data
# ============================================
print("\n=== Menambah & Mengubah ===")
mahasiswa["alamat"] = "Bandung"  # Menambah key baru
mahasiswa["ipk"] = 3.80  # Mengubah value yang ada
print(f"Setelah update: {mahasiswa}")

# update() - menambah/mengubah banyak sekaligus
mahasiswa.update({"semester": 5, "ipk": 3.85})
print(f"Setelah update(): {mahasiswa}")

# ============================================
# 4. Menghapus Data
# ============================================
print("\n=== Menghapus Data ===")
# del
del mahasiswa["aktif"]
print(f"del ['aktif']  -> {mahasiswa}")

# pop() - menghapus dan mengembalikan value
semester = mahasiswa.pop("semester")
print(f"pop('semester') -> dihapus: {semester}")

# pop dengan default (tidak error jika key tidak ada)
tidak_ada = mahasiswa.pop("telepon", "key tidak ditemukan")
print(f"pop('telepon')  -> {tidak_ada}")

# ============================================
# 5. Method Dictionary
# ============================================
print("\n=== Method Dictionary ===")
siswa = {"nama": "Ani", "umur": 18, "kelas": "XII"}

print(f"siswa = {siswa}")
print(f"keys()   = {list(siswa.keys())}")
print(f"values() = {list(siswa.values())}")
print(f"items()  = {list(siswa.items())}")
print(f"len()    = {len(siswa)}")

# ============================================
# 6. Iterasi Dictionary
# ============================================
print("\n=== Iterasi Dictionary ===")

# Iterasi keys
print("Keys:")
for key in siswa:
    print(f"  {key}")

# Iterasi values
print("Values:")
for value in siswa.values():
    print(f"  {value}")

# Iterasi key-value pairs
print("Key-Value pairs:")
for key, value in siswa.items():
    print(f"  {key}: {value}")

# ============================================
# 7. Dictionary Comprehension
# ============================================
print("\n=== Dictionary Comprehension ===")

# Kuadrat angka 1-5
kuadrat = {x: x**2 for x in range(1, 6)}
print(f"Kuadrat: {kuadrat}")

# Filter: hanya angka genap
genap_kuadrat = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Genap kuadrat: {genap_kuadrat}")

# Membalik key-value
original = {"a": 1, "b": 2, "c": 3}
terbalik = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Terbalik: {terbalik}")

# ============================================
# 8. Nested Dictionary
# ============================================
print("\n=== Nested Dictionary ===")
kelas = {
    "siswa_1": {"nama": "Budi", "nilai": {"matematika": 90, "fisika": 85}},
    "siswa_2": {"nama": "Ani", "nilai": {"matematika": 95, "fisika": 88}},
}

print(f"Nama siswa_1: {kelas['siswa_1']['nama']}")
print(f"Nilai MTK siswa_2: {kelas['siswa_2']['nilai']['matematika']}")

# Iterasi nested dict
print("\nDaftar Nilai:")
for id_siswa, data in kelas.items():
    print(f"  {data['nama']}:")
    for mapel, nilai in data["nilai"].items():
        print(f"    {mapel}: {nilai}")

# ============================================
# 9. Cek Keberadaan Key
# ============================================
print("\n=== Cek Keberadaan Key ===")
print(f"'nama' in siswa   : {'nama' in siswa}")
print(f"'alamat' in siswa  : {'alamat' in siswa}")

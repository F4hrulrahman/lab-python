"""
Chapter 1 - Bagian 1: Variabel
================================
Variabel adalah tempat menyimpan data di memori.
Python tidak memerlukan deklarasi tipe data secara eksplisit.
"""

# ============================================
# 1. Mendeklarasikan Variabel
# ============================================
nama = "Budi"
umur = 25
tinggi = 175.5
aktif = True

print("=== Deklarasi Variabel ===")
print("Nama :", nama)
print("Umur :", umur)
print("Tinggi:", tinggi)
print("Aktif :", aktif)

# ============================================
# 2. Aturan Penamaan Variabel
# ============================================
# Boleh:
nama_lengkap = "Budi Santoso"  # snake_case (disarankan di Python)
namaLengkap = "Budi Santoso"  # camelCase (boleh tapi tidak lazim)
_private = "data rahasia"  # diawali underscore
nama2 = "Andi"  # mengandung angka (bukan di awal)

# Tidak boleh (akan error jika dijalankan):
# 2nama = "salah"        # diawali angka
# nama-lengkap = "salah" # menggunakan tanda hubung
# class = "salah"        # menggunakan keyword Python

print("\n=== Aturan Penamaan ===")
print("snake_case  :", nama_lengkap)
print("camelCase   :", namaLengkap)
print("_private    :", _private)

# ============================================
# 3. Multiple Assignment
# ============================================
# Assign beberapa variabel sekaligus
x, y, z = 10, 20, 30
print("\n=== Multiple Assignment ===")
print(f"x = {x}, y = {y}, z = {z}")

# Assign nilai yang sama ke beberapa variabel
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# Swap nilai tanpa variabel sementara
x, y = y, x
print(f"Setelah swap: x = {x}, y = {y}")

# ============================================
# 4. Konstanta (Konvensi)
# ============================================
# Python tidak punya keyword const, tapi konvensi menggunakan HURUF_BESAR
PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 1000

print("\n=== Konstanta (Konvensi) ===")
print("PI       :", PI)
print("GRAVITY  :", GRAVITY)
print("MAX_USERS:", MAX_USERS)

# ============================================
# 5. Memeriksa Tipe Variabel
# ============================================
print("\n=== Tipe Variabel ===")
print(f"nama  -> {type(nama)}")
print(f"umur  -> {type(umur)}")
print(f"tinggi -> {type(tinggi)}")
print(f"aktif  -> {type(aktif)}")

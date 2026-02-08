"""
Chapter 1 - Bagian 2: Tipe Data
=================================
Python memiliki beberapa tipe data bawaan (built-in types).
"""

# ============================================
# 1. Integer (int) - Bilangan Bulat
# ============================================
bilangan_bulat = 42
negatif = -10
besar = 1_000_000  # underscore sebagai pemisah ribuan (Python 3.6+)

print("=== Integer ===")
print(f"bilangan_bulat = {bilangan_bulat} (tipe: {type(bilangan_bulat).__name__})")
print(f"negatif = {negatif}")
print(f"besar = {besar}")

# ============================================
# 2. Float - Bilangan Desimal
# ============================================
desimal = 3.14
ilmiah = 2.5e3  # 2.5 x 10^3 = 2500.0
kecil = 1.5e-4  # 0.00015

print("\n=== Float ===")
print(f"desimal = {desimal} (tipe: {type(desimal).__name__})")
print(f"ilmiah = {ilmiah}")
print(f"kecil = {kecil}")

# ============================================
# 3. String (str) - Teks
# ============================================
satu_baris = "Halo, Python!"
satu_baris_2 = "Bisa pakai petik satu"
multi_baris = """Ini adalah
string yang memiliki
beberapa baris"""

print("\n=== String ===")
print(f"satu_baris = {satu_baris}")
print(f"satu_baris_2 = {satu_baris_2}")
print(f"multi_baris:\n{multi_baris}")

# String operations
teks = "Python Dasar"
print(f"\nPanjang '{teks}': {len(teks)}")
print(f"Huruf besar: {teks.upper()}")
print(f"Huruf kecil: {teks.lower()}")
print(f"Ganti kata : {teks.replace('Dasar', 'Lanjut')}")
print(f"Potong [0:6]: {teks[0:6]}")

# f-string (formatted string literals)
nama = "Andi"
umur = 20
print(f"\nf-string: Nama saya {nama}, umur {umur} tahun")

# ============================================
# 4. Boolean (bool)
# ============================================
benar = True
salah = False

print("\n=== Boolean ===")
print(f"benar = {benar} (tipe: {type(benar).__name__})")
print(f"salah = {salah}")
print(f"10 > 5 = {10 > 5}")
print(f"10 == 5 = {10 == 5}")

# Truthy dan Falsy
print("\n--- Truthy & Falsy ---")
print(f"bool(1)     = {bool(1)}")  # True
print(f"bool(0)     = {bool(0)}")  # False
print(f"bool('')    = {bool('')}")  # False
print(f"bool('abc') = {bool('abc')}")  # True
print(f"bool([])    = {bool([])}")  # False
print(f"bool([1])   = {bool([1])}")  # True
print(f"bool(None)  = {bool(None)}")  # False

# ============================================
# 5. None - Nilai Kosong
# ============================================
kosong = None

print("\n=== None ===")
print(f"kosong = {kosong} (tipe: {type(kosong).__name__})")
print(f"kosong is None: {kosong is None}")

# ============================================
# 6. Type Casting (Konversi Tipe Data)
# ============================================
print("\n=== Type Casting ===")

# String ke Integer
angka_str = "123"
angka_int = int(angka_str)
print(f"int('123')   = {angka_int} (tipe: {type(angka_int).__name__})")

# Integer ke Float
angka_float = float(angka_int)
print(f"float(123)   = {angka_float} (tipe: {type(angka_float).__name__})")

# Float ke Integer (membuang desimal)
bulat = int(3.99)
print(f"int(3.99)    = {bulat} (desimal dibuang, bukan dibulatkan)")

# Integer/Float ke String
teks_angka = str(42)
print(f"str(42)      = '{teks_angka}' (tipe: {type(teks_angka).__name__})")

# Boolean ke Integer
print(f"int(True)    = {int(True)}")  # 1
print(f"int(False)   = {int(False)}")  # 0

# ============================================
# 7. Memeriksa Tipe Data
# ============================================
print("\n=== Memeriksa Tipe Data ===")
print(f"type(42)        = {type(42)}")
print(f"isinstance(42, int)    = {isinstance(42, int)}")
print(f"isinstance(42, float)  = {isinstance(42, float)}")
print(f"isinstance('hi', str)  = {isinstance('hi', str)}")

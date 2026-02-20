
# TUGAS 3 - Operator & Ekspresi (tugas_03.py)
# Chapter 1: Dasar Python
# Laboratorium Python & Dasar AI
# Universitas Muhammadiyah Makassar

# ── Definisi Variabel Bilangan Bulat ─────────────────────
a = 15
b = 4

print(f"Variabel awal: a = {a}, b = {b}")
print("-" * 40)

# ── Operator Aritmatika ──────────────────────────────────
print("--- OPERATOR ARITMATIKA ---")
print(f"{a} + {b}  = {a + b}   (Penjumlahan)")
print(f"{a} - {b}  = {a - b}   (Pengurangan)")
print(f"{a} * {b}  = {a * b}   (Perkalian)")
print(f"{a} / {b}  = {a / b}   (Pembagian)")
print(f"{a} // {b} = {a // b}    (Pembagian Bulat/Floor)")
print(f"{a} % {b}  = {a % b}    (Sisa Bagi/Modulo)")
print(f"{a} ** {b} = {a ** b} (Perpangkatan)")
print("-" * 40)

# ── Operator Perbandingan & Logika ──────────────────────
print("--- OPERATOR PERBANDINGAN & LOGIKA ---")
# Perbandingan
hasil_perbandingan = a > b # True karena 15 > 4
print(f"Apakah a > b? {hasil_perbandingan}")

# Logika (and, or, not)
ekspresi_1 = (a > 10) and (b < 5)   # True and True -> True
ekspresi_2 = (a == 10) or (b == 4)  # False or True -> True
ekspresi_3 = not (a < b)            # not (False) -> True

print(f"Hasil Logika 1 (AND): {ekspresi_1}")
print(f"Hasil Logika 2 (OR) : {ekspresi_2}")
print(f"Hasil Logika 3 (NOT): {ekspresi_3}")
print("-" * 40)

# ── Operator Keanggotaan (in & not in) ──────────────────
print("--- OPERATOR KEANGGOTAAN ---")
buah_list = ["Apel", "Jeruk", "Mangga"]
print(f"List Buah: {buah_list}")
print(f"Apakah 'Apel' ada di list? {'Apel' in buah_list}")
print(f"Apakah 'Pisang' TIDAK ada di list? {'Pisang' not in buah_list}")
print("-" * 40)

# ── Perbedaan == dan is ──────────────────────────────────
print("--- PERBEDAAN == DAN IS ---")
list_x = [1, 2, 3]
list_y = [1, 2, 3]
list_z = list_x

# == memeriksa NILAI (Content)
# is memeriksa IDENTITAS/ALAMAT MEMORI (Object Identity)
print(f"list_x == list_y : {list_x == list_y} (Nilainya sama)")
print(f"list_x is list_y : {list_x is list_y} (Objek berbeda di memori)")
print(f"list_x is list_z : {list_x is list_z} (Objek yang sama/merujuk ke x)")
print("-" * 40)

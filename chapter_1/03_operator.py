"""
Chapter 1 - Bagian 3: Operator
================================
Operator digunakan untuk melakukan operasi pada variabel dan nilai.
"""

# ============================================
# 1. Operator Aritmatika
# ============================================
print("=== Operator Aritmatika ===")
a, b = 15, 4

print(f"{a} + {b}  = {a + b}")  # Penjumlahan
print(f"{a} - {b}  = {a - b}")  # Pengurangan
print(f"{a} * {b}  = {a * b}")  # Perkalian
print(f"{a} / {b}  = {a / b}")  # Pembagian (selalu float)
print(f"{a} // {b} = {a // b}")  # Pembagian bulat (floor division)
print(f"{a} % {b}  = {a % b}")  # Modulus (sisa bagi)
print(f"{a} ** {b} = {a**b}")  # Pangkat (eksponen)

# ============================================
# 2. Operator Perbandingan
# ============================================
print("\n=== Operator Perbandingan ===")
x, y = 10, 20

print(f"{x} == {y} : {x == y}")  # Sama dengan
print(f"{x} != {y} : {x != y}")  # Tidak sama dengan
print(f"{x} > {y}  : {x > y}")  # Lebih besar
print(f"{x} < {y}  : {x < y}")  # Lebih kecil
print(f"{x} >= {y} : {x >= y}")  # Lebih besar atau sama
print(f"{x} <= {y} : {x <= y}")  # Lebih kecil atau sama

# ============================================
# 3. Operator Logika
# ============================================
print("\n=== Operator Logika ===")
p, q = True, False

print(f"True and False = {p and q}")  # AND: keduanya harus True
print(f"True or False  = {p or q}")  # OR: salah satu True
print(f"not True       = {not p}")  # NOT: membalik nilai

# Contoh penggunaan praktis
umur = 25
punya_ktp = True
print(f"\numur = {umur}, punya_ktp = {punya_ktp}")
print(f"Boleh buat SIM (umur >= 17 and punya_ktp): {umur >= 17 and punya_ktp}")

# Short-circuit evaluation
print("\n--- Short-circuit Evaluation ---")
# Python tidak mengevaluasi ekspresi kedua jika sudah tahu hasilnya
print(f"False and (1/0) tidak error karena short-circuit")
hasil = False and (
    1 == 1
)  # (1 == 1) tetap dievaluasi, tapi jika pakai False hasilnya pasti False
print(f"False and True = {hasil}")

# ============================================
# 4. Operator Assignment
# ============================================
print("\n=== Operator Assignment ===")
n = 10
print(f"n = {n}")

n += 5  # n = n + 5
print(f"n += 5  -> n = {n}")

n -= 3  # n = n - 3
print(f"n -= 3  -> n = {n}")

n *= 2  # n = n * 2
print(f"n *= 2  -> n = {n}")

n /= 4  # n = n / 4
print(f"n /= 4  -> n = {n}")

n //= 2  # n = n // 2
print(f"n //= 2 -> n = {n}")

n = 10
n %= 3  # n = n % 3
print(f"\nn = 10; n %= 3  -> n = {n}")

n = 2
n **= 4  # n = n ** 4
print(f"n = 2;  n **= 4 -> n = {n}")

# ============================================
# 5. Operator Identitas
# ============================================
print("\n=== Operator Identitas (is / is not) ===")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"a == b : {a == b}")  # True - nilainya sama
print(f"a is b : {a is b}")  # False - objek berbeda di memori
print(f"a is c : {a is c}")  # True - objek yang sama

# ============================================
# 6. Operator Keanggotaan
# ============================================
print("\n=== Operator Keanggotaan (in / not in) ===")
buah = ["apel", "jeruk", "mangga"]
print(f"buah = {buah}")
print(f"'apel' in buah     : {'apel' in buah}")
print(f"'durian' in buah   : {'durian' in buah}")
print(f"'durian' not in buah: {'durian' not in buah}")

# Juga bisa untuk string
kalimat = "Python itu menyenangkan"
print(f"\n'{kalimat}'")
print(f"'Python' in kalimat: {'Python' in kalimat}")
print(f"'Java' in kalimat  : {'Java' in kalimat}")

# ============================================
# 7. Prioritas Operator
# ============================================
print("\n=== Prioritas Operator ===")
# Dari tertinggi ke terendah: ** -> *, /, //, % -> +, - -> perbandingan -> not -> and -> or
hasil = 2 + 3 * 4**2
print(f"2 + 3 * 4 ** 2 = {hasil}")
print("Langkah: 4**2=16, 3*16=48, 2+48=50")

hasil2 = (2 + 3) * 4**2
print(f"\n(2 + 3) * 4 ** 2 = {hasil2}")
print("Langkah: 2+3=5, 4**2=16, 5*16=80")

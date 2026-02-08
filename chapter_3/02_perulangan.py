"""
Chapter 3 - Bagian 2: Perulangan
===================================
Perulangan digunakan untuk mengeksekusi blok kode secara berulang.
"""

# ============================================
# 1. For Loop
# ============================================
print("=== For Loop ===")

# Iterasi list
buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(f"  Buah: {b}")

# range()
print("\nrange(5):")
for i in range(5):
    print(f"  i = {i}")

print("\nrange(2, 8):")
for i in range(2, 8):
    print(f"  i = {i}")

print("\nrange(0, 20, 5):")
for i in range(0, 20, 5):
    print(f"  i = {i}")

# Iterasi string
print("\nIterasi string 'Python':")
for char in "Python":
    print(f"  {char}", end=" ")
print()

# ============================================
# 2. While Loop
# ============================================
print("\n=== While Loop ===")

hitung = 0
while hitung < 5:
    print(f"  hitung = {hitung}")
    hitung += 1

# While dengan kondisi
print("\nMencari angka habis dibagi 7 dari 50 ke bawah:")
n = 50
while n % 7 != 0:
    n -= 1
print(f"  Ditemukan: {n}")

# ============================================
# 3. break, continue, pass
# ============================================
print("\n=== break ===")
# break - menghentikan loop
for i in range(10):
    if i == 5:
        print(f"  Berhenti di i = {i}")
        break
    print(f"  i = {i}")

print("\n=== continue ===")
# continue - skip iterasi saat ini
print("Bilangan ganjil 1-10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"  {i}", end=" ")
print()

print("\n=== pass ===")
# pass - placeholder, tidak melakukan apa-apa
for i in range(3):
    if i == 1:
        pass  # TODO: implementasi nanti
    else:
        print(f"  i = {i}")

# ============================================
# 4. enumerate()
# ============================================
print("\n=== enumerate() ===")
bahasa = ["Python", "JavaScript", "Go", "Rust"]

for index, nama in enumerate(bahasa):
    print(f"  {index}: {nama}")

print("\nMulai dari 1:")
for index, nama in enumerate(bahasa, start=1):
    print(f"  {index}. {nama}")

# ============================================
# 5. zip()
# ============================================
print("\n=== zip() ===")
nama = ["Budi", "Ani", "Candra"]
umur = [20, 22, 19]
kota = ["Jakarta", "Bandung", "Surabaya"]

for n, u, k in zip(nama, umur, kota):
    print(f"  {n}, umur {u}, dari {k}")

# ============================================
# 6. Nested Loop
# ============================================
print("\n=== Nested Loop ===")

# Tabel perkalian 1-5
print("Tabel Perkalian:")
for i in range(1, 6):
    baris = ""
    for j in range(1, 6):
        baris += f"{i * j:4d}"
    print(f"  {baris}")

# Pola segitiga bintang
print("\nPola Bintang:")
for i in range(1, 6):
    print(f"  {'*' * i}")

# ============================================
# 7. for...else dan while...else
# ============================================
print("\n=== for...else ===")

# else dijalankan jika loop selesai tanpa break
angka_list = [1, 3, 5, 7, 9]

print(f"Cari bilangan genap di {angka_list}:")
for angka in angka_list:
    if angka % 2 == 0:
        print(f"  Ditemukan: {angka}")
        break
else:
    print("  Tidak ada bilangan genap")

# Contoh ditemukan
angka_list2 = [1, 3, 4, 7, 9]
print(f"\nCari bilangan genap di {angka_list2}:")
for angka in angka_list2:
    if angka % 2 == 0:
        print(f"  Ditemukan: {angka}")
        break
else:
    print("  Tidak ada bilangan genap")

# ============================================
# 8. Contoh Praktis: FizzBuzz
# ============================================
print("\n=== FizzBuzz (1-20) ===")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        hasil = "FizzBuzz"
    elif i % 3 == 0:
        hasil = "Fizz"
    elif i % 5 == 0:
        hasil = "Buzz"
    else:
        hasil = str(i)
    print(f"  {i:2d}: {hasil}")

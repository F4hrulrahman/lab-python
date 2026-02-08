"""
Chapter 2 - Bagian 1: List
============================
List adalah struktur data yang ordered, mutable, dan bisa menyimpan
berbagai tipe data. Ditulis menggunakan tanda kurung siku [].
"""

# ============================================
# 1. Membuat List
# ============================================
print("=== Membuat List ===")
buah = ["apel", "jeruk", "mangga", "pisang"]
angka = [1, 2, 3, 4, 5]
campuran = ["hello", 42, 3.14, True, None]
kosong = []

print(f"buah    = {buah}")
print(f"angka   = {angka}")
print(f"campuran = {campuran}")
print(f"kosong  = {kosong}")

# ============================================
# 2. Mengakses Elemen
# ============================================
print("\n=== Mengakses Elemen ===")
print(f"buah[0]  = {buah[0]}")  # Elemen pertama
print(f"buah[2]  = {buah[2]}")  # Elemen ketiga
print(f"buah[-1] = {buah[-1]}")  # Elemen terakhir
print(f"buah[-2] = {buah[-2]}")  # Elemen kedua dari belakang

# ============================================
# 3. Slicing
# ============================================
print("\n=== Slicing ===")
print(f"buah = {buah}")
print(f"buah[1:3]  = {buah[1:3]}")  # Index 1 sampai 2
print(f"buah[:2]   = {buah[:2]}")  # Dari awal sampai index 1
print(f"buah[2:]   = {buah[2:]}")  # Dari index 2 sampai akhir
print(f"buah[::2]  = {buah[::2]}")  # Setiap 2 langkah
print(f"buah[::-1] = {buah[::-1]}")  # Membalik list

# ============================================
# 4. Mengubah Elemen
# ============================================
print("\n=== Mengubah Elemen ===")
buah[1] = "durian"
print(f"buah[1] = 'durian' -> {buah}")

# ============================================
# 5. Method List
# ============================================
print("\n=== Method List ===")
hewan = ["kucing", "anjing"]

# append - menambah di akhir
hewan.append("kelinci")
print(f"append('kelinci')  -> {hewan}")

# insert - menambah di posisi tertentu
hewan.insert(1, "hamster")
print(f"insert(1,'hamster') -> {hewan}")

# extend - menggabungkan list
hewan.extend(["ikan", "burung"])
print(f"extend(['ikan','burung']) -> {hewan}")

# remove - menghapus berdasarkan nilai
hewan.remove("hamster")
print(f"remove('hamster')  -> {hewan}")

# pop - menghapus dan mengembalikan elemen
terakhir = hewan.pop()
print(f"pop()  -> dihapus: '{terakhir}', sisa: {hewan}")

item = hewan.pop(1)
print(f"pop(1) -> dihapus: '{item}', sisa: {hewan}")

# sort dan reverse
angka2 = [3, 1, 4, 1, 5, 9, 2, 6]
angka2.sort()
print(f"\nsort()    -> {angka2}")

angka2.sort(reverse=True)
print(f"sort(reverse=True) -> {angka2}")

angka2.reverse()
print(f"reverse() -> {angka2}")

# len, count, index
print(f"\nlen(angka2)     = {len(angka2)}")
print(f"angka2.count(1) = {angka2.count(1)}")
print(f"angka2.index(5) = {angka2.index(5)}")

# ============================================
# 6. List Comprehension
# ============================================
print("\n=== List Comprehension ===")

# Cara biasa
kuadrat_biasa = []
for i in range(1, 6):
    kuadrat_biasa.append(i**2)
print(f"Cara biasa : {kuadrat_biasa}")

# Dengan list comprehension
kuadrat = [i**2 for i in range(1, 6)]
print(f"Comprehension: {kuadrat}")

# Dengan kondisi (filter)
genap = [i for i in range(1, 11) if i % 2 == 0]
print(f"Genap 1-10 : {genap}")

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix 3x3 : {matrix}")

# ============================================
# 7. Operasi Lain
# ============================================
print("\n=== Operasi Lain ===")

# Concatenation
a = [1, 2] + [3, 4]
print(f"[1,2] + [3,4] = {a}")

# Repetition
b = [0] * 5
print(f"[0] * 5 = {b}")

# Cek keanggotaan
print(f"3 in [1,2,3] = {3 in [1, 2, 3]}")

# Copy (shallow copy)
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]
copy1.append(99)
print(f"\noriginal = {original}")
print(f"copy1 (setelah append 99) = {copy1}")
print("original tidak berubah karena copy bukan reference")

"""
Chapter 2 - Bagian 4: Set
===========================
Set adalah koleksi yang TIDAK BERURUTAN dan TIDAK ADA DUPLIKAT.
Sangat berguna untuk operasi himpunan matematika.
"""

# ============================================
# 1. Membuat Set
# ============================================
print("=== Membuat Set ===")
buah = {"apel", "jeruk", "mangga", "apel"}  # duplikat otomatis dihapus
angka = {1, 2, 3, 4, 5}
kosong = set()  # BUKAN {} (itu dictionary kosong!)

print(f"buah  = {buah}")  # 'apel' hanya muncul sekali
print(f"angka = {angka}")
print(f"kosong = {kosong}")
print(f"type({{}}) = {type({})}")  # dict
print(f"type(set()) = {type(set())}")  # set

# Membuat set dari list (menghapus duplikat)
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unik = set(data)
print(f"\nList: {data}")
print(f"Set:  {unik}")

# ============================================
# 2. Menambah & Menghapus Elemen
# ============================================
print("\n=== Menambah & Menghapus ===")
warna = {"merah", "hijau", "biru"}

# add - menambah satu elemen
warna.add("kuning")
print(f"add('kuning')    -> {warna}")

# update - menambah banyak elemen
warna.update(["ungu", "oranye"])
print(f"update(...)      -> {warna}")

# discard - menghapus (tidak error jika tidak ada)
warna.discard("merah")
print(f"discard('merah') -> {warna}")

warna.discard("pink")  # Tidak error meskipun 'pink' tidak ada

# remove - menghapus (ERROR jika tidak ada)
warna.remove("hijau")
print(f"remove('hijau')  -> {warna}")

# pop - menghapus elemen acak
dihapus = warna.pop()
print(f"pop()            -> dihapus: '{dihapus}', sisa: {warna}")

# ============================================
# 3. Operasi Himpunan
# ============================================
print("\n=== Operasi Himpunan ===")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# Union (gabungan)
print(f"\nA | B  (union)        = {A | B}")
print(f"A.union(B)            = {A.union(B)}")

# Intersection (irisan)
print(f"\nA & B  (intersection) = {A & B}")
print(f"A.intersection(B)    = {A.intersection(B)}")

# Difference (selisih)
print(f"\nA - B  (difference)   = {A - B}")  # Ada di A, tidak di B
print(f"B - A  (difference)   = {B - A}")  # Ada di B, tidak di A

# Symmetric Difference (elemen yang hanya di salah satu)
print(f"\nA ^ B  (symmetric diff) = {A ^ B}")
print(f"A.symmetric_difference(B) = {A.symmetric_difference(B)}")

# ============================================
# 4. Relasi Himpunan
# ============================================
print("\n=== Relasi Himpunan ===")
C = {1, 2, 3}
D = {1, 2, 3, 4, 5}

print(f"C = {C}")
print(f"D = {D}")
print(f"C.issubset(D)   = {C.issubset(D)}")  # C subset dari D?
print(f"D.issuperset(C) = {D.issuperset(C)}")  # D superset dari C?

E = {10, 20}
print(f"\nE = {E}")
print(f"C.isdisjoint(E) = {C.isdisjoint(E)}")  # Tidak ada irisan?

# ============================================
# 5. Frozen Set (Immutable Set)
# ============================================
print("\n=== Frozen Set ===")
fs = frozenset([1, 2, 3, 4, 5])
print(f"frozenset = {fs}")

try:
    fs.add(6)
except AttributeError as e:
    print(f"Error: {e}")
print("Frozenset tidak bisa diubah (immutable)")

# ============================================
# 6. Set Comprehension
# ============================================
print("\n=== Set Comprehension ===")
kuadrat = {x**2 for x in range(1, 6)}
print(f"Kuadrat 1-5: {kuadrat}")

huruf = {char.lower() for char in "Hello World" if char.isalpha()}
print(f"Huruf unik 'Hello World': {huruf}")

# ============================================
# 7. Penggunaan Praktis
# ============================================
print("\n=== Penggunaan Praktis ===")

# Menghapus duplikat dari list sambil menjaga urutan
data_asli = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unik_berurutan = list(dict.fromkeys(data_asli))
print(f"Data asli       : {data_asli}")
print(f"Unik & berurutan: {unik_berurutan}")


# Cek apakah semua elemen unik
def semua_unik(data):
    return len(data) == len(set(data))


print(f"\n[1,2,3] semua unik? {semua_unik([1, 2, 3])}")
print(f"[1,2,2] semua unik? {semua_unik([1, 2, 2])}")

# Mencari elemen yang sama dari dua list
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
sama = set(list_a) & set(list_b)
print(f"\nElemen sama dari {list_a} dan {list_b}: {sama}")

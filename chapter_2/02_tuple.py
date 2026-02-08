"""
Chapter 2 - Bagian 2: Tuple
==============================
Tuple mirip dengan list, tapi IMMUTABLE (tidak bisa diubah setelah dibuat).
Ditulis menggunakan tanda kurung ().
"""

# ============================================
# 1. Membuat Tuple
# ============================================
print("=== Membuat Tuple ===")
koordinat = (10, 20)
warna = ("merah", "hijau", "biru")
campuran = (1, "hello", 3.14, True)
satu_elemen = (42,)  # Perhatikan koma! Tanpa koma bukan tuple
kosong = ()

print(f"koordinat  = {koordinat}")
print(f"warna      = {warna}")
print(f"campuran   = {campuran}")
print(f"satu_elemen = {satu_elemen} (tipe: {type(satu_elemen).__name__})")
print(f"bukan_tuple = {(42)} (tipe: {type((42)).__name__})")  # int, bukan tuple

# Tuple tanpa kurung (tuple packing)
point = 5, 10, 15
print(f"point = 5, 10, 15 -> {point} (tipe: {type(point).__name__})")

# ============================================
# 2. Mengakses Elemen
# ============================================
print("\n=== Mengakses Elemen ===")
print(f"warna[0]  = {warna[0]}")
print(f"warna[-1] = {warna[-1]}")
print(f"warna[0:2] = {warna[0:2]}")

# ============================================
# 3. Tuple adalah Immutable
# ============================================
print("\n=== Immutable ===")
try:
    warna[0] = "kuning"
except TypeError as e:
    print(f"Error saat mengubah: {e}")
print("Tuple tidak bisa diubah setelah dibuat!")

# ============================================
# 4. Tuple Unpacking
# ============================================
print("\n=== Tuple Unpacking ===")

# Basic unpacking
x, y = koordinat
print(f"x, y = {koordinat} -> x={x}, y={y}")

# Unpacking dengan *
pertama, *sisanya = (1, 2, 3, 4, 5)
print(f"pertama, *sisanya = (1,2,3,4,5)")
print(f"  pertama = {pertama}")
print(f"  sisanya = {sisanya}")

awal, *tengah, akhir = (10, 20, 30, 40, 50)
print(f"\nawal, *tengah, akhir = (10,20,30,40,50)")
print(f"  awal   = {awal}")
print(f"  tengah = {tengah}")
print(f"  akhir  = {akhir}")

# Swap menggunakan tuple unpacking
a, b = 1, 2
a, b = b, a
print(f"\nSwap: a, b = b, a -> a={a}, b={b}")

# ============================================
# 5. Method Tuple
# ============================================
print("\n=== Method Tuple ===")
angka = (1, 2, 3, 2, 4, 2, 5)

print(f"angka = {angka}")
print(f"angka.count(2) = {angka.count(2)}")  # Hitung kemunculan
print(f"angka.index(3) = {angka.index(3)}")  # Cari index pertama
print(f"len(angka)     = {len(angka)}")
print(f"max(angka)     = {max(angka)}")
print(f"min(angka)     = {min(angka)}")
print(f"sum(angka)     = {sum(angka)}")

# ============================================
# 6. Kapan Menggunakan Tuple
# ============================================
print("\n=== Kapan Pakai Tuple ===")
print("1. Data yang tidak boleh berubah (koordinat, warna RGB)")
print("2. Sebagai key dictionary (list tidak bisa)")
print("3. Return multiple values dari fungsi")
print("4. Lebih cepat dan hemat memori daripada list")

# Contoh: tuple sebagai dictionary key
lokasi = {
    (0, 0): "Origin",
    (3, 4): "Titik A",
    (7, 1): "Titik B",
}
print(f"\nlokasi[(3,4)] = {lokasi[(3, 4)]}")


# Contoh: return multiple values
def hitung_statistik(data):
    return min(data), max(data), sum(data) / len(data)


minimum, maksimum, rata_rata = hitung_statistik([10, 20, 30, 40, 50])
print(f"\nStatistik [10,20,30,40,50]:")
print(f"  Min: {minimum}, Max: {maksimum}, Rata-rata: {rata_rata}")

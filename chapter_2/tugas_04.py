"""
==========================================================
 TUGAS 4 - Tuple untuk Data Koordinat
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================
"""

# Buat list berisi 5 tuple koordinat (x, y)
koordinat = [(1, 2), (4, 6), (7, 1), (2, 9), (5, 3)]
print("Daftar Koordinat:", koordinat)

# Gunakan tuple unpacking untuk menampilkan setiap koordinat
print("\nMenampilkan koordinat (Unpacking):")
for i, (x, y) in enumerate(koordinat, 1):
    print(f"Lokasi {i}: x = {x}, y = {y}")

# Fungsi hitung jarak Euclidean (Manual tanpa math)
# Rumus: d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
print("\n--- Analisis Jarak ---")
def hitung_jarak(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

# Cari pasangan titik yang paling dekat
titik_a, titik_b = None, None
jarak_terdekat = float('inf') # Set awal ke tak terhingga

for i in range(len(koordinat)):
    for j in range(i + 1, len(koordinat)):
        d = hitung_jarak(koordinat[i], koordinat[j])
        if d < jarak_terdekat:
            jarak_terdekat = d
            titik_a, titik_b = koordinat[i], koordinat[j]

print(f"Pasangan titik terdekat: {titik_a} dan {titik_b}")
print(f"Jarak: {jarak_terdekat:.2f}")

# Dictionary dengan tuple sebagai key
lokasi_dict = {
    (1, 2): "Rumah",
    (4, 6): "Kampus Unismuh",
    (7, 1): "Pasar",
    (2, 9): "Rumah Sakit",
    (5, 3): "Kafe"
}
print("\nDictionary Lokasi:", lokasi_dict)

# Buktikan list tidak bisa jadi key (Try-Except)
print("\n--- Pembuktian Hashable ---")
try:
    test_dict = {[1, 2]: "Gagal"}
except TypeError as e:
    print(f"Error: List tidak bisa jadi key karena: {e}")

try:
    test_dict = {(1, 2): "Berhasil"}
    print("Berhasil: Tuple bisa jadi key karena bersifat immutable.")
except TypeError as e:
    print(f"Gagal: {e}")

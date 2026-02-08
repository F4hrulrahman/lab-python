"""
==========================================================
 TUGAS 4 - Tuple untuk Data Koordinat
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat list berisi 5 tuple koordinat (x, y) sebagai lokasi
 2. Gunakan tuple unpacking untuk menampilkan setiap koordinat
 3. Hitung jarak Euclidean antar dua titik:
    d = sqrt((x2-x1)^2 + (y2-y1)^2)  (gunakan ** 0.5, tanpa math)
 4. Cari pasangan titik yang paling dekat jaraknya
 5. Buat dictionary dengan tuple sebagai key, nama lokasi sebagai value
 6. Buktikan tuple bisa jadi key dict tapi list tidak (try-except)
==========================================================
"""

# ── Data Koordinat ───────────────────────────────────────────────────────────
# TODO: Buat list berisi 5 tuple koordinat (x, y)
koordinat = [
    # (x, y),
    # (x, y),
    # ...
]


# ── Tuple Unpacking ──────────────────────────────────────────────────────────
# TODO: Tampilkan setiap koordinat menggunakan unpacking
# Contoh:
# for i, (x, y) in enumerate(koordinat, 1):
#     print(f"Titik {i}: x={x}, y={y}")


# ── Fungsi Jarak Euclidean ───────────────────────────────────────────────────
def hitung_jarak(titik_1, titik_2):
    """Hitung jarak Euclidean antara dua titik.

    Args:
        titik_1 (tuple): Koordinat titik pertama (x, y).
        titik_2 (tuple): Koordinat titik kedua (x, y).

    Returns:
        float: Jarak antara kedua titik.
    """
    # TODO: Implementasikan rumus Euclidean
    # d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    ...


# ── Cari Pasangan Titik Terdekat ─────────────────────────────────────────────
# TODO: Bandingkan semua pasangan titik, cari yang jaraknya paling kecil
# Hint: gunakan nested loop
#   jarak_min = float('inf')
#   for i in range(len(koordinat)):
#       for j in range(i+1, len(koordinat)):
#           jarak = hitung_jarak(koordinat[i], koordinat[j])
#           if jarak < jarak_min:
#               jarak_min = jarak
#               pasangan_terdekat = (i, j)


# ── Tuple sebagai Key Dictionary ─────────────────────────────────────────────
# TODO: Buat dictionary dengan tuple sebagai key
# Contoh:
# lokasi = {
#     (0, 0): "Kampus Unismuh",
#     (3, 4): "Perpustakaan",
#     ...
# }


# ── Buktikan List Tidak Bisa Jadi Key ────────────────────────────────────────
# TODO: Buktikan menggunakan try-except
# try:
#     invalid_dict = {[1, 2]: "ini akan error"}
# except TypeError as e:
#     print(f"Error: {e}")
#     print("List tidak bisa menjadi key dictionary karena mutable!")

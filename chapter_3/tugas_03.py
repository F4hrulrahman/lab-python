"""
==========================================================
 TUGAS 3 - Kalkulator Serbaguna
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi kalkulator(a, b, operasi="+") dengan default param
 2. Tangani pembagian dengan nol
 3. Buat fungsi statistik(*args) -> dict {min, max, sum, mean, count}
 4. Buat fungsi format_output(**kwargs) -> cetak key: value
 5. Demonstrasikan lambda dengan map() (kuadrat)
 6. Demonstrasikan lambda dengan filter() (bilangan genap)
 7. Demonstrasikan lambda dengan sorted() (sort list of tuple)
==========================================================
"""


# Tugas 3 -- Kalkulator Serbaguna (tugas_03.py)

# Fungsi Kalkulator dengan Default Parameter
def kalkulator(a, b, operasi="+"):
    if operasi == "+":
        return a + b
    elif operasi == "-":
        return a - b
    elif operasi == "*":
        return a * b
    elif operasi == "/":
# Tangani pembagian dengan nol
        return "Error: Pembagian nol" if b == 0 else a / b
    elif operasi == "//":
        return "Error: Pembagian nol" if b == 0 else a // b
    elif operasi == "%":
        return a % b
    elif operasi == "**":
        return a ** b
    else:
        return "Operasi tidak dikenal"

# Fungsi Statistik menggunakan *args
def statistik(*args):
    if not args:
        return None
    # Hitung manual tanpa library
    total = sum(args)
    count = len(args)
    return {
        "min": min(args),
        "max": max(args),
        "sum": total,
        "mean": total / count,
        "count": count
    }

# Fungsi Format Output menggunakan **kwargs
def format_output(**kwargs):
    print("\n--- FORMATTED DATA ---")
    for key, value in kwargs.items():
        print(f"{key.capitalize():<10}: {value}")

# --- DEMONSTRASI ---

# Kalkulator
print("===== KALKULATOR =====")
print(f"8 + 2  = {kalkulator(8, 2)}") # Menggunakan default +
print(f"8 ** 2 = {kalkulator(8, 2, '**')}")
print(f"5 / 0  = {kalkulator(5, 0, '/')}")

# Statistik
hasil_stat = statistik(10, 20, 30, 40, 50)
format_output(judul="Hasil Statistik", **hasil_stat)

# Lambda dengan map() (Kuadrat)
angka = [1, 2, 3, 4, 5]
kuadrat = list(map(lambda x: x**2, angka))
print(f"\nKuadrat {angka} : {kuadrat}")

# Lambda dengan filter() (Genap)
genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"Bilangan Genap  : {genap}")

# Lambda dengan sorted() (Urutkan Tuple berdasarkan Nilai)
data_mhs = [("Nurul", 85), ("Habibah", 92), ("Ciko", 78)]
# Mengurutkan berdasarkan elemen kedua (nilai) secara descending
urut_nilai = sorted(data_mhs, key=lambda x: x[1], reverse=True)
print(f"Urut Nilai (Desc): {urut_nilai}")

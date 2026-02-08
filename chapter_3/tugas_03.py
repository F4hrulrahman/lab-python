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


def kalkulator(a, b, operasi="+"):
    """Kalkulator dasar dengan default parameter.

    Args:
        a (float): Bilangan pertama.
        b (float): Bilangan kedua.
        operasi (str): Operator (+, -, *, /, //, %, **). Default: "+".

    Returns:
        float: Hasil perhitungan, atau None jika operasi tidak valid.
    """
    # TODO: Implementasikan kalkulator
    # Jangan lupa tangani pembagian dengan nol!
    ...


def statistik(*args):
    """Menghitung statistik dari sekumpulan angka.

    Args:
        *args: Bilangan-bilangan yang akan dihitung statistiknya.

    Returns:
        dict: {"min": ..., "max": ..., "sum": ..., "mean": ..., "count": ...}
    """
    # TODO: Implementasikan menggunakan *args
    # Hint: args adalah tuple, bisa pakai min(), max(), sum(), len()
    ...


def format_output(**kwargs):
    """Mencetak data dalam format key: value yang rapi.

    Args:
        **kwargs: Pasangan key-value yang akan dicetak.
    """
    # TODO: Implementasikan menggunakan **kwargs
    # Contoh:
    # for key, value in kwargs.items():
    #     print(f"  {key:<15}: {value}")
    ...


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Demonstrasi kalkulator
    # print("=== Kalkulator ===")
    # print(f"10 + 3 = {kalkulator(10, 3, '+')}")
    # print(f"10 / 0 = {kalkulator(10, 0, '/')}")  # tangani error

    # TODO: Demonstrasi statistik(*args)
    # print("\n=== Statistik ===")
    # hasil = statistik(85, 90, 78, 92, 65, 88, 73)
    # print(hasil)

    # TODO: Demonstrasi format_output(**kwargs)
    # print("\n=== Format Output ===")
    # format_output(nama="Ahmad", nim="105841100123", jurusan="Informatika")

    # TODO: Lambda + map() -> hitung kuadrat dari list
    # angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # kuadrat = list(map(lambda x: x ** 2, angka))
    # print(f"\nKuadrat: {kuadrat}")

    # TODO: Lambda + filter() -> saring bilangan genap
    # genap = list(filter(lambda x: x % 2 == 0, angka))
    # print(f"Genap  : {genap}")

    # TODO: Lambda + sorted() -> urutkan list of tuple
    # mahasiswa = [("Ahmad", 85), ("Siti", 92), ("Budi", 78), ("Dewi", 90)]
    # by_nilai = sorted(mahasiswa, key=lambda x: x[1], reverse=True)
    # print(f"\nUrut by nilai: {by_nilai}")

    pass

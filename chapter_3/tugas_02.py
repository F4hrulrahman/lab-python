"""
==========================================================
 TUGAS 2 - Pola & Deret
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi pola_segitiga(n) -> cetak segitiga bintang
 2. Buat fungsi pola_segitiga_terbalik(n) -> cetak segitiga terbalik
 3. Buat fungsi pola_diamond(n) -> cetak pola diamond/berlian
 4. Buat fungsi deret_fibonacci(n) -> list n bilangan Fibonacci
 5. Buat fungsi is_prima(n) -> True jika n bilangan prima
 6. Tampilkan bilangan prima 1-100 menggunakan filter() + is_prima
==========================================================
"""


def pola_segitiga(n):
    """Mencetak pola segitiga bintang dengan tinggi n.

    Args:
        n (int): Tinggi segitiga.

    Contoh (n=4):
       *
      **
     ***
    ****
    """
    # TODO: Implementasikan
    ...


def pola_segitiga_terbalik(n):
    """Mencetak pola segitiga terbalik dengan tinggi n.

    Args:
        n (int): Tinggi segitiga.

    Contoh (n=4):
    ****
     ***
      **
       *
    """
    # TODO: Implementasikan
    ...


def pola_diamond(n):
    """Mencetak pola diamond/berlian.

    Args:
        n (int): Setengah tinggi diamond (jumlah baris bagian atas).

    Contoh (n=5):
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    """
    # TODO: Implementasikan
    # Hint: bagian atas menggunakan range(1, n+1)
    #        bagian bawah menggunakan range(n-1, 0, -1)
    ...


def deret_fibonacci(n):
    """Mengembalikan list berisi n bilangan Fibonacci pertama.

    Args:
        n (int): Jumlah bilangan Fibonacci yang diinginkan.

    Returns:
        list: Deret Fibonacci. Contoh (n=8): [0, 1, 1, 2, 3, 5, 8, 13]
    """
    # TODO: Implementasikan
    ...


def is_prima(n):
    """Memeriksa apakah n adalah bilangan prima.

    Args:
        n (int): Bilangan yang diperiksa.

    Returns:
        bool: True jika prima, False jika bukan.
    """
    # TODO: Implementasikan
    # Hint: prima > 1 dan tidak habis dibagi bilangan 2..sqrt(n)
    ...


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Tampilkan pola segitiga (n=5)
    # print("=== Pola Segitiga (n=5) ===")
    # pola_segitiga(5)

    # TODO: Tampilkan pola segitiga terbalik (n=5)
    # print("\n=== Pola Segitiga Terbalik (n=5) ===")
    # pola_segitiga_terbalik(5)

    # TODO: Tampilkan pola diamond (n=5)
    # print("\n=== Pola Diamond (n=5) ===")
    # pola_diamond(5)

    # TODO: Tampilkan 15 bilangan Fibonacci
    # print(f"\nFibonacci (15): {deret_fibonacci(15)}")

    # TODO: Tampilkan bilangan prima 1-100 menggunakan filter()
    # bilangan_prima = list(filter(is_prima, range(1, 101)))
    # print(f"\nBilangan prima (1-100): {bilangan_prima}")
    # print(f"Jumlah: {len(bilangan_prima)}")

    pass

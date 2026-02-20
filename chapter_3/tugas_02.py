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


# Tugas 2 -- Pola & Deret (tugas_02.py)

# Fungsi Pola Segitiga Bintang
def pola_segitiga(n):
    print(f"\n--- Segitiga (n={n}) ---")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Fungsi Pola Segitiga Terbalik
def pola_segitiga_terbalik(n):
    print(f"\n--- Segitiga Terbalik (n={n}) ---")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Fungsi Pola Diamond
def pola_diamond(n):
    print(f"\n--- Diamond (n={n}) ---")
    # Bagian Atas
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Bagian Bawah
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Fungsi Deret Fibonacci
def deret_fibonacci(n):
    deret = [0, 1]
    while len(deret) < n:
        deret.append(deret[-1] + deret[-2])
    return deret[:n]

# Fungsi Cek Bilangan Prima
def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Eksekusi Program ---

# Menampilkan Pola
pola_segitiga(5)
pola_segitiga_terbalik(5)
pola_diamond(5)

# Menampilkan Fibonacci
n_fibo = 10
print(f"\nDeret Fibonacci ({n_fibo} angka):")
print(deret_fibonacci(n_fibo))

# Menampilkan Bilangan Prima 1-100 menggunakan filter()
list_angka = list(range(1, 101))
bil_prima = list(filter(is_prima, list_angka))

print("\nBilangan Prima antara 1 - 100:")
print(bil_prima)

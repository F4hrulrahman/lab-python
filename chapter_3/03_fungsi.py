"""
Chapter 3 - Bagian 3: Fungsi
===============================
Fungsi adalah blok kode yang dapat digunakan ulang (reusable).
"""

# ============================================
# 1. Mendefinisikan Fungsi
# ============================================
print("=== Mendefinisikan Fungsi ===")


def sapa():
    """Fungsi sederhana tanpa parameter."""
    print("  Halo! Selamat belajar Python!")


sapa()
sapa()

# ============================================
# 2. Fungsi dengan Parameter & Return
# ============================================
print("\n=== Parameter & Return ===")


def luas_persegi(sisi):
    """Menghitung luas persegi."""
    return sisi**2


def luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga."""
    return 0.5 * alas * tinggi


print(f"Luas persegi (sisi=5): {luas_persegi(5)}")
print(f"Luas segitiga (alas=10, tinggi=8): {luas_segitiga(10, 8)}")

# ============================================
# 3. Default Parameter
# ============================================
print("\n=== Default Parameter ===")


def sapa_nama(nama, sapaan="Halo"):
    """Fungsi dengan default parameter."""
    return f"{sapaan}, {nama}!"


print(sapa_nama("Budi"))
print(sapa_nama("Ani", "Selamat pagi"))
print(sapa_nama("Candra", sapaan="Hey"))

# ============================================
# 4. Keyword Arguments
# ============================================
print("\n=== Keyword Arguments ===")


def buat_profil(nama, umur, kota):
    return f"{nama}, {umur} tahun, dari {kota}"


# Positional arguments
print(buat_profil("Budi", 25, "Jakarta"))

# Keyword arguments (urutan bebas)
print(buat_profil(kota="Bandung", nama="Ani", umur=22))

# Campuran
print(buat_profil("Candra", kota="Surabaya", umur=20))

# ============================================
# 5. *args (Positional Variable Arguments)
# ============================================
print("\n=== *args ===")


def jumlahkan(*angka):
    """Menerima jumlah argumen yang tidak tetap."""
    print(f"  args = {angka} (tipe: {type(angka).__name__})")
    return sum(angka)


print(f"jumlahkan(1, 2, 3) = {jumlahkan(1, 2, 3)}")
print(f"jumlahkan(10, 20) = {jumlahkan(10, 20)}")
print(f"jumlahkan(5) = {jumlahkan(5)}")

# ============================================
# 6. **kwargs (Keyword Variable Arguments)
# ============================================
print("\n=== **kwargs ===")


def cetak_info(**info):
    """Menerima keyword arguments yang tidak tetap."""
    print(f"  kwargs = {info} (tipe: {type(info).__name__})")
    for key, value in info.items():
        print(f"    {key}: {value}")


cetak_info(nama="Budi", umur=25, hobi="coding")

# ============================================
# 7. Kombinasi *args dan **kwargs
# ============================================
print("\n=== Kombinasi *args dan **kwargs ===")


def fungsi_lengkap(wajib, *args, **kwargs):
    print(f"  wajib  = {wajib}")
    print(f"  args   = {args}")
    print(f"  kwargs = {kwargs}")


fungsi_lengkap("data", 1, 2, 3, nama="test", aktif=True)

# ============================================
# 8. Return Multiple Values
# ============================================
print("\n=== Return Multiple Values ===")


def statistik(data):
    """Mengembalikan beberapa nilai sekaligus."""
    return min(data), max(data), sum(data) / len(data)


data = [10, 20, 30, 40, 50]
minimum, maksimum, rata_rata = statistik(data)
print(f"Data: {data}")
print(f"Min: {minimum}, Max: {maksimum}, Rata-rata: {rata_rata}")

# ============================================
# 9. Lambda Function
# ============================================
print("\n=== Lambda Function ===")


# Fungsi biasa
def kuadrat(x):
    return x**2


# Sama dengan lambda
kuadrat_lambda = lambda x: x**2

print(f"kuadrat(5)        = {kuadrat(5)}")
print(f"kuadrat_lambda(5) = {kuadrat_lambda(5)}")

# Lambda sering dipakai dengan fungsi built-in
angka = [3, 1, 4, 1, 5, 9, 2, 6]

# Sorting dengan key
siswa = [("Budi", 80), ("Ani", 95), ("Candra", 70)]
siswa_sorted = sorted(siswa, key=lambda x: x[1], reverse=True)
print(f"\nSiswa sorted by nilai: {siswa_sorted}")

# map
angka_kuadrat = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(f"map(kuadrat, 1-5) = {angka_kuadrat}")

# filter
genap = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(f"filter(genap, 1-10) = {genap}")

# ============================================
# 10. Scope Variabel
# ============================================
print("\n=== Scope Variabel ===")

x = "global"  # Global scope


def fungsi_scope():
    x = "local"  # Local scope
    print(f"  Di dalam fungsi: x = {x}")


fungsi_scope()
print(f"  Di luar fungsi: x = {x}")

# Menggunakan global keyword
counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()
increment()
print(f"\n  counter setelah 3x increment: {counter}")

# ============================================
# 11. Fungsi Rekursif
# ============================================
print("\n=== Fungsi Rekursif ===")


def faktorial(n):
    """Menghitung n! secara rekursif."""
    if n <= 1:
        return 1
    return n * faktorial(n - 1)


def fibonacci(n):
    """Mengembalikan angka fibonacci ke-n."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"5! = {faktorial(5)}")
print(f"10! = {faktorial(10)}")
print(f"Fibonacci ke-10: {fibonacci(10)}")
fib_list = [fibonacci(i) for i in range(10)]
print(f"Fibonacci 0-9: {fib_list}")

# ============================================
# 12. Docstring & Type Hints
# ============================================
print("\n=== Type Hints (Python 3.5+) ===")


def hitung_bmi(berat: float, tinggi_cm: float) -> float:
    """
    Menghitung Body Mass Index (BMI).

    Args:
        berat: Berat badan dalam kg.
        tinggi_cm: Tinggi badan dalam cm.

    Returns:
        Nilai BMI.
    """
    tinggi_m = tinggi_cm / 100
    return round(berat / (tinggi_m**2), 1)


bmi = hitung_bmi(70, 175)
print(f"BMI (70kg, 175cm) = {bmi}")
print(f"Docstring: {hitung_bmi.__doc__[:50]}...")

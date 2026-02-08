"""
Chapter 4 - Bagian 2: Inheritance (Pewarisan)
================================================
Inheritance memungkinkan class baru mewarisi atribut dan method
dari class yang sudah ada.
"""

# ============================================
# 1. Single Inheritance
# ============================================
print("=== Single Inheritance ===")


class Hewan:
    """Class dasar (parent/base class)."""

    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def suara(self):
        return "..."

    def info(self):
        return f"{self.nama} ({self.jenis})"

    def __str__(self):
        return self.info()


class Kucing(Hewan):
    """Class turunan (child/derived class)."""

    def __init__(self, nama, warna):
        super().__init__(nama, "Kucing")  # Memanggil __init__ parent
        self.warna = warna

    def suara(self):
        """Method overriding - mengganti method parent."""
        return "Meong!"

    def info(self):
        return f"{self.nama} ({self.jenis}, warna: {self.warna})"


class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, "Anjing")
        self.ras = ras

    def suara(self):
        return "Guk guk!"

    def info(self):
        return f"{self.nama} ({self.jenis}, ras: {self.ras})"


# Membuat objek
kucing = Kucing("Mimi", "putih")
anjing = Anjing("Buddy", "Golden Retriever")

print(kucing)
print(f"  Suara: {kucing.suara()}")
print(anjing)
print(f"  Suara: {anjing.suara()}")

# ============================================
# 2. Polymorphism
# ============================================
print("\n=== Polymorphism ===")

# Objek berbeda merespons method yang sama dengan cara berbeda
hewan_list = [
    Kucing("Kitty", "hitam"),
    Anjing("Rex", "Husky"),
    Kucing("Luna", "oranye"),
    Anjing("Max", "Poodle"),
]

for h in hewan_list:
    print(f"  {h.info()} -> {h.suara()}")

# ============================================
# 3. isinstance() dan issubclass()
# ============================================
print("\n=== isinstance() dan issubclass() ===")

print(f"kucing isinstance Kucing: {isinstance(kucing, Kucing)}")
print(f"kucing isinstance Hewan:  {isinstance(kucing, Hewan)}")
print(f"kucing isinstance Anjing: {isinstance(kucing, Anjing)}")

print(f"\nKucing issubclass Hewan: {issubclass(Kucing, Hewan)}")
print(f"Anjing issubclass Hewan: {issubclass(Anjing, Hewan)}")
print(f"Kucing issubclass Anjing: {issubclass(Kucing, Anjing)}")

# ============================================
# 4. Multiple Inheritance
# ============================================
print("\n=== Multiple Inheritance ===")


class Terbang:
    def terbang(self):
        return "Bisa terbang!"


class Berenang:
    def berenang(self):
        return "Bisa berenang!"


class Bebek(Hewan, Terbang, Berenang):
    """Mewarisi dari Hewan, Terbang, dan Berenang."""

    def __init__(self, nama):
        super().__init__(nama, "Bebek")

    def suara(self):
        return "Kwek kwek!"


bebek = Bebek("Donald")
print(f"{bebek.info()}")
print(f"  Suara: {bebek.suara()}")
print(f"  {bebek.terbang()}")
print(f"  {bebek.berenang()}")

# Method Resolution Order (MRO)
print(f"\nMRO Bebek: {[cls.__name__ for cls in Bebek.__mro__]}")

# ============================================
# 5. Contoh Praktis: Sistem Karyawan
# ============================================
print("\n=== Contoh Praktis: Sistem Karyawan ===")


class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def __str__(self):
        return f"{self.nama} - Gaji: Rp{self.hitung_gaji():,.0f}"


class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan


class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, lembur_per_jam, jam_lembur):
        super().__init__(nama, gaji_pokok)
        self.lembur_per_jam = lembur_per_jam
        self.jam_lembur = jam_lembur

    def hitung_gaji(self):
        return self.gaji_pokok + (self.lembur_per_jam * self.jam_lembur)


class Intern(Karyawan):
    def __init__(self, nama, gaji_pokok, durasi_bulan):
        super().__init__(nama, gaji_pokok)
        self.durasi_bulan = durasi_bulan

    def __str__(self):
        return f"{self.nama} - Gaji: Rp{self.hitung_gaji():,.0f} (Intern {self.durasi_bulan} bulan)"


karyawan_list = [
    Manager("Pak Budi", 15_000_000, 5_000_000),
    Programmer("Ani", 12_000_000, 100_000, 20),
    Programmer("Candra", 12_000_000, 100_000, 35),
    Intern("Dian", 3_000_000, 6),
]

print("Daftar Karyawan:")
total_gaji = 0
for k in karyawan_list:
    print(f"  {k}")
    total_gaji += k.hitung_gaji()

print(f"\nTotal pengeluaran gaji: Rp{total_gaji:,.0f}")

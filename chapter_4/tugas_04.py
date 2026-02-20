"""
==========================================================
 TUGAS 4 - Class Bangun Ruang
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class BangunRuang (parent) dengan method abstract:
    volume(), luas_permukaan(), info()
 2. Buat subclass: Kubus, Balok, Tabung, Bola
 3. Implementasikan @classmethod sebagai alternative constructor
    (contoh: Kubus.dari_volume(vol) -> buat Kubus dari volume)
 4. Implementasikan @staticmethod untuk validasi
    (contoh: Kubus.is_valid(sisi) -> True jika sisi > 0)
 5. Overload operator __gt__ (>) untuk perbandingan volume
 6. Urutkan list campuran bangun ruang berdasarkan volume
    menggunakan sorted() + lambda

 Konsep yang dipelajari:
 - Abstract class dan method (tanpa ABC, gunakan raise)
 - @classmethod dan @staticmethod
 - Operator overloading (__gt__, __eq__, __lt__)
 - Polymorphism dalam sorted() + lambda
 - Rumus: pi = 3.14159265358979

 Rumus Bangun Ruang:
 | Bangun | Volume              | Luas Permukaan          |
 |--------|---------------------|-------------------------|
 | Kubus  | s^3                 | 6 * s^2                 |
 | Balok  | p * l * t           | 2 * (pl + pt + lt)      |
 | Tabung | pi * r^2 * t        | 2 * pi * r * (r + t)    |
 | Bola   | 4/3 * pi * r^3      | 4 * pi * r^2            |
==========================================================
"""

# Tugas 4 -- Class Bangun Ruang (tugas_04.py)
from abc import ABC, abstractmethod

class BangunRuang(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def luas_permukaan(self):
        pass

    @abstractmethod
    def info(self):
        pass

    # Overload operator > untuk membandingkan volume
    def __gt__(self, other):
        if isinstance(other, BangunRuang):
            return self.volume() > other.volume()
        return NotImplemented

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    @staticmethod
    def is_valid(sisi):
        return sisi > 0

    @classmethod
    def dari_volume(cls, vol):
        # s = akar pangkat 3 dari volume
        sisi = vol ** (1/3)
        return cls(round(sisi, 2))

    def volume(self):
        return self.sisi ** 3

    def luas_permukaan(self):
        return 6 * (self.sisi ** 2)

    def info(self):
        return f"Kubus (s={self.sisi})"

class Balok(BangunRuang):
    def __init__(self, p, l, t):
        self.p, self.l, self.t = p, l, t

    def volume(self):
        return self.p * self.l * self.t

    def luas_permukaan(self):
        return 2 * (self.p*self.l + self.p*self.t + self.l*self.t)

    def info(self):
        return f"Balok ({self.p}x{self.l}x{self.t})"

class Tabung(BangunRuang):
    def __init__(self, r, t):
        self.r, self.t = r, t
        self.pi = 3.14

    def volume(self):
        return self.pi * (self.r**2) * self.t

    def luas_permukaan(self):
        return 2 * self.pi * self.r * (self.r + self.t)

    def info(self):
        return f"Tabung (r={self.r}, t={self.t})"

class Bola(BangunRuang):
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def volume(self):
        return (4/3) * self.pi * (self.r**3)

    def luas_permukaan(self):
        return 4 * self.pi * (self.r**2)

    def info(self):
        return f"Bola (r={self.r})"

# --- EKSEKUSI ---

# 1. Membuat daftar bangun ruang (List of Objects)
daftar_bangun = [
    Kubus(5),
    Balok(4, 3, 2),
    Tabung(7, 10),
    Bola(10),
    Kubus.dari_volume(64) # Menggunakan Class Method
]

# 2. Urutkan berdasarkan Volume (Descending) menggunakan Lambda
daftar_urut = sorted(daftar_bangun, key=lambda x: x.volume(), reverse=True)

# 3. Tampilkan dalam format tabel
print("="*65)
print(f"{'No':<3} | {'Jenis Bangun':<25} | {'Volume':<12} | {'Luas Permukaan'}")
print("-" * 65)

for i, bangun in enumerate(daftar_urut, 1):
    print(f"{i:<3} | {bangun.info():<25} | {bangun.volume():<12.2f} | {bangun.luas_permukaan():.2f}")

print("="*65)

# 4. Demonstrasi Operator Overloading
if daftar_bangun[0] > daftar_bangun[1]:
    print(f"\nInfo: {daftar_bangun[0].info()} lebih besar dari {daftar_bangun[1].info()}")

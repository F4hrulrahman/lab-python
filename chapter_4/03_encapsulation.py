"""
Chapter 4 - Bagian 3: Encapsulation
======================================
Encapsulation menyembunyikan detail internal dan membatasi akses langsung
ke atribut object.
"""

# ============================================
# 1. Public, Protected, Private
# ============================================
print("=== Public, Protected, Private ===")


class AkunBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik  # Public - bisa diakses dari mana saja
        self._bank = "Bank Python"  # Protected - konvensi: internal use
        self.__saldo = saldo  # Private - name mangling

    def info(self):
        return f"{self.pemilik} | {self._bank} | Saldo: Rp{self.__saldo:,.0f}"


akun = AkunBank("Budi", 5_000_000)

# Public - bebas diakses
print(f"Public  (pemilik): {akun.pemilik}")

# Protected - secara teknis masih bisa diakses, tapi sebaiknya tidak
print(f"Protected (_bank): {akun._bank}")

# Private - tidak bisa diakses langsung
try:
    print(akun.__saldo)
except AttributeError as e:
    print(f"Private (__saldo): Error - {e}")

# Name mangling: Python mengubah nama menjadi _ClassName__atribut
print(f"Name mangling (_AkunBank__saldo): {akun._AkunBank__saldo}")
print("  (Jangan gunakan ini! Ini melanggar prinsip encapsulation)")

# ============================================
# 2. Property Decorator (Getter/Setter)
# ============================================
print("\n=== Property Decorator ===")


class Suhu:
    """Class yang menyimpan suhu dalam Celsius dengan validasi."""

    def __init__(self, celsius=0):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):
        """Getter untuk celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter dengan validasi."""
        if value < -273.15:
            raise ValueError("Suhu tidak bisa di bawah -273.15°C (absolute zero)")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Property read-only: konversi ke Fahrenheit."""
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        """Property read-only: konversi ke Kelvin."""
        return self._celsius + 273.15

    def __str__(self):
        return f"{self._celsius}°C / {self.fahrenheit}°F / {self.kelvin}K"


suhu = Suhu(25)
print(f"Suhu awal: {suhu}")

# Menggunakan setter
suhu.celsius = 100
print(f"Setelah set 100°C: {suhu}")

# Validasi
try:
    suhu.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

# Fahrenheit read-only
try:
    suhu.fahrenheit = 72
except AttributeError as e:
    print(f"fahrenheit is read-only: {e}")

# ============================================
# 3. Contoh Praktis: Rekening Bank
# ============================================
print("\n=== Contoh: Rekening Bank ===")


class Rekening:
    """Rekening bank dengan encapsulation yang baik."""

    _jumlah_rekening = 0  # Class attribute (protected)

    def __init__(self, pemilik, saldo_awal=0):
        Rekening._jumlah_rekening += 1
        self._nomor = f"REK{Rekening._jumlah_rekening:04d}"
        self._pemilik = pemilik
        self.__saldo = saldo_awal
        self.__riwayat = [f"Saldo awal: Rp{saldo_awal:,.0f}"]

    @property
    def nomor(self):
        return self._nomor

    @property
    def pemilik(self):
        return self._pemilik

    @property
    def saldo(self):
        return self.__saldo

    @property
    def riwayat(self):
        return self.__riwayat.copy()  # Return copy agar list asli tidak diubah

    def setor(self, jumlah):
        """Menyetor uang ke rekening."""
        if jumlah <= 0:
            raise ValueError("Jumlah setor harus positif")
        self.__saldo += jumlah
        self.__riwayat.append(f"Setor: +Rp{jumlah:,.0f}")
        return self.__saldo

    def tarik(self, jumlah):
        """Menarik uang dari rekening."""
        if jumlah <= 0:
            raise ValueError("Jumlah tarik harus positif")
        if jumlah > self.__saldo:
            raise ValueError(f"Saldo tidak cukup (saldo: Rp{self.__saldo:,.0f})")
        self.__saldo -= jumlah
        self.__riwayat.append(f"Tarik: -Rp{jumlah:,.0f}")
        return self.__saldo

    def transfer(self, tujuan, jumlah):
        """Transfer uang ke rekening lain."""
        self.tarik(jumlah)
        tujuan.setor(jumlah)
        self.__riwayat.append(f"Transfer ke {tujuan.nomor}: -Rp{jumlah:,.0f}")
        tujuan.__dict__[f"_Rekening__riwayat"].append(
            f"Transfer dari {self.nomor}: +Rp{jumlah:,.0f}"
        )

    def __str__(self):
        return f"[{self._nomor}] {self._pemilik} - Saldo: Rp{self.__saldo:,.0f}"


# Membuat rekening
rek1 = Rekening("Budi", 10_000_000)
rek2 = Rekening("Ani", 5_000_000)

print(rek1)
print(rek2)

# Operasi
rek1.setor(2_000_000)
rek1.tarik(500_000)
rek1.transfer(rek2, 3_000_000)

print(f"\nSetelah transaksi:")
print(rek1)
print(rek2)

# Riwayat transaksi
print(f"\nRiwayat {rek1.pemilik}:")
for r in rek1.riwayat:
    print(f"  {r}")

print(f"\nRiwayat {rek2.pemilik}:")
for r in rek2.riwayat:
    print(f"  {r}")

# Validasi
print("\nValidasi:")
try:
    rek1.tarik(100_000_000)
except ValueError as e:
    print(f"  Error: {e}")

try:
    rek1.setor(-500)
except ValueError as e:
    print(f"  Error: {e}")

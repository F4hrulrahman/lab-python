"""
Chapter 4 - Bagian 1: Class & Object
=======================================
Class adalah blueprint untuk membuat object.
Object adalah instance dari class.
"""

# ============================================
# 1. Class Sederhana
# ============================================
print("=== Class Sederhana ===")


class Mahasiswa:
    """Class yang merepresentasikan seorang mahasiswa."""

    # Class attribute (milik semua instance)
    institusi = "Universitas Python"

    def __init__(self, nama, nim, jurusan):
        """Constructor - dipanggil saat membuat object baru."""
        # Instance attributes (milik masing-masing object)
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = []

    def tambah_nilai(self, nilai):
        """Menambahkan nilai ke daftar nilai mahasiswa."""
        self.nilai.append(nilai)

    def rata_rata(self):
        """Menghitung rata-rata nilai."""
        if not self.nilai:
            return 0
        return sum(self.nilai) / len(self.nilai)

    def info(self):
        """Menampilkan informasi mahasiswa."""
        return (
            f"Nama: {self.nama}, NIM: {self.nim}, "
            f"Jurusan: {self.jurusan}, IPK: {self.rata_rata():.2f}"
        )


# Membuat object (instance)
mhs1 = Mahasiswa("Budi Santoso", "2024001", "Informatika")
mhs2 = Mahasiswa("Ani Wijaya", "2024002", "Sistem Informasi")

# Menggunakan method
mhs1.tambah_nilai(85)
mhs1.tambah_nilai(90)
mhs1.tambah_nilai(78)

mhs2.tambah_nilai(92)
mhs2.tambah_nilai(88)

print(mhs1.info())
print(mhs2.info())

# Mengakses class attribute
print(f"\nInstitusi: {Mahasiswa.institusi}")
print(f"mhs1.institusi: {mhs1.institusi}")

# ============================================
# 2. __str__ dan __repr__
# ============================================
print("\n=== __str__ dan __repr__ ===")


class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        """Representasi string yang user-friendly (untuk print)."""
        return f"'{self.judul}' oleh {self.penulis} ({self.tahun})"

    def __repr__(self):
        """Representasi string yang unambiguous (untuk debugging)."""
        return f"Buku('{self.judul}', '{self.penulis}', {self.tahun})"


buku = Buku("Belajar Python", "John Doe", 2024)
print(f"str:  {buku}")  # Memanggil __str__
print(f"repr: {repr(buku)}")  # Memanggil __repr__

# ============================================
# 3. Method Khusus (Dunder Methods)
# ============================================
print("\n=== Dunder Methods ===")


class Vektor:
    """Class Vektor 2D dengan operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def __add__(self, other):
        """Operator +"""
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Operator -"""
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, skalar):
        """Operator * (perkalian skalar)"""
        return Vektor(self.x * skalar, self.y * skalar)

    def __eq__(self, other):
        """Operator =="""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Fungsi len() - mengembalikan magnitude (dibulatkan)"""
        return int((self.x**2 + self.y**2) ** 0.5)

    def magnitude(self):
        """Menghitung panjang vektor."""
        return (self.x**2 + self.y**2) ** 0.5


v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3  = {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vektor(3,4): {v1 == Vektor(3, 4)}")
print(f"Magnitude v1: {v1.magnitude():.2f}")

# ============================================
# 4. Class Method & Static Method
# ============================================
print("\n=== Class Method & Static Method ===")


class Lingkaran:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        """Instance method - butuh self."""
        return self.PI * self.radius**2

    def keliling(self):
        return 2 * self.PI * self.radius

    @classmethod
    def dari_diameter(cls, diameter):
        """Class method - menerima cls (class itu sendiri)."""
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(radius):
        """Static method - tidak butuh self atau cls."""
        return radius > 0

    def __str__(self):
        return f"Lingkaran(r={self.radius})"


# Instance method
l1 = Lingkaran(5)
print(f"{l1} -> Luas: {l1.luas():.2f}, Keliling: {l1.keliling():.2f}")

# Class method sebagai alternative constructor
l2 = Lingkaran.dari_diameter(10)
print(f"Dari diameter 10: {l2}")

# Static method
print(f"Radius 5 valid? {Lingkaran.is_valid_radius(5)}")
print(f"Radius -3 valid? {Lingkaran.is_valid_radius(-3)}")

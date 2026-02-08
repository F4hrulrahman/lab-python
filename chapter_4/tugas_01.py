"""
==========================================================
 TUGAS 1 - Sistem Perpustakaan
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Buku dengan atribut: judul, penulis, tahun, isbn, tersedia
 2. Implementasikan __str__ dan __repr__ pada class Buku
 3. Buat class Perpustakaan dengan atribut: nama, daftar_buku
 4. Implementasikan method: tambah_buku, cari_buku (pencarian parsial),
    pinjam_buku (by isbn), kembalikan_buku (by isbn), tampilkan_semua
 5. Buat minimal 5 objek Buku dan demonstrasikan semua method

 Konsep yang dipelajari:
 - Membuat class dan __init__
 - Method __str__ dan __repr__
 - Atribut instance dan default value
 - Interaksi antar objek (Perpustakaan memiliki list Buku)
==========================================================
"""


class Buku:
    """Representasi sebuah buku di perpustakaan.

    Attributes:
        judul (str): Judul buku.
        penulis (str): Nama penulis buku.
        tahun (int): Tahun terbit buku.
        isbn (str): Nomor ISBN buku (unik).
        tersedia (bool): Status ketersediaan buku (default True).
    """

    def __init__(self, judul, penulis, tahun, isbn):
        """Inisialisasi objek Buku.

        Args:
            judul (str): Judul buku.
            penulis (str): Nama penulis.
            tahun (int): Tahun terbit.
            isbn (str): Nomor ISBN.
        """
        # TODO: Inisialisasi semua atribut
        # Hint: self.tersedia default-nya True (buku baru selalu tersedia)
        ...

    def __str__(self):
        """Representasi string yang mudah dibaca.

        Returns:
            str: Contoh -> "Python Dasar oleh John (2023) [Tersedia]"
        """
        # TODO: Implementasikan
        # Hint: gunakan "Tersedia" jika self.tersedia else "Dipinjam"
        ...

    def __repr__(self):
        """Representasi resmi untuk debugging.

        Returns:
            str: Contoh -> "Buku('Python Dasar', 'John', 2023, '978-123')"
        """
        # TODO: Implementasikan
        # Hint: return f"Buku('{self.judul}', '{self.penulis}', {self.tahun}, '{self.isbn}')"
        ...


class Perpustakaan:
    """Sistem manajemen perpustakaan sederhana.

    Attributes:
        nama (str): Nama perpustakaan.
        daftar_buku (list): Koleksi objek Buku.
    """

    def __init__(self, nama):
        """Inisialisasi perpustakaan.

        Args:
            nama (str): Nama perpustakaan.
        """
        # TODO: Inisialisasi atribut nama dan daftar_buku (list kosong)
        ...

    def tambah_buku(self, buku):
        """Menambahkan buku ke koleksi perpustakaan.

        Args:
            buku (Buku): Objek Buku yang akan ditambahkan.
        """
        # TODO: Tambahkan buku ke daftar_buku
        # Hint: cek apakah ISBN sudah ada untuk menghindari duplikasi
        ...

    def cari_buku(self, kata_kunci):
        """Mencari buku berdasarkan kata kunci (pencarian parsial).

        Pencarian dilakukan pada judul dan penulis (case-insensitive).

        Args:
            kata_kunci (str): Kata kunci pencarian.

        Returns:
            list: Daftar objek Buku yang cocok.
        """
        # TODO: Implementasikan pencarian parsial
        # Hint: gunakan 'in' operator dan .lower() untuk case-insensitive
        # Contoh: [b for b in self.daftar_buku if kata_kunci.lower() in b.judul.lower()]
        ...

    def pinjam_buku(self, isbn):
        """Meminjam buku berdasarkan ISBN.

        Args:
            isbn (str): Nomor ISBN buku yang akan dipinjam.

        Returns:
            str: Pesan berhasil/gagal meminjam.
        """
        # TODO: Implementasikan logika peminjaman
        # 1. Cari buku berdasarkan ISBN
        # 2. Cek apakah buku tersedia (tersedia == True)
        # 3. Jika tersedia, ubah status menjadi False
        # 4. Jika tidak tersedia atau tidak ditemukan, tampilkan pesan
        ...

    def kembalikan_buku(self, isbn):
        """Mengembalikan buku berdasarkan ISBN.

        Args:
            isbn (str): Nomor ISBN buku yang akan dikembalikan.

        Returns:
            str: Pesan berhasil/gagal mengembalikan.
        """
        # TODO: Implementasikan logika pengembalian
        # 1. Cari buku berdasarkan ISBN
        # 2. Cek apakah buku sedang dipinjam (tersedia == False)
        # 3. Jika sedang dipinjam, ubah status menjadi True
        # 4. Jika sudah tersedia atau tidak ditemukan, tampilkan pesan
        ...

    def tampilkan_semua(self):
        """Menampilkan semua buku dalam format tabel.

        Contoh output:
        ============================================================
        No | Judul               | Penulis        | Tahun | Status
        ------------------------------------------------------------
         1 | Python Dasar        | John Doe       |  2023 | Tersedia
         2 | Data Science        | Jane Smith     |  2022 | Dipinjam
        ============================================================
        """
        # TODO: Implementasikan tampilan tabel
        # Hint: gunakan f-string dengan format alignment
        # f"{i:>2} | {b.judul:<20} | {b.penulis:<15} | {b.tahun:>5} | {status}"
        ...


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Buat minimal 5 objek Buku
    # buku1 = Buku("Python Dasar", "Guido van Rossum", 2023, "978-001")
    # buku2 = Buku("Data Science dengan Python", "Jake VanderPlas", 2022, "978-002")
    # buku3 = Buku("Machine Learning", "Andrew Ng", 2021, "978-003")
    # buku4 = Buku("Algoritma & Pemrograman", "Thomas Cormen", 2020, "978-004")
    # buku5 = Buku("Artificial Intelligence", "Stuart Russell", 2019, "978-005")

    # TODO: Buat objek Perpustakaan
    # perpus = Perpustakaan("Perpustakaan Unismuh Makassar")

    # TODO: Tambahkan semua buku ke perpustakaan
    # for buku in [buku1, buku2, buku3, buku4, buku5]:
    #     perpus.tambah_buku(buku)

    # TODO: Tampilkan semua buku
    # print("=== DAFTAR BUKU ===")
    # perpus.tampilkan_semua()

    # TODO: Cari buku
    # print("\n=== CARI BUKU: 'python' ===")
    # hasil = perpus.cari_buku("python")
    # for buku in hasil:
    #     print(f"  - {buku}")

    # TODO: Pinjam buku
    # print("\n=== PINJAM BUKU ===")
    # print(perpus.pinjam_buku("978-001"))
    # print(perpus.pinjam_buku("978-001"))  # coba pinjam lagi (sudah dipinjam)

    # TODO: Tampilkan setelah peminjaman
    # print("\n=== DAFTAR BUKU (setelah peminjaman) ===")
    # perpus.tampilkan_semua()

    # TODO: Kembalikan buku
    # print("\n=== KEMBALIKAN BUKU ===")
    # print(perpus.kembalikan_buku("978-001"))

    # TODO: Test __repr__
    # print("\n=== REPR ===")
    # print(repr(buku1))

    pass

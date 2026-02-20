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


# Tugas 1 -- Sistem Perpustakaan (tugas_01.py)

class Buku:
    # Implementasi class Buku dengan atribut yang diminta
    def __init__(self, judul, penulis, tahun, isbn):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.isbn = isbn
        self.tersedia = True  # Default tersedia

    # Implementasi __str__ untuk tampilan user-friendly
    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} oleh {self.penulis} ({status})"

    # Implementasi __repr__ untuk keperluan debugging/internal
    def __repr__(self):
        return f"Buku('{self.judul}', '{self.isbn}')"

class Perpustakaan:
    # Implementasi class Perpustakaan
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def cari_buku(self, judul):
        print(f"\n--- Hasil Pencarian Judul: '{judul}' ---")
        hasil = [b for b in self.daftar_buku if judul.lower() in b.judul.lower()]
        if not hasil:
            print("Buku tidak ditemukan.")
        else:
            for b in hasil:
                print(f"- {b}")

    def pinjam_buku(self, isbn):
        for b in self.daftar_buku:
            if b.isbn == isbn:
                if b.tersedia:
                    b.tersedia = False
                    print(f"\nBerhasil meminjam: {b.judul}")
                    return
                else:
                    print(f"\nMaaf, buku '{b.judul}' sedang dipinjam.")
                    return
        print("\nISBN tidak ditemukan.")

    def kembalikan_buku(self, isbn):
        for b in self.daftar_buku:
            if b.isbn == isbn:
                b.tersedia = True
                print(f"\nBerhasil mengembalikan: {b.judul}")
                return
        print("\nISBN tidak ditemukan.")

    def tampilkan_semua(self):
        print(f"\n{'='*12} {self.nama.upper()} {'='*12}")
        print(f"{'No':<2} | {'Judul':<22} | {'Penulis':<15} | {'Tahun':<5} | {'Status'}")
        print(f"{'-'*3}+{'-'*24}+{'-'*17}+{'-'*7}+{'-'*10}")
        
        tersedia_count = 0
        for i, b in enumerate(self.daftar_buku, 1):
            status = "Tersedia" if b.tersedia else "Dipinjam"
            if b.tersedia: tersedia_count += 1
            print(f"{i:<2} | {b.judul[:22]:<22} | {b.penulis[:15]:<15} | {b.tahun:<5} | {status}")
        
        print(f"{'='*55}")
        print(f"Total: {len(self.daftar_buku)} buku | Tersedia: {tersedia_count} | Dipinjam: {len(self.daftar_buku) - tersedia_count}")

# --- Demonstrasi Sistem Perpustakaan ---

# Buat objek Perpustakaan
perpus = Perpustakaan("Perpustakaan Unismuh Makassar")

# Tambahkan 5 objek buku
perpus.tambah_buku(Buku("Algoritma & Pemrograman", "Rinaldi Munir", 2016, "978-1"))
perpus.tambah_buku(Buku("Basis Data", "Fathansyah", 2018, "978-2"))
perpus.tambah_buku(Buku("Machine Learning", "Tom Mitchell", 2020, "978-3"))
perpus.tambah_buku(Buku("Clean Code", "Robert Martin", 2008, "978-4"))
perpus.tambah_buku(Buku("Python for Data Science", "Jake VanderPlas", 2016, "978-5"))

# Demonstrasi method
perpus.tampilkan_semua()
perpus.pinjam_buku("978-2") # Pinjam Basis Data
perpus.pinjam_buku("978-3") # Pinjam Machine Learning
perpus.tampilkan_semua()
perpus.cari_buku("Python")
perpus.kembalikan_buku("978-2")
perpus.tampilkan_semua()

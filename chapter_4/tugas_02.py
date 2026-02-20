"""
==========================================================
 TUGAS 2 - Sistem Akademik dengan Inheritance
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Orang (parent) dengan atribut: nama, umur, alamat
 2. Buat class Mahasiswa(Orang) dengan atribut: nim, jurusan, semester,
    daftar_mk; method: tambah_mk, hitung_ipk, info (override)
 3. Buat class Dosen(Orang) dengan atribut: nidn, bidang_keahlian,
    daftar_mk_diampu; method: tambah_mk_diampu, info (override)
 4. Buat class Asisten(Mahasiswa) dengan atribut: lab, dosen_pembimbing
 5. Demonstrasikan polymorphism, isinstance(), dan issubclass()

 Konsep yang dipelajari:
 - Inheritance (pewarisan) single & multilevel
 - Method overriding
 - super() untuk memanggil parent constructor
 - Polymorphism (method yang sama, perilaku berbeda)
 - isinstance() dan issubclass()
==========================================================
"""


# Tugas 2 -- Sistem Akademik dengan Inheritance (tugas_02.py)

# Class Induk Orang
class Orang:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def info(self):
        return f"Nama: {self.nama} | Umur: {self.umur} | Alamat: {self.alamat}"

# Class Mahasiswa (Turunan Orang)
class Mahasiswa(Orang):
    def __init__(self, nama, umur, alamat, nim, jurusan, semester):
        super().__init__(nama, umur, alamat)
        self.nim = nim
        self.jurusan = jurusan
        self.semester = semester
        self.daftar_mk = []

    def tambah_mk(self, mata_kuliah, nilai):
        self.daftar_mk.append({"mata_kuliah": mata_kuliah, "nilai": nilai})

    def hitung_ipk(self):
        if not self.daftar_mk:
            return 0.0
        total_nilai = sum(item['nilai'] for item in self.daftar_mk)
        return total_nilai / len(self.daftar_mk)

    def info(self):
        return f"[Mahasiswa] NIM: {self.nim} | {self.nama} | Jurusan: {self.jurusan} | IPK: {self.hitung_ipk():.2f}"

# Class Dosen (Turunan Orang)
class Dosen(Orang):
    def __init__(self, nama, umur, alamat, nidn, bidang):
        super().__init__(nama, umur, alamat)
        self.nidn = nidn
        self.bidang = bidang
        self.daftar_mk_diampu = []

    def tambah_mk_diampu(self, mata_kuliah):
        self.daftar_mk_diampu.append(mata_kuliah)

    def info(self):
        return f"[Dosen] NIDN: {self.nidn} | {self.nama} | Keahlian: {self.bidang}"

# Class Asisten (Turunan Mahasiswa)
class Asisten(Mahasiswa):
    def __init__(self, nama, umur, alamat, nim, jurusan, semester, lab, dosen_pembimbing):
        super().__init__(nama, umur, alamat, nim, jurusan, semester)
        self.lab = lab
        self.dosen_pembimbing = dosen_pembimbing

    def info(self):
        # Menggabungkan info Mahasiswa dengan info Lab
        info_mhs = super().info()
        return f"{info_mhs} | [Asisten Lab: {self.lab}]"

# --- Demonstrasi ---

# Inisialisasi Objek
mhs1 = Mahasiswa("Safriamsah", 22, "Makassar", "10584110", "Informatika", 8)
mhs1.tambah_mk("Data Mining", 85)
mhs1.tambah_mk("Machine Learning", 90)

dsn1 = Dosen("Dr. Ahmad", 45, "Jl. Sultan Alauddin", "0912345", "Kecerdasan Buatan")
dsn1.tambah_mk_diampu("Pemrograman Python")

ast1 = Asisten("Ciko", 20, "Lab Unismuh", "10584111", "Informatika", 4, "Lab Robotik", dsn1.nama)

# Demonstrasi Polymorphism
print("===== DEMONSTRASI POLYMORPHISM =====")
civitas_akademika = [mhs1, dsn1, ast1]

for orang in civitas_akademika:
    print(orang.info())

# Demonstrasi isinstance() dan issubclass()
print("\n===== CEK RELASI CLASS =====")
print(f"Apakah ast1 adalah Mahasiswa? {isinstance(ast1, Mahasiswa)}")
print(f"Apakah Asisten adalah sub-class dari Orang? {issubclass(Asisten, Orang)}")
print(f"Apakah Dosen adalah sub-class dari Mahasiswa? {issubclass(Dosen, Mahasiswa)}")
    pass

<div align="center">

# Chapter 4: Object-Oriented Programming (OOP)

**Modul Praktikum Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

---

## Tujuan Praktikum

Setelah menyelesaikan chapter ini, praktikan diharapkan mampu:

1. Mendefinisikan **class** dan membuat **object** (instance)
2. Mengimplementasikan **constructor** (`__init__`) dan **method**
3. Menerapkan **inheritance** (pewarisan) dan **method overriding**
4. Memahami dan menerapkan prinsip **encapsulation** (public, protected, private)
5. Menggunakan **property decorator** sebagai getter/setter

---

## Landasan Teori

### Pilar OOP

| Pilar | Deskripsi | Contoh |
|-------|-----------|--------|
| **Encapsulation** | Menyembunyikan data internal, akses melalui method | Private attribute + property |
| **Inheritance** | Class baru mewarisi sifat class yang sudah ada | `class Kucing(Hewan)` |
| **Polymorphism** | Method yang sama berperilaku berbeda di class berbeda | Override method `suara()` |
| **Abstraction** | Menyembunyikan kompleksitas, tampilkan antarmuka sederhana | Method publik tanpa detail |

### Konvensi Akses Atribut

| Prefix | Jenis | Akses | Contoh |
|--------|-------|-------|--------|
| *(tanpa)* | Public | Bebas dari mana saja | `self.nama` |
| `_` | Protected | Konvensi internal, jangan akses dari luar | `self._data` |
| `__` | Private | Name mangling, tidak bisa akses langsung | `self.__saldo` |

---

## File Praktikum

| No | File | Topik |
|:--:|------|-------|
| 1 | `01_class_object.py` | Class, `__init__`, dunder methods, classmethod, staticmethod |
| 2 | `02_inheritance.py` | Single/multiple inheritance, polymorphism, MRO |
| 3 | `03_encapsulation.py` | Public/protected/private, property, getter/setter |

### Cara Menjalankan

```bash
python chapter_4/01_class_object.py
python chapter_4/02_inheritance.py
python chapter_4/03_encapsulation.py
```

---

## Tugas Praktikum

Kerjakan seluruh tugas berikut sebagai bahan laporan praktikum. Buat file Python baru di dalam folder `chapter_4/` untuk setiap tugas.

### Tugas 1 -- Sistem Perpustakaan (`tugas_01.py`)

Implementasikan sistem perpustakaan sederhana menggunakan OOP.

- [ ] Buat class `Buku` dengan atribut: `judul`, `penulis`, `tahun`, `isbn`, `tersedia` (bool)
- [ ] Implementasikan `__init__`, `__str__`, dan `__repr__`
- [ ] Buat class `Perpustakaan` dengan atribut: `nama`, `daftar_buku` (list)
- [ ] Implementasikan method di `Perpustakaan`:
  - `tambah_buku(buku)` -- menambahkan buku ke koleksi
  - `cari_buku(judul)` -- mencari buku berdasarkan judul (partial match)
  - `pinjam_buku(isbn)` -- mengubah status buku jadi tidak tersedia
  - `kembalikan_buku(isbn)` -- mengubah status buku jadi tersedia
  - `tampilkan_semua()` -- menampilkan semua buku dalam format tabel
- [ ] Buat minimal 5 objek buku dan demonstrasikan semua method

**Contoh Output:**
```
============ PERPUSTAKAAN UNISMUH MAKASSAR ============
No | Judul                 | Penulis        | Tahun | Status
---+-----------------------+----------------+-------+----------
 1 | Algoritma & Pemrograman| Rinaldi Munir | 2016  | Tersedia
 2 | Basis Data            | Fathansyah     | 2018  | Dipinjam
 3 | Machine Learning      | Tom Mitchell   | 2020  | Tersedia
...
=======================================================
Total: 5 buku | Tersedia: 3 | Dipinjam: 2
```

---

### Tugas 2 -- Sistem Akademik dengan Inheritance (`tugas_02.py`)

- [ ] Buat class **induk** `Orang` dengan atribut: `nama`, `umur`, `alamat`
- [ ] Buat class `Mahasiswa` (turunan `Orang`) dengan atribut tambahan: `nim`, `jurusan`, `semester`, `daftar_mk` (list of dict: `{mata_kuliah, nilai}`)
- [ ] Buat class `Dosen` (turunan `Orang`) dengan atribut tambahan: `nidn`, `bidang_keahlian`, `daftar_mk_diampu` (list)
- [ ] Buat class `Asisten` (turunan `Mahasiswa`) dengan atribut tambahan: `lab`, `dosen_pembimbing`
- [ ] Implementasikan method di `Mahasiswa`:
  - `tambah_mk(mata_kuliah, nilai)` -- menambah mata kuliah dan nilai
  - `hitung_ipk()` -- menghitung rata-rata nilai
  - `info()` -- menampilkan seluruh informasi (override dari parent)
- [ ] Implementasikan method di `Dosen`:
  - `tambah_mk_diampu(mata_kuliah)` -- menambah MK yang diampu
  - `info()` -- menampilkan seluruh informasi (override)
- [ ] Demonstrasikan **polymorphism** dengan membuat list campuran (Mahasiswa + Dosen + Asisten) dan panggil `info()` pada setiap elemen
- [ ] Demonstrasikan `isinstance()` dan `issubclass()`

---

### Tugas 3 -- Sistem Keuangan dengan Encapsulation (`tugas_03.py`)

- [ ] Buat class `Rekening` dengan:
  - **Private** attribute: `__saldo`, `__pin`, `__riwayat_transaksi`
  - **Protected** attribute: `_nomor_rekening`, `_pemilik`
  - **Public** attribute: `bank`
- [ ] Gunakan **`@property`** untuk membuat getter `saldo` (read-only, tidak boleh diubah langsung)
- [ ] Gunakan **`@property`** untuk `pemilik` dengan setter yang memvalidasi (nama tidak boleh kosong)
- [ ] Implementasikan method:
  - `setor(jumlah, pin)` -- setor dengan validasi pin
  - `tarik(jumlah, pin)` -- tarik dengan validasi pin dan cek saldo
  - `transfer(tujuan, jumlah, pin)` -- transfer ke rekening lain
  - `cek_riwayat(pin)` -- tampilkan riwayat transaksi (harus validasi pin)
  - `ganti_pin(pin_lama, pin_baru)` -- ganti pin dengan validasi
- [ ] Demonstrasikan bahwa atribut private tidak bisa diakses langsung (gunakan try-except)
- [ ] Buat minimal 2 objek rekening dan demonstrasikan seluruh operasi

**Contoh Output:**
```
===== SISTEM KEUANGAN =====
[REK-0001] Budi Santoso - Bank Unismuh

Setor Rp2,000,000 ... Berhasil! Saldo: Rp7,000,000
Tarik Rp500,000 ... Berhasil! Saldo: Rp6,500,000
Transfer ke REK-0002 Rp1,000,000 ... Berhasil!

Akses langsung __saldo: Error - 'Rekening' object has no attribute '__saldo'

--- Riwayat Transaksi REK-0001 ---
  [2024-01-15] Saldo awal: Rp5,000,000
  [2024-01-15] Setor: +Rp2,000,000
  [2024-01-15] Tarik: -Rp500,000
  [2024-01-15] Transfer ke REK-0002: -Rp1,000,000
```

---

### Tugas 4 -- Class Bangun Ruang (`tugas_04.py`)

- [ ] Buat class **induk** `BangunRuang` dengan method abstrak: `volume()`, `luas_permukaan()`, `info()`
- [ ] Buat class turunan: `Kubus`, `Balok`, `Tabung`, `Bola`
- [ ] Setiap class turunan mengimplementasikan `volume()` dan `luas_permukaan()` sesuai rumusnya
- [ ] Gunakan `@classmethod` sebagai alternative constructor (misal: `Kubus.dari_volume(vol)`)
- [ ] Gunakan `@staticmethod` untuk validasi (misal: `Kubus.is_valid(sisi)`)
- [ ] Overload operator `__gt__` untuk membandingkan volume antar bangun ruang
- [ ] Buat list berisi berbagai bangun ruang, lalu urutkan berdasarkan volume (gunakan `sorted` + `lambda`)
- [ ] Tampilkan hasil dalam format tabel

---

## Checklist Laporan

- [ ] Semua tugas (Tugas 1 s/d 4) telah dikerjakan
- [ ] Setiap file dapat dijalankan tanpa error
- [ ] Menerapkan `__init__`, `__str__` pada semua class
- [ ] Demonstrasi **inheritance** dan **method overriding** minimal di 1 tugas
- [ ] Demonstrasi **encapsulation** (private/protected + property) minimal di 1 tugas
- [ ] Demonstrasi **polymorphism** minimal di 1 tugas
- [ ] Kode ditulis rapi dengan docstring pada setiap class dan method
- [ ] Screenshot output program dilampirkan dalam laporan

---

<div align="center">

**Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

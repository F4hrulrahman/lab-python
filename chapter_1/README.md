<div align="center">

# Chapter 1: Dasar Python

**Modul Praktikum Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

---

## Tujuan Praktikum

Setelah menyelesaikan chapter ini, praktikan diharapkan mampu:

1. Mendeklarasikan dan menggunakan variabel dengan penamaan yang benar
2. Memahami dan membedakan tipe data dasar Python (`int`, `float`, `str`, `bool`, `None`)
3. Melakukan konversi tipe data (type casting)
4. Menggunakan berbagai jenis operator dalam Python

---

## Landasan Teori

### Variabel
Variabel adalah nama yang merujuk ke suatu nilai di memori. Python menggunakan *dynamic typing*, sehingga tipe data ditentukan secara otomatis saat assignment.

### Tipe Data
Python memiliki beberapa tipe data bawaan:

| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| `int` | Bilangan bulat | `42`, `-10`, `1_000` |
| `float` | Bilangan desimal | `3.14`, `2.5e3` |
| `str` | Teks/string | `"hello"`, `'world'` |
| `bool` | Boolean | `True`, `False` |
| `None` | Nilai kosong | `None` |

### Operator
| Kategori | Operator | Contoh |
|----------|----------|--------|
| Aritmatika | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `10 + 5` |
| Perbandingan | `==`, `!=`, `>`, `<`, `>=`, `<=` | `x > 5` |
| Logika | `and`, `or`, `not` | `True and False` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=` | `x += 1` |
| Identitas | `is`, `is not` | `x is None` |
| Keanggotaan | `in`, `not in` | `'a' in 'abc'` |

---

## File Praktikum

| No | File | Topik |
|:--:|------|-------|
| 1 | `01_variabel.py` | Deklarasi variabel, penamaan, multiple assignment, konstanta |
| 2 | `02_tipe_data.py` | Tipe data bawaan, truthy/falsy, type casting |
| 3 | `03_operator.py` | Operator aritmatika, perbandingan, logika, prioritas |

### Cara Menjalankan

```bash
python chapter_1/01_variabel.py
python chapter_1/02_tipe_data.py
python chapter_1/03_operator.py
```

> Jalankan setiap file, amati output-nya, dan pahami setiap baris kode sebelum mengerjakan tugas.

---

## Tugas Praktikum

Kerjakan seluruh tugas berikut sebagai bahan laporan praktikum. Buat file Python baru di dalam folder `chapter_1/` untuk setiap tugas.

### Tugas 1 -- Biodata Mahasiswa (`tugas_01.py`)

- [ ] Buat variabel yang menyimpan: nama lengkap, NIM, jurusan, semester (int), IPK (float), dan status aktif (bool)
- [ ] Tampilkan semua data menggunakan f-string dengan format rapi
- [ ] Tampilkan tipe data dari setiap variabel menggunakan `type()`
- [ ] Gunakan `isinstance()` untuk memeriksa apakah NIM bertipe `str` dan semester bertipe `int`

**Contoh Output:**
```
===== BIODATA MAHASISWA =====
Nama    : Ahmad Fauzi
NIM     : 105841100123
Jurusan : Informatika
Semester: 4
IPK     : 3.75
Aktif   : True
=============================
Tipe 'nama'    : <class 'str'>
Tipe 'semester': <class 'int'>
...
```

---

### Tugas 2 -- Kalkulator Konversi Suhu (`tugas_02.py`)

- [ ] Definisikan variabel `celsius` dengan nilai tertentu
- [ ] Hitung konversi ke Fahrenheit: `F = (C x 9/5) + 32`
- [ ] Hitung konversi ke Reamur: `R = C x 4/5`
- [ ] Hitung konversi ke Kelvin: `K = C + 273.15`
- [ ] Tampilkan semua hasil konversi dengan 2 angka desimal
- [ ] Uji dengan minimal 3 nilai celsius berbeda (gunakan variabel, bukan input)

---

### Tugas 3 -- Operator & Ekspresi (`tugas_03.py`)

- [ ] Buat dua variabel bilangan bulat `a` dan `b`
- [ ] Tampilkan hasil semua operator aritmatika (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- [ ] Buat variabel boolean berdasarkan hasil perbandingan `a` dan `b`
- [ ] Demonstrasikan penggunaan operator logika (`and`, `or`, `not`) dengan minimal 3 ekspresi berbeda
- [ ] Buat sebuah list dan demonstrasikan operator `in` dan `not in`
- [ ] Tunjukkan perbedaan `==` dan `is` menggunakan contoh list

---

### Tugas 4 -- Menghitung Luas & Keliling Bangun Datar (`tugas_04.py`)

- [ ] Buat variabel untuk menyimpan dimensi: persegi, persegi panjang, lingkaran, dan segitiga
- [ ] Hitung luas dan keliling masing-masing bangun datar
- [ ] Gunakan konstanta `PI = 3.14159` untuk lingkaran
- [ ] Tampilkan hasil perhitungan dalam format tabel yang rapi
- [ ] Gunakan operator assignment (`+=`) untuk menghitung total luas semua bangun

**Contoh Output:**
```
============ LUAS & KELILING BANGUN DATAR ============
Bangun            |    Luas   |  Keliling
--------------------------------------------------
Persegi           |     25.00 |     20.00
Persegi Panjang   |     40.00 |     26.00
Lingkaran         |     78.54 |     31.42
Segitiga          |     24.00 |     24.00
--------------------------------------------------
Total Luas        |    167.54
======================================================
```

---

## Checklist Laporan

Pastikan laporan praktikum memenuhi seluruh poin berikut:

- [ ] Semua tugas (Tugas 1 s/d 4) telah dikerjakan
- [ ] Setiap file dapat dijalankan tanpa error
- [ ] Output program sesuai dengan format yang diminta
- [ ] Kode menggunakan penamaan variabel yang deskriptif (snake_case)
- [ ] Setiap file memiliki komentar penjelasan di bagian atas
- [ ] Screenshot output program dilampirkan dalam laporan

---

<div align="center">

**Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

<div align="center">

# Chapter 3: Control Flow & Fungsi

**Modul Praktikum Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

---

## Tujuan Praktikum

Setelah menyelesaikan chapter ini, praktikan diharapkan mampu:

1. Mengimplementasikan percabangan (`if`, `elif`, `else`) untuk pengambilan keputusan
2. Menggunakan perulangan (`for`, `while`) untuk proses iteratif
3. Mengendalikan alur loop dengan `break`, `continue`, dan `pass`
4. Membuat fungsi yang reusable dengan berbagai jenis parameter
5. Menggunakan lambda function dan fungsi higher-order (`map`, `filter`)

---

## Landasan Teori

### Percabangan

```python
if kondisi:
    # blok kode jika True
elif kondisi_lain:
    # blok kode alternatif
else:
    # blok kode jika semua False
```

### Perulangan

| Jenis | Digunakan Ketika |
|-------|-----------------|
| `for` | Jumlah iterasi sudah diketahui / iterasi koleksi |
| `while` | Iterasi sampai kondisi tertentu terpenuhi |

### Fungsi

```python
def nama_fungsi(param1, param2="default"):
    """Docstring penjelasan fungsi."""
    # proses
    return hasil
```

| Konsep | Penjelasan |
|--------|-----------|
| `*args` | Menerima argumen posisional tak terbatas sebagai tuple |
| `**kwargs` | Menerima keyword argument tak terbatas sebagai dictionary |
| `lambda` | Fungsi anonim satu baris: `lambda x: x * 2` |
| `scope` | Variabel lokal hanya ada di dalam fungsi |

---

## File Praktikum

| No | File | Topik |
|:--:|------|-------|
| 1 | `01_percabangan.py` | if/elif/else, ternary, nested if, match-case |
| 2 | `02_perulangan.py` | for, while, break/continue, enumerate, zip |
| 3 | `03_fungsi.py` | def, parameter, return, *args, **kwargs, lambda, rekursi |

### Cara Menjalankan

```bash
python chapter_3/01_percabangan.py
python chapter_3/02_perulangan.py
python chapter_3/03_fungsi.py
```

---

## Tugas Praktikum

Kerjakan seluruh tugas berikut sebagai bahan laporan praktikum. Buat file Python baru di dalam folder `chapter_3/` untuk setiap tugas.

### Tugas 1 -- Sistem Penilaian Akademik (`tugas_01.py`)

- [ ] Buat **fungsi** `hitung_grade(nilai)` yang menerima nilai angka (0-100) dan mengembalikan grade berdasarkan ketentuan berikut:

| Rentang Nilai | Grade | Keterangan |
|:------------:|:-----:|-----------|
| 90 - 100 | A | Sangat Baik |
| 80 - 89 | B | Baik |
| 70 - 79 | C | Cukup |
| 60 - 69 | D | Kurang |
| 0 - 59 | E | Sangat Kurang |

- [ ] Buat **fungsi** `status_kelulusan(grade)` yang mengembalikan "LULUS" jika grade A/B/C, dan "TIDAK LULUS" jika D/E
- [ ] Buat list berisi 10 nama mahasiswa dan nilainya (gunakan list of tuple)
- [ ] Gunakan **perulangan** untuk memproses semua mahasiswa, tampilkan hasilnya dalam format tabel
- [ ] Hitung dan tampilkan: jumlah yang lulus, tidak lulus, dan persentasenya
- [ ] Gunakan **ternary operator** minimal 1 kali dalam program

**Contoh Output:**
```
================== HASIL PENILAIAN AKADEMIK ==================
No | Nama              | Nilai | Grade | Keterangan    | Status
---+-------------------+-------+-------+---------------+-----------
 1 | Ahmad Fauzi       |    85 |   B   | Baik          | LULUS
 2 | Siti Rahma        |    92 |   A   | Sangat Baik   | LULUS
 3 | Budi Santoso      |    55 |   E   | Sangat Kurang | TIDAK LULUS
...
==============================================================
Lulus: 7 (70.0%) | Tidak Lulus: 3 (30.0%)
```

---

### Tugas 2 -- Pola & Deret (`tugas_02.py`)

- [ ] Buat **fungsi** `pola_segitiga(n)` yang mencetak pola segitiga bintang dengan tinggi `n`
- [ ] Buat **fungsi** `pola_segitiga_terbalik(n)` yang mencetak pola segitiga terbalik
- [ ] Buat **fungsi** `pola_diamond(n)` yang mencetak pola diamond/berlian
- [ ] Buat **fungsi** `deret_fibonacci(n)` yang mengembalikan list berisi `n` bilangan Fibonacci
- [ ] Buat **fungsi** `is_prima(n)` yang mengembalikan `True` jika `n` bilangan prima
- [ ] Tampilkan semua bilangan prima antara 1 sampai 100 menggunakan `filter()` dan `is_prima`

**Contoh Output Pola Diamond (n=5):**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

### Tugas 3 -- Kalkulator Serbaguna (`tugas_03.py`)

- [ ] Buat **fungsi** `kalkulator(a, b, operasi="+")` dengan default parameter
- [ ] Operasi yang didukung: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- [ ] Tangani pembagian dengan nol menggunakan percabangan
- [ ] Buat **fungsi** `statistik(*args)` menggunakan `*args` yang mengembalikan dict berisi: `min`, `max`, `sum`, `mean`, `count`
- [ ] Buat **fungsi** `format_output(**kwargs)` menggunakan `**kwargs` yang mencetak data dalam format `key: value` yang rapi
- [ ] Demonstrasikan penggunaan `lambda` dengan `map()` untuk menghitung kuadrat dari sebuah list
- [ ] Demonstrasikan penggunaan `lambda` dengan `filter()` untuk menyaring bilangan genap
- [ ] Demonstrasikan penggunaan `lambda` dengan `sorted()` untuk mengurutkan list of tuple berdasarkan elemen tertentu

---

### Tugas 4 -- Permainan Tebak Angka (`tugas_04.py`)

- [ ] Buat fungsi yang menghasilkan angka acak 1-100 (gunakan `import random`)
- [ ] Buat **while loop** yang meminta user menebak angka tersebut (gunakan `input()`)
- [ ] Berikan petunjuk "Terlalu besar!" atau "Terlalu kecil!" setiap tebakan salah
- [ ] Hitung dan tampilkan jumlah percobaan saat berhasil menebak
- [ ] Gunakan **break** untuk keluar dari loop saat tebakan benar
- [ ] Tambahkan batas maksimal 10 percobaan, jika gagal tampilkan "Game Over" dan jawaban yang benar
- [ ] Buat **fungsi rekursif** `tebak_rekursif(target, percobaan)` sebagai alternatif versi rekursif

> **Catatan:** Tugas ini bersifat interaktif (menggunakan `input()`). Sertakan screenshot saat menjalankan program.

---

## Checklist Laporan

- [ ] Semua tugas (Tugas 1 s/d 4) telah dikerjakan
- [ ] Setiap file dapat dijalankan tanpa error
- [ ] Setiap tugas menggunakan **fungsi** (bukan kode prosedural tanpa fungsi)
- [ ] Demonstrasi `*args`, `**kwargs`, dan `lambda` minimal di 1 tugas
- [ ] Output program sesuai dengan format yang diminta
- [ ] Kode ditulis rapi dengan komentar dan docstring pada setiap fungsi
- [ ] Screenshot output program dilampirkan dalam laporan

---

<div align="center">

**Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

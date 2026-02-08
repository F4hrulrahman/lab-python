<div align="center">

# Chapter 2: Struktur Data

**Modul Praktikum Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

---

## Tujuan Praktikum

Setelah menyelesaikan chapter ini, praktikan diharapkan mampu:

1. Membuat dan memanipulasi **List** beserta method-method-nya
2. Memahami perbedaan **Tuple** dan List (immutability)
3. Menggunakan **Dictionary** untuk menyimpan data key-value
4. Memanfaatkan **Set** untuk operasi himpunan
5. Menentukan struktur data yang tepat untuk suatu permasalahan

---

## Landasan Teori

### Perbandingan Struktur Data

| Fitur | List `[]` | Tuple `()` | Dictionary `{}` | Set `{}` |
|-------|:---------:|:----------:|:----------------:|:--------:|
| Ordered | Ya | Ya | Ya (3.7+) | Tidak |
| Mutable | Ya | Tidak | Ya | Ya |
| Duplikat | Ya | Ya | Key unik | Tidak |
| Akses | Index | Index | Key | Tidak bisa index |
| Contoh | `[1,2,3]` | `(1,2,3)` | `{"a":1}` | `{1,2,3}` |

### Kapan Menggunakan?

| Situasi | Gunakan |
|---------|---------|
| Koleksi data yang perlu diubah/ditambah | **List** |
| Data tetap yang tidak boleh berubah | **Tuple** |
| Menyimpan data berpasangan (key-value) | **Dictionary** |
| Menghilangkan duplikat / operasi himpunan | **Set** |

---

## File Praktikum

| No | File | Topik |
|:--:|------|-------|
| 1 | `01_list.py` | Membuat list, slicing, method, list comprehension |
| 2 | `02_tuple.py` | Tuple, immutability, unpacking |
| 3 | `03_dictionary.py` | Key-value pairs, nested dict, dict comprehension |
| 4 | `04_set.py` | Set, operasi himpunan, frozenset |

### Cara Menjalankan

```bash
python chapter_2/01_list.py
python chapter_2/02_tuple.py
python chapter_2/03_dictionary.py
python chapter_2/04_set.py
```

---

## Tugas Praktikum

Kerjakan seluruh tugas berikut sebagai bahan laporan praktikum. Buat file Python baru di dalam folder `chapter_2/` untuk setiap tugas.

### Tugas 1 -- Manajemen Nilai Mahasiswa (`tugas_01.py`)

- [ ] Buat sebuah **list** berisi 10 nilai ujian (integer, range 0-100)
- [ ] Tampilkan: nilai tertinggi, nilai terendah, dan rata-rata (hitung manual, jangan pakai library)
- [ ] Urutkan list dari terkecil ke terbesar, tampilkan hasilnya
- [ ] Gunakan **list comprehension** untuk membuat list baru berisi hanya nilai yang >= 70 (lulus)
- [ ] Hitung dan tampilkan jumlah mahasiswa yang lulus dan tidak lulus
- [ ] Tambahkan 2 nilai baru menggunakan `append()`, lalu hapus nilai terkecil menggunakan `remove()`

**Contoh Output:**
```
===== MANAJEMEN NILAI MAHASISWA =====
Nilai awal   : [85, 60, 92, 45, 78, 55, 90, 73, 68, 88]
Tertinggi    : 92
Terendah     : 45
Rata-rata    : 73.4
Nilai sorted : [45, 55, 60, 68, 73, 78, 85, 88, 90, 92]
Nilai lulus   : [85, 92, 78, 90, 73, 88]
Lulus: 6 | Tidak lulus: 4
...
```

---

### Tugas 2 -- Sistem Data Mahasiswa (`tugas_02.py`)

- [ ] Buat **dictionary** berisi data 5 mahasiswa, setiap mahasiswa memiliki: `nama`, `nim`, `jurusan`, dan `nilai` (berupa dict dengan key mata kuliah)
- [ ] Tampilkan seluruh data mahasiswa dalam format tabel rapi
- [ ] Hitung dan tampilkan rata-rata nilai setiap mahasiswa
- [ ] Cari dan tampilkan mahasiswa dengan rata-rata tertinggi
- [ ] Tambahkan 1 mahasiswa baru ke dictionary
- [ ] Gunakan **dictionary comprehension** untuk membuat dict baru yang berisi `{nama: rata_rata_nilai}`

**Contoh Struktur Data:**
```python
mahasiswa = {
    "MHS001": {
        "nama": "Ahmad",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78}
    },
    ...
}
```

---

### Tugas 3 -- Analisis Teks dengan Set (`tugas_03.py`)

- [ ] Definisikan 2 buah string kalimat (minimal 10 kata per kalimat)
- [ ] Konversi setiap kalimat menjadi **set** berisi kata-kata unik (lowercase)
- [ ] Tampilkan kata yang muncul di **kedua** kalimat (intersection)
- [ ] Tampilkan kata yang **hanya** ada di kalimat pertama (difference)
- [ ] Tampilkan kata yang **hanya** ada di kalimat kedua (difference)
- [ ] Tampilkan **semua** kata unik dari kedua kalimat (union)
- [ ] Tampilkan kata yang hanya ada di **salah satu** kalimat (symmetric difference)
- [ ] Hitung jumlah kata unik total

---

### Tugas 4 -- Tuple untuk Data Koordinat (`tugas_04.py`)

- [ ] Buat list berisi 5 **tuple** koordinat `(x, y)` yang merepresentasikan lokasi
- [ ] Gunakan **tuple unpacking** untuk menampilkan setiap koordinat
- [ ] Hitung jarak antara dua titik menggunakan rumus Euclidean: `d = sqrt((x2-x1)^2 + (y2-y1)^2)` (tanpa import math, gunakan `** 0.5`)
- [ ] Cari dan tampilkan pasangan titik yang paling dekat jaraknya
- [ ] Buat **dictionary** dengan tuple sebagai key dan nama lokasi sebagai value
- [ ] Buktikan bahwa tuple bisa jadi key dictionary tapi list tidak bisa (gunakan try-except)

---

## Checklist Laporan

- [ ] Semua tugas (Tugas 1 s/d 4) telah dikerjakan
- [ ] Setiap file dapat dijalankan tanpa error
- [ ] Output program sesuai dengan format yang diminta
- [ ] Menggunakan struktur data yang tepat sesuai kebutuhan
- [ ] Kode menggunakan list/dict comprehension minimal di 1 tugas
- [ ] Setiap file memiliki komentar penjelasan di bagian atas
- [ ] Screenshot output program dilampirkan dalam laporan

---

<div align="center">

**Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

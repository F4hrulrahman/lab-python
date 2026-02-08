<div align="center">

# Chapter 5: NumPy & Pandas

**Modul Praktikum Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

---

## Tujuan Praktikum

Setelah menyelesaikan chapter ini, praktikan diharapkan mampu:

1. Membuat dan memanipulasi **array NumPy** untuk komputasi numerik
2. Melakukan operasi statistik dasar (mean, median, std, dll.) menggunakan NumPy
3. Membuat dan memanipulasi **DataFrame Pandas** untuk data tabular
4. Melakukan filtering, grouping, dan agregasi data
5. Menangani missing data pada dataset

---

## Landasan Teori

### Mengapa NumPy & Pandas?

```
Raw Data  ──►  NumPy (numerik)  ──►  Analisis  ──►  Machine Learning
              Pandas (tabular)       & Insight       (Chapter 6)
```

| Library | Struktur Utama | Kegunaan |
|---------|:-------------:|----------|
| **NumPy** | `ndarray` | Operasi matematika cepat, array multidimensi, aljabar linear |
| **Pandas** | `Series`, `DataFrame` | Manipulasi data tabular, baca/tulis CSV/Excel, analisis data |

### Fungsi Statistik Penting

| Fungsi | Kegunaan |
|--------|----------|
| `np.mean()` | Rata-rata |
| `np.median()` | Nilai tengah |
| `np.std()` | Standar deviasi |
| `np.min()` / `np.max()` | Nilai minimum / maksimum |
| `np.sum()` | Jumlah total |
| `np.corrcoef()` | Koefisien korelasi |

---

## File Praktikum

| No | File | Topik |
|:--:|------|-------|
| 1 | `01_numpy_dasar.py` | Membuat array, indexing, statistik, reshaping, operasi matriks |
| 2 | `02_pandas_dasar.py` | Series, DataFrame, filtering, groupby, missing data |

### Cara Menjalankan

```bash
python chapter_5/01_numpy_dasar.py
python chapter_5/02_pandas_dasar.py
```

---

## Tugas Praktikum

Kerjakan seluruh tugas berikut sebagai bahan laporan praktikum. Buat file Python baru di dalam folder `chapter_5/` untuk setiap tugas.

### Tugas 1 -- Analisis Statistik dengan NumPy (`tugas_01.py`)

- [ ] Buat array NumPy berisi **nilai ujian 30 mahasiswa** (gunakan `np.random.randint(40, 100, 30)` dengan seed 42)
- [ ] Hitung dan tampilkan:
  - Mean, Median, Standar Deviasi
  - Nilai tertinggi dan terendah beserta index-nya (`argmax`, `argmin`)
  - Jumlah mahasiswa dengan nilai >= 70
- [ ] Lakukan **normalisasi Min-Max** (0-1) terhadap data
- [ ] Lakukan **normalisasi Z-Score** terhadap data
- [ ] Buat array 2D (6x5) dari data tersebut menggunakan `reshape`, anggap setiap baris = 1 kelas
- [ ] Hitung rata-rata per kelas (per baris) dan rata-rata per mata ujian (per kolom)
- [ ] Tampilkan semua hasil dalam format yang terstruktur

**Contoh Output:**
```
===== ANALISIS STATISTIK NILAI MAHASISWA =====
Data (30 mahasiswa): [72 51 87 ... ]

--- Statistik Deskriptif ---
Mean    : 68.73
Median  : 70.50
Std Dev : 15.42
Min     : 41 (index: 12)
Max     : 97 (index: 7)
Lulus   : 18 dari 30 (60.0%)

--- Normalisasi ---
Min-Max : [0.554 0.179 0.821 ...]
Z-Score : [0.212 -1.150 1.184 ...]

--- Rata-rata per Kelas (reshape 6x5) ---
Kelas 1 : 73.40
Kelas 2 : 65.20
...
```

---

### Tugas 2 -- Analisis Data Mahasiswa dengan Pandas (`tugas_02.py`)

- [ ] Buat DataFrame berisi data **20 mahasiswa** dengan kolom:
  - `Nama`, `NIM`, `Jurusan` (pilih 3 jurusan), `Semester` (2-8), `IPK` (2.0-4.0), `Jenis_Kelamin` (L/P)
  - (Boleh generate secara random dengan seed 42, atau tulis manual)
- [ ] Tampilkan informasi dasar: `shape`, `dtypes`, `describe()`
- [ ] **Filtering**: Tampilkan mahasiswa yang:
  - IPK >= 3.5
  - Jurusan "Informatika" DAN semester >= 5
- [ ] **Sorting**: Urutkan berdasarkan IPK (descending), tampilkan 5 teratas
- [ ] **Groupby**: Hitung statistik IPK per jurusan (mean, min, max, count)
- [ ] **Groupby**: Hitung jumlah mahasiswa per jenis kelamin per jurusan
- [ ] Tambahkan kolom baru `Predikat`:
  - IPK >= 3.5 -> "Cum Laude"
  - IPK >= 3.0 -> "Sangat Memuaskan"
  - IPK >= 2.5 -> "Memuaskan"
  - IPK < 2.5 -> "Cukup"
- [ ] Tampilkan distribusi predikat menggunakan `value_counts()`

---

### Tugas 3 -- Handling Missing Data (`tugas_03.py`)

- [ ] Buat DataFrame yang **sengaja memiliki missing value (NaN)** pada beberapa kolom (minimal 3 kolom, 10-15 baris)
- [ ] Tampilkan jumlah NaN per kolom menggunakan `isnull().sum()`
- [ ] Tampilkan persentase data yang hilang per kolom
- [ ] Buat 3 versi DataFrame yang telah ditangani:
  - **Versi 1**: `dropna()` -- hapus baris yang memiliki NaN
  - **Versi 2**: `fillna()` dengan **mean** untuk kolom numerik dan **modus** untuk kolom kategorikal
  - **Versi 3**: `fillna()` dengan method `ffill` (forward fill)
- [ ] Bandingkan jumlah baris ketiga versi
- [ ] Jelaskan dalam komentar: kapan sebaiknya menggunakan masing-masing metode

---

### Tugas 4 -- Analisis Data Penjualan (`tugas_04.py`)

- [ ] Buat DataFrame simulasi data penjualan dengan kolom:
  - `Tanggal` (gunakan `pd.date_range`, 30 hari)
  - `Produk` (random dari 5 produk)
  - `Kategori` (sesuai produk)
  - `Quantity` (random 1-50)
  - `Harga_Satuan` (sesuai produk)
- [ ] Tambahkan kolom `Total` = `Quantity * Harga_Satuan`
- [ ] Analisis:
  - Total penjualan keseluruhan
  - Produk dengan total penjualan tertinggi
  - Kategori dengan total penjualan tertinggi
  - Rata-rata penjualan per hari
  - Hari dengan penjualan tertinggi dan terendah
- [ ] Buat ringkasan menggunakan `groupby` + `agg` (sum, mean, count)
- [ ] Tampilkan semua hasil analisis dalam format yang rapi

**Contoh Output:**
```
===== LAPORAN ANALISIS PENJUALAN =====
Periode: 2024-01-01 s/d 2024-01-30

--- Ringkasan per Produk ---
Produk       | Qty Total | Total Penjualan | Rata-Rata
-------------+-----------+-----------------+-----------
Laptop       |        45 | Rp675,000,000   | Rp15,000,000
Mouse        |       120 | Rp18,000,000    | Rp150,000
...

--- Grand Total ---
Total Penjualan  : Rp1,234,567,890
Rata-rata/hari   : Rp41,152,263
Hari tertinggi   : 2024-01-15 (Rp98,500,000)
```

---

## Checklist Laporan

- [ ] Semua tugas (Tugas 1 s/d 4) telah dikerjakan
- [ ] Setiap file dapat dijalankan tanpa error
- [ ] Menggunakan NumPy untuk operasi numerik (bukan loop manual)
- [ ] Menggunakan Pandas untuk manipulasi data tabular
- [ ] Demonstrasi `groupby`, `filtering`, dan handling missing data
- [ ] Output program menampilkan data secara terstruktur dan mudah dibaca
- [ ] Setiap file memiliki komentar penjelasan di bagian atas
- [ ] Screenshot output program dilampirkan dalam laporan

---

<div align="center">

**Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

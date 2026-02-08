<div align="center">

# Laboratorium Python & Dasar Artificial Intelligence

### Universitas Muhammadiyah Makassar

---

**Modul Praktikum Pemrograman Python & Pengenalan Machine Learning**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## Tentang Modul Ini

Repositori ini merupakan modul praktikum resmi **Laboratorium Pemrograman Python & Dasar AI** di Universitas Muhammadiyah Makassar. Modul dirancang secara bertahap dari fundamental bahasa Python hingga implementasi algoritma Machine Learning, sehingga mahasiswa dapat membangun pemahaman yang solid dari dasar hingga aplikasi AI sederhana.

Setiap chapter dilengkapi dengan **penjelasan konsep**, **contoh kode yang bisa langsung dijalankan**, dan **studi kasus praktis** agar mahasiswa tidak hanya memahami teori, tetapi juga mampu menerapkannya.

---

## Daftar Modul Praktikum

| Chapter | Topik | Deskripsi | Tingkat |
|:-------:|-------|-----------|:-------:|
| [01](chapter_1/) | **Dasar Python** | Variabel, tipe data, operator, input/output | Dasar |
| [02](chapter_2/) | **Struktur Data** | List, tuple, dictionary, set | Dasar |
| [03](chapter_3/) | **Control Flow & Fungsi** | Percabangan, perulangan, fungsi, lambda | Dasar |
| [04](chapter_4/) | **OOP Dasar** | Class, object, inheritance, encapsulation | Menengah |
| [05](chapter_5/) | **NumPy & Pandas** | Manipulasi data numerik dan tabular | Menengah |
| [06](chapter_6/) | **Machine Learning & AI** | Klasifikasi, regresi, clustering dengan scikit-learn | Lanjut |

---

## Capaian Pembelajaran

Setelah menyelesaikan seluruh modul, mahasiswa diharapkan mampu:

1. Memahami sintaks dasar dan struktur data pada Python
2. Menerapkan paradigma Object-Oriented Programming (OOP)
3. Melakukan manipulasi dan analisis data menggunakan NumPy & Pandas
4. Memahami konsep dasar Machine Learning (supervised & unsupervised learning)
5. Mengimplementasikan algoritma klasifikasi, regresi, dan clustering
6. Mengevaluasi performa model menggunakan metrik yang tepat

---

## Prasyarat

| Kebutuhan | Versi Minimum | Keterangan |
|-----------|:------------:|------------|
| Python | 3.8+ | Bahasa pemrograman utama |
| pip | Terbaru | Package manager Python |
| Git | Terbaru | Version control *(opsional)* |

---

## Panduan Instalasi

### 1. Clone Repositori

```bash
git clone https://github.com/devnolife/python-dasar.git
cd python-dasar
```

### 2. Buat Virtual Environment

```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi (pilih sesuai OS)
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux / macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verifikasi Instalasi

```bash
python -c "import numpy; import pandas; import sklearn; print('Semua package berhasil diinstall.')"
```

---

## Cara Menggunakan

Setiap chapter memiliki folder tersendiri. Jalankan file Python secara berurutan sesuai nomor modul:

```bash
# Contoh: menjalankan modul Chapter 1
python chapter_1/01_variabel.py
python chapter_1/02_tipe_data.py
python chapter_1/03_operator.py

# Contoh: menjalankan modul Chapter 6 (Machine Learning)
python chapter_6/01_klasifikasi.py
python chapter_6/02_regresi.py
python chapter_6/03_clustering.py
```

> Setiap chapter juga memiliki file `README.md` tersendiri yang berisi penjelasan materi dan panduan lebih detail.

---

## Struktur Repositori

```
python-dasar/
│
├── README.md                   # Dokumentasi utama
├── requirements.txt            # Daftar dependencies
│
├── chapter_1/                  # DASAR PYTHON
│   ├── README.md
│   ├── 01_variabel.py          # Variabel & penamaan
│   ├── 02_tipe_data.py         # Tipe data & type casting
│   └── 03_operator.py          # Operator aritmatika, logika, perbandingan
│
├── chapter_2/                  # STRUKTUR DATA
│   ├── README.md
│   ├── 01_list.py              # List & list comprehension
│   ├── 02_tuple.py             # Tuple & unpacking
│   ├── 03_dictionary.py        # Dictionary & nested dict
│   └── 04_set.py               # Set & operasi himpunan
│
├── chapter_3/                  # CONTROL FLOW & FUNGSI
│   ├── README.md
│   ├── 01_percabangan.py       # if/elif/else, match-case
│   ├── 02_perulangan.py        # for, while, enumerate, zip
│   └── 03_fungsi.py            # def, lambda, *args, **kwargs, rekursi
│
├── chapter_4/                  # OBJECT-ORIENTED PROGRAMMING
│   ├── README.md
│   ├── 01_class_object.py      # Class, object, dunder methods
│   ├── 02_inheritance.py       # Inheritance & polymorphism
│   └── 03_encapsulation.py     # Encapsulation & property
│
├── chapter_5/                  # NUMPY & PANDAS
│   ├── README.md
│   ├── 01_numpy_dasar.py       # Array, operasi numerik, statistik
│   └── 02_pandas_dasar.py      # DataFrame, filtering, groupby
│
└── chapter_6/                  # MACHINE LEARNING & AI
    ├── README.md
    ├── 01_klasifikasi.py       # KNN, Decision Tree, Random Forest
    ├── 02_regresi.py           # Linear & Polynomial Regression
    └── 03_clustering.py        # K-Means, Elbow Method, Silhouette
```

---

## Peta Pembelajaran

```
FUNDAMENTAL                    DATA SCIENCE               MACHINE LEARNING
─────────────                  ────────────               ────────────────

 Chapter 1                      Chapter 5                  Chapter 6
 Dasar Python ──────┐          NumPy & Pandas ─────┐      ML & AI
                    │                              │
 Chapter 2          ├────────►  Manipulasi   ──────┼────►  Klasifikasi
 Struktur Data ─────┤           Data Numerik       │       Regresi
                    │           & Tabular           │       Clustering
 Chapter 3          │                              │
 Control Flow  ─────┤                              │
 & Fungsi           │                              │
                    │                              │
 Chapter 4          │                              │
 OOP Dasar    ──────┘                              │
                                                   │
                    Prerequisite ───────────────────┘
```

---

## Teknologi & Library

| Library | Fungsi | Digunakan di |
|---------|--------|:------------:|
| **Python** | Bahasa pemrograman utama | Semua chapter |
| **NumPy** | Komputasi numerik & array multidimensi | Chapter 5, 6 |
| **Pandas** | Manipulasi & analisis data tabular | Chapter 5, 6 |
| **scikit-learn** | Framework machine learning | Chapter 6 |
| **Matplotlib** | Visualisasi data | Chapter 6 |

---

## Panduan untuk Praktikan

1. **Baca `README.md`** pada setiap chapter sebelum memulai
2. **Jalankan kode** secara berurutan dan **amati output**-nya
3. **Modifikasi parameter** dalam kode untuk memahami dampaknya
4. **Kerjakan latihan** yang tersedia di akhir setiap chapter
5. **Jangan copy-paste** -- ketik ulang kode untuk membangun *muscle memory*
6. **Diskusikan** dengan asisten lab jika menemui kesulitan

---

## Panduan untuk Asisten Lab

- Pastikan semua PC lab sudah terinstall Python 3.8+ dan dependencies
- Gunakan modul ini sebagai acuan saat mendampingi praktikum
- Setiap pertemuan disarankan menyelesaikan **1 chapter**
- Berikan waktu 15-20 menit di akhir sesi untuk latihan mandiri
- Evaluasi pemahaman mahasiswa melalui modifikasi kode, bukan hafalan

---

## Kontributor

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/devnolife">
        <img src="https://github.com/devnolife.png" width="100px;" alt="devnolife"/>
        <br />
        <sub><b>devnolife</b></sub>
      </a>
      <br />
      <sub>Koordinator Lab</sub>
    </td>
  </tr>
</table>

---

## Lisensi

Modul ini dikembangkan untuk keperluan akademik di lingkungan **Universitas Muhammadiyah Makassar**. Materi boleh digunakan, dimodifikasi, dan didistribusikan untuk tujuan edukasi dengan tetap menyertakan atribusi kepada sumber asli.

---

<div align="center">

**Laboratorium Pemrograman Python & Dasar AI**
<br />
Universitas Muhammadiyah Makassar
<br /><br />

*"Belajar AI dimulai dari fondasi yang kuat"*

</div>

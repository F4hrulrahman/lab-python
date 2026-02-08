<div align="center">

# Chapter 6: Machine Learning & Artificial Intelligence

**Modul Praktikum Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

---

## Tujuan Praktikum

Setelah menyelesaikan chapter ini, praktikan diharapkan mampu:

1. Memahami konsep dasar **supervised** dan **unsupervised learning**
2. Melakukan **preprocessing** data untuk keperluan machine learning
3. Mengimplementasikan algoritma **klasifikasi** (KNN, Decision Tree, Random Forest)
4. Mengimplementasikan algoritma **regresi** (Linear, Polynomial, Multiple)
5. Mengimplementasikan algoritma **clustering** (K-Means)
6. Mengevaluasi performa model menggunakan **metrik** yang tepat

---

## Landasan Teori

### Taksonomi Machine Learning

```
Machine Learning
│
├── Supervised Learning (data memiliki label)
│   ├── Klasifikasi ──► Prediksi kategori    ──► Spam/Bukan, Penyakit/Sehat
│   └── Regresi      ──► Prediksi nilai angka ──► Harga Rumah, Prediksi Gaji
│
├── Unsupervised Learning (data tanpa label)
│   ├── Clustering   ──► Pengelompokan data   ──► Segmentasi Pelanggan
│   └── Dim. Reduction ► Mengurangi fitur     ──► PCA, t-SNE
│
└── Reinforcement Learning
    └── Agent belajar dari reward/penalty      ──► Game AI, Robot
```

### Pipeline Machine Learning

```
┌──────────┐    ┌───────────────┐    ┌─────────────┐    ┌──────────┐    ┌──────────┐
│ Kumpulkan│───►│ Preprocessing │───►│ Train / Test │───►│ Training │───►│ Evaluasi │
│   Data   │    │  & Cleaning   │    │    Split     │    │  Model   │    │  Model   │
└──────────┘    └───────────────┘    └─────────────┘    └──────────┘    └──────────┘
                                                                              │
                                                                              ▼
                                                                        ┌──────────┐
                                                                        │ Prediksi │
                                                                        │ Data Baru│
                                                                        └──────────┘
```

### Metrik Evaluasi

| Tipe ML | Metrik | Penjelasan |
|---------|--------|-----------|
| **Klasifikasi** | Accuracy | Persentase prediksi benar |
| | Precision | Ketepatan prediksi positif |
| | Recall | Kelengkapan prediksi positif |
| | F1-Score | Harmonic mean precision & recall |
| **Regresi** | MSE | Rata-rata kuadrat error |
| | RMSE | Akar MSE (satuan sama dengan target) |
| | R-squared | Seberapa baik model menjelaskan variasi data (0-1) |
| **Clustering** | Silhouette Score | Seberapa baik data cocok di clusternya (-1 s/d 1) |
| | Inertia | Sum of squared distances ke centroid |

---

## File Praktikum

| No | File | Topik | Algoritma |
|:--:|------|-------|-----------|
| 1 | `01_klasifikasi.py` | Supervised - Klasifikasi | KNN, Decision Tree, Random Forest |
| 2 | `02_regresi.py` | Supervised - Regresi | Linear, Polynomial, Multiple Regression |
| 3 | `03_clustering.py` | Unsupervised - Clustering | K-Means, Elbow Method |

### Cara Menjalankan

```bash
python chapter_6/01_klasifikasi.py
python chapter_6/02_regresi.py
python chapter_6/03_clustering.py
```

---

## Tugas Praktikum

Kerjakan seluruh tugas berikut sebagai bahan laporan praktikum. Buat file Python baru di dalam folder `chapter_6/` untuk setiap tugas.

### Tugas 1 -- Klasifikasi Dataset Wine (`tugas_01.py`)

Gunakan dataset **Wine** bawaan scikit-learn (`from sklearn.datasets import load_wine`) untuk melakukan klasifikasi jenis wine.

- [ ] Muat dataset dan tampilkan informasi dasar:
  - Jumlah sampel, jumlah fitur, nama fitur, nama kelas
  - Distribusi kelas (berapa sampel per kelas)
- [ ] Lakukan **preprocessing**:
  - Train/test split (80:20) dengan `stratify` dan `random_state=42`
  - Standardisasi fitur menggunakan `StandardScaler`
- [ ] Latih dan evaluasi **3 model**:
  - K-Nearest Neighbors (coba k=3, k=5, k=7, pilih yang terbaik)
  - Decision Tree (`max_depth=5`)
  - Random Forest (`n_estimators=100`)
- [ ] Untuk setiap model, tampilkan:
  - Accuracy score
  - Classification report (precision, recall, f1-score per kelas)
  - Confusion matrix
- [ ] Buat **tabel perbandingan** ketiga model
- [ ] Prediksi kelas untuk **3 data baru** yang dibuat sendiri menggunakan model terbaik
- [ ] **Analisis**: Tuliskan dalam komentar, model mana yang terbaik dan mengapa

**Contoh Output Perbandingan:**
```
===== PERBANDINGAN MODEL KLASIFIKASI =====
Model               | Accuracy | Precision | Recall | F1-Score
--------------------+----------+-----------+--------+---------
KNN (k=5)           |   0.9722 |    0.9735 | 0.9722 |  0.9720
Decision Tree       |   0.9167 |    0.9200 | 0.9167 |  0.9155
Random Forest       |   1.0000 |    1.0000 | 1.0000 |  1.0000
=====================================================
Model Terbaik: Random Forest (Accuracy: 100.0%)
```

---

### Tugas 2 -- Regresi: Prediksi Nilai Mahasiswa (`tugas_02.py`)

Buat dataset simulasi dan lakukan regresi untuk memprediksi nilai akhir mahasiswa.

- [ ] **Buat dataset** (200 sampel) dengan fitur:
  - `jam_belajar` (0-20 jam/minggu)
  - `kehadiran` (50-100%)
  - `tugas_selesai` (0-10 tugas)
  - `nilai_uts` (0-100)
  - Target: `nilai_akhir` (hubungan: kombinasi linear dari fitur + noise)
- [ ] Lakukan **train/test split** (80:20)
- [ ] Latih model **Linear Regression**
- [ ] Tampilkan:
  - Koefisien model (interpretasikan setiap koefisien dalam komentar)
  - MSE, RMSE, MAE, R-squared
- [ ] Latih model **Polynomial Regression** (degree=2), bandingkan hasilnya dengan linear
- [ ] Prediksi nilai akhir untuk **5 mahasiswa baru** dengan data yang dibuat sendiri
- [ ] Buat **tabel perbandingan** Linear vs Polynomial
- [ ] **Analisis**: Tuliskan interpretasi koefisien -- fitur mana yang paling berpengaruh?

**Contoh Output Prediksi:**
```
===== PREDIKSI NILAI AKHIR MAHASISWA =====
No | Jam Belajar | Kehadiran | Tugas | UTS  | Prediksi Nilai Akhir
---+-------------+-----------+-------+------+---------------------
 1 |          15 |      95%  |     9 |   85 |                88.5
 2 |           3 |      60%  |     4 |   50 |                47.2
 3 |          10 |      80%  |     7 |   70 |                72.8
...

--- Interpretasi Koefisien ---
jam_belajar  : +2.15 (setiap +1 jam belajar, nilai naik ~2.15 poin)
kehadiran    : +0.35 (setiap +1% kehadiran, nilai naik ~0.35 poin)
...
```

---

### Tugas 3 -- Clustering: Segmentasi Mahasiswa (`tugas_03.py`)

Lakukan clustering untuk mengelompokkan mahasiswa berdasarkan perilaku akademik.

- [ ] **Buat dataset** (150 sampel) dengan fitur:
  - `ipk` (1.5-4.0)
  - `jam_belajar_per_minggu` (0-25)
  - `kehadiran_persen` (40-100)
  - `aktivitas_organisasi` (0-10 skala)
  - (Generate data sehingga secara natural membentuk 3-4 cluster)
- [ ] Lakukan **standardisasi** menggunakan `StandardScaler`
- [ ] Tentukan jumlah cluster optimal menggunakan **Elbow Method**:
  - Jalankan K-Means untuk K=2 sampai K=10
  - Tampilkan tabel Inertia dan Silhouette Score untuk setiap K
  - Tentukan K optimal
- [ ] Jalankan **K-Means** dengan K optimal
- [ ] Tampilkan:
  - Jumlah mahasiswa per cluster
  - Rata-rata setiap fitur per cluster
  - Silhouette Score keseluruhan
- [ ] **Beri nama/label** setiap cluster berdasarkan karakteristiknya (misal: "Mahasiswa Aktif", "Mahasiswa Pasif", dll.)
- [ ] Prediksi cluster untuk **5 mahasiswa baru**
- [ ] **Analisis**: Tuliskan dalam komentar, apa karakteristik setiap cluster dan saran untuk masing-masing kelompok

**Contoh Output:**
```
===== SEGMENTASI MAHASISWA =====
K Optimal: 3 (Silhouette Score: 0.6234)

--- Profil Cluster ---
Cluster | Nama Segment       | Jumlah | IPK  | Jam Belajar | Kehadiran | Organisasi
--------+--------------------+--------+------+-------------+-----------+-----------
   0    | Mahasiswa Berprestasi |   45  | 3.72 |    18.5     |   95.2%   |    7.3
   1    | Mahasiswa Standar  |   62  | 2.85 |    10.2     |   78.4%   |    4.1
   2    | Mahasiswa Berisiko |   43  | 2.10 |     4.8     |   58.7%   |    2.0

--- Rekomendasi ---
Cluster 0 (Berprestasi) : Pertahankan prestasi, arahkan ke riset/lomba
Cluster 1 (Standar)     : Tingkatkan jam belajar dan kehadiran
Cluster 2 (Berisiko)    : Perlu bimbingan intensif dan monitoring kehadiran
```

---

### Tugas 4 -- Proyek Mini: End-to-End ML Pipeline (`tugas_04.py`)

Buat pipeline machine learning lengkap dari awal sampai akhir. Pilih **salah satu** skenario berikut:

**Opsi A -- Klasifikasi Kelayakan Beasiswa**

- [ ] Buat dataset mahasiswa (min 200 sampel) dengan fitur: IPK, penghasilan orang tua, semester, jumlah tanggungan, prestasi (skor 0-100)
- [ ] Target: Layak / Tidak Layak beasiswa
- [ ] Preprocessing: handling outlier, scaling
- [ ] Latih minimal 2 model klasifikasi
- [ ] Evaluasi dan bandingkan
- [ ] Prediksi untuk data baru

**Opsi B -- Regresi Prediksi Biaya Hidup**

- [ ] Buat dataset (min 200 sampel) dengan fitur: kota (encoded), tipe kos, jarak kampus, fasilitas (skor), luas kamar
- [ ] Target: Biaya kos per bulan
- [ ] Preprocessing: encoding kategorikal, scaling
- [ ] Latih minimal 2 model regresi
- [ ] Evaluasi dan bandingkan
- [ ] Prediksi untuk data baru

**Untuk kedua opsi, pastikan:**

- [ ] Dataset dibuat/disimulasikan secara realistis
- [ ] Ada tahap **preprocessing** (scaling, encoding jika perlu)
- [ ] Ada **train/test split**
- [ ] Minimal **2 model** dibandingkan
- [ ] Ada **evaluasi** dengan metrik yang sesuai
- [ ] Ada **prediksi data baru** dengan interpretasi hasil
- [ ] Ada **kesimpulan** dalam komentar: model mana yang dipilih dan alasannya

---

## Checklist Laporan

- [ ] Semua tugas (Tugas 1 s/d 4) telah dikerjakan
- [ ] Setiap file dapat dijalankan tanpa error
- [ ] Menggunakan **train/test split** pada setiap model
- [ ] Menampilkan **metrik evaluasi** yang sesuai untuk setiap tipe ML
- [ ] Ada **perbandingan antar model** minimal di 2 tugas
- [ ] Ada **analisis/interpretasi** hasil dalam bentuk komentar
- [ ] Output program menampilkan hasil secara terstruktur dan mudah dibaca
- [ ] Setiap file memiliki komentar penjelasan dan docstring
- [ ] Screenshot output program dilampirkan dalam laporan
- [ ] Tugas 4 (proyek mini) memuat pipeline ML yang lengkap

---

<div align="center">

**Laboratorium Python & Dasar AI**
<br/>
Universitas Muhammadiyah Makassar

</div>

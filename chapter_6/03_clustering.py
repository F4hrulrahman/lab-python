"""
Chapter 6 - Bagian 3: Clustering
====================================
Clustering adalah tipe UNSUPERVISED learning di mana model
mengelompokkan data tanpa label/jawaban yang sudah diketahui.

Contoh: Segmentasi pelanggan, pengelompokan dokumen, deteksi anomali.

Install: pip install scikit-learn numpy matplotlib
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs

# ============================================
# 1. Konsep Clustering
# ============================================
print("=" * 60)
print("CLUSTERING DENGAN SCIKIT-LEARN")
print("=" * 60)

print("\n=== 1. Konsep Clustering ===")
print("Clustering = mengelompokkan data TANPA label")
print("  - Model mencari pola/struktur tersembunyi dalam data")
print("  - K-Means: mengelompokkan data ke K cluster berdasarkan jarak")
print("  - Setiap cluster punya centroid (titik pusat)")

# ============================================
# 2. Membuat Dataset
# ============================================
print("\n=== 2. Membuat Dataset ===")

# Generate data dengan 4 cluster
np.random.seed(42)
X, y_true = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.0,
    random_state=42,
)

print(f"Jumlah data: {X.shape[0]}")
print(f"Jumlah fitur: {X.shape[1]}")
print(f"Cluster asli: {len(np.unique(y_true))} (ini kita 'pura-pura' tidak tahu)")
print(f"Contoh data (5 pertama):\n{X[:5].round(2)}")

# Standardisasi
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================
# 3. K-Means Clustering
# ============================================
print("\n=== 3. K-Means Clustering ===")
print("Algoritma K-Means:")
print("  1. Pilih K centroid secara acak")
print("  2. Assign setiap data ke centroid terdekat")
print("  3. Update centroid = rata-rata data di cluster")
print("  4. Ulangi langkah 2-3 sampai konvergen\n")

# Kita coba K=4 (karena kita tahu ada 4 cluster)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

print(f"Cluster labels (10 pertama): {labels[:10]}")
print(f"Jumlah data per cluster:")
for i in range(4):
    count = np.sum(labels == i)
    print(f"  Cluster {i}: {count} data ({count / len(labels) * 100:.1f}%)")

print(f"\nCentroid (setelah scaling):")
for i, centroid in enumerate(kmeans.cluster_centers_):
    print(f"  Cluster {i}: [{centroid[0]:.3f}, {centroid[1]:.3f}]")

print(f"\nInertia (sum of squared distances): {kmeans.inertia_:.2f}")

# ============================================
# 4. Menentukan K Optimal (Elbow Method)
# ============================================
print("\n=== 4. Elbow Method ===")
print("Cara menentukan jumlah cluster (K) yang optimal:")
print("  - Jalankan K-Means dengan berbagai nilai K")
print("  - Plot inertia vs K")
print("  - Cari 'siku' (elbow) di mana penurunan melambat\n")

inertias = []
silhouettes = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    sil = silhouette_score(X_scaled, km.labels_)
    silhouettes.append(sil)

print(f"{'K':>3} | {'Inertia':>10} | {'Silhouette':>10} | Visualisasi")
print("-" * 55)
for k, inertia, sil in zip(K_range, inertias, silhouettes):
    bar_i = "#" * int(inertia / max(inertias) * 20)
    bar_s = "#" * int(sil / max(silhouettes) * 20)
    marker = " <-- optimal" if k == 4 else ""
    print(f"{k:3d} | {inertia:10.1f} | {sil:10.4f} | {bar_s}{marker}")

best_k = K_range[np.argmax(silhouettes)]
print(f"\nK optimal (berdasarkan silhouette): {best_k}")

# ============================================
# 5. Evaluasi: Silhouette Score
# ============================================
print("\n=== 5. Silhouette Score ===")
print("Silhouette Score mengukur seberapa baik data cocok dengan clusternya")
print("  - Range: -1 sampai 1")
print("  - 1.0 = cluster sangat terpisah dengan baik")
print("  - 0.0 = cluster tumpang tindih")
print("  - <0  = data mungkin di cluster yang salah")

sil_score = silhouette_score(X_scaled, labels)
print(f"\nSilhouette Score (K=4): {sil_score:.4f}")

# ============================================
# 6. Contoh Praktis: Segmentasi Pelanggan
# ============================================
print("\n=== 6. Contoh: Segmentasi Pelanggan ===")

np.random.seed(42)
n_customers = 200

# Simulasi data pelanggan
pengeluaran_bulanan = np.concatenate(
    [
        np.random.normal(500_000, 100_000, 60),  # Low spender
        np.random.normal(2_000_000, 300_000, 80),  # Medium spender
        np.random.normal(5_000_000, 500_000, 60),  # High spender
    ]
)

frekuensi_belanja = np.concatenate(
    [
        np.random.normal(3, 1, 60),  # Jarang belanja
        np.random.normal(8, 2, 80),  # Sedang
        np.random.normal(15, 3, 60),  # Sering belanja
    ]
)

# Pastikan nilai positif
pengeluaran_bulanan = np.abs(pengeluaran_bulanan)
frekuensi_belanja = np.abs(frekuensi_belanja)

X_customer = np.column_stack([pengeluaran_bulanan, frekuensi_belanja])

# Scaling
scaler_cust = StandardScaler()
X_cust_scaled = scaler_cust.fit_transform(X_customer)

# K-Means
kmeans_cust = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_cust = kmeans_cust.fit_predict(X_cust_scaled)

# Analisis cluster
print(f"\nHasil Segmentasi ({n_customers} pelanggan):")
print(
    f"{'Segment':>10} | {'Jumlah':>7} | {'Avg Pengeluaran':>18} | {'Avg Frekuensi':>15}"
)
print("-" * 65)

segment_names = {}
for i in range(3):
    mask = labels_cust == i
    avg_spend = pengeluaran_bulanan[mask].mean()
    avg_freq = frekuensi_belanja[mask].mean()
    count = mask.sum()

    # Tentukan nama segment berdasarkan pengeluaran
    if avg_spend < 1_000_000:
        name = "Budget"
    elif avg_spend < 3_500_000:
        name = "Regular"
    else:
        name = "Premium"

    segment_names[i] = name
    print(f"{name:>10} | {count:>7} | Rp{avg_spend:>14,.0f} | {avg_freq:>13.1f}x/bln")

sil_cust = silhouette_score(X_cust_scaled, labels_cust)
print(f"\nSilhouette Score: {sil_cust:.4f}")

# Prediksi segment untuk pelanggan baru
print("\nPrediksi segment pelanggan baru:")
pelanggan_baru = [
    [300_000, 2],  # Low spender, jarang belanja
    [2_500_000, 10],  # Medium spender, cukup sering
    [6_000_000, 18],  # High spender, sangat sering
]

for p in pelanggan_baru:
    p_scaled = scaler_cust.transform([p])
    cluster = kmeans_cust.predict(p_scaled)[0]
    seg_name = segment_names[cluster]
    print(f"  Pengeluaran Rp{p[0]:,.0f}, Frekuensi {p[1]}x -> Segment: {seg_name}")

# ============================================
# 7. Ringkasan
# ============================================
print("\n=== 7. Ringkasan ML yang Dipelajari ===")
print("""
+------------------+-------------+-------------------+---------------------+
| Tipe             | Label?      | Contoh Algoritma  | Contoh Penggunaan   |
+------------------+-------------+-------------------+---------------------+
| Klasifikasi      | Ya (kelas)  | KNN, Decision     | Spam detection,     |
|                  |             | Tree, Random      | diagnosis penyakit  |
|                  |             | Forest            |                     |
+------------------+-------------+-------------------+---------------------+
| Regresi          | Ya (angka)  | Linear            | Prediksi harga,     |
|                  |             | Regression,       | prediksi gaji       |
|                  |             | Polynomial Reg.   |                     |
+------------------+-------------+-------------------+---------------------+
| Clustering       | Tidak       | K-Means           | Segmentasi          |
|                  |             |                   | pelanggan,          |
|                  |             |                   | pengelompokan data  |
+------------------+-------------+-------------------+---------------------+

Langkah selanjutnya:
1. Coba dataset lain (sklearn.datasets, Kaggle)
2. Pelajari feature engineering & preprocessing
3. Eksplorasi model lain (SVM, Neural Network)
4. Pelajari cross-validation & hyperparameter tuning
5. Coba deep learning dengan TensorFlow/PyTorch
""")

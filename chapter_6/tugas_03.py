"""
==========================================================
 TUGAS 3 - Clustering Segmentasi Mahasiswa
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat dataset sintetis 150 mahasiswa dengan fitur:
    - ipk (1.5-4.0)
    - jam_belajar_per_minggu (0-25)
    - kehadiran_persen (40-100)
    - aktivitas_organisasi (0-10)
    Data harus membentuk 3-4 cluster secara natural
 2. Preprocessing: StandardScaler
 3. Elbow Method: K-Means untuk K=2..10
    - Tabel Inertia dan Silhouette Score per K
 4. K-Means dengan K optimal
    - Jumlah anggota per cluster
    - Rata-rata fitur per cluster
    - Silhouette Score keseluruhan
 5. Beri nama/label setiap cluster berdasarkan karakteristik
 6. Prediksi cluster untuk 5 mahasiswa baru
 7. Analisis dan rekomendasi per cluster

 Tips membuat cluster natural:
   Gunakan np.concatenate untuk menggabungkan beberapa
   distribusi normal dengan mean berbeda.
==========================================================
"""

# TODO: Uncomment import yang diperlukan
# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import silhouette_score


# ============================================
# 1. Membuat Dataset
# ============================================
def buat_dataset(random_state=42):
    """Buat dataset sintetis mahasiswa dengan 3-4 cluster natural.

    Cluster yang diharapkan:
    - Cluster A: Mahasiswa berprestasi (IPK tinggi, rajin, aktif organisasi)
    - Cluster B: Mahasiswa rata-rata (IPK sedang, cukup rajin)
    - Cluster C: Mahasiswa kurang aktif (IPK rendah, jarang hadir)
    - Cluster D (opsional): Mahasiswa aktif organisasi tapi IPK sedang

    Args:
        random_state (int): Random seed.

    Returns:
        tuple: (X, feature_names)
               X = feature matrix (150, 4)
               feature_names = list nama fitur
    """
    # TODO: Set random seed
    # np.random.seed(random_state)
    #
    # TODO: Buat data per cluster lalu gabungkan
    # Cluster 1: Mahasiswa berprestasi (~40 orang)
    # ipk_1 = np.random.normal(3.7, 0.15, 40)
    # jam_1 = np.random.normal(20, 3, 40)
    # hadir_1 = np.random.normal(95, 3, 40)
    # org_1 = np.random.normal(7, 1.5, 40)
    #
    # Cluster 2: Mahasiswa rata-rata (~50 orang)
    # ipk_2 = np.random.normal(3.0, 0.25, 50)
    # jam_2 = np.random.normal(12, 3, 50)
    # hadir_2 = np.random.normal(78, 8, 50)
    # org_2 = np.random.normal(4, 2, 50)
    #
    # Cluster 3: Mahasiswa kurang aktif (~35 orang)
    # ipk_3 = np.random.normal(2.2, 0.3, 35)
    # jam_3 = np.random.normal(5, 2, 35)
    # hadir_3 = np.random.normal(55, 8, 35)
    # org_3 = np.random.normal(1, 1, 35)
    #
    # Cluster 4: Aktivis organisasi (~25 orang)
    # ipk_4 = np.random.normal(2.8, 0.2, 25)
    # jam_4 = np.random.normal(8, 3, 25)
    # hadir_4 = np.random.normal(70, 7, 25)
    # org_4 = np.random.normal(9, 1, 25)
    #
    # TODO: Gabungkan semua cluster
    # ipk = np.concatenate([ipk_1, ipk_2, ipk_3, ipk_4])
    # jam = np.concatenate([jam_1, jam_2, jam_3, jam_4])
    # hadir = np.concatenate([hadir_1, hadir_2, hadir_3, hadir_4])
    # org = np.concatenate([org_1, org_2, org_3, org_4])
    #
    # TODO: Clip nilai agar masuk akal
    # ipk = np.clip(ipk, 1.5, 4.0)
    # jam = np.clip(jam, 0, 25)
    # hadir = np.clip(hadir, 40, 100)
    # org = np.clip(org, 0, 10)
    #
    # TODO: Buat feature matrix
    # X = np.column_stack([ipk, jam, hadir, org])
    # feature_names = ["IPK", "Jam Belajar/Minggu", "Kehadiran (%)", "Aktivitas Organisasi"]
    #
    # TODO: Tampilkan info dataset
    # print(f"Jumlah sampel : {X.shape[0]}")
    # print(f"Jumlah fitur  : {X.shape[1]}")
    # print(f"Fitur         : {feature_names}")
    # print(f"\nStatistik fitur:")
    # for i, name in enumerate(feature_names):
    #     print(f"  {name:25s}: min={X[:, i].min():.2f}, max={X[:, i].max():.2f}, mean={X[:, i].mean():.2f}")
    #
    # return X, feature_names
    ...


# ============================================
# 2. Preprocessing (Scaling)
# ============================================
def preprocessing(X):
    """Standardisasi fitur menggunakan StandardScaler.

    Args:
        X (ndarray): Feature matrix.

    Returns:
        tuple: (X_scaled, scaler)
    """
    # TODO: Standardisasi
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)
    #
    # TODO: Tampilkan efek scaling
    # print("Sebelum scaling:")
    # print(f"  Mean: {X.mean(axis=0).round(2)}")
    # print(f"  Std : {X.std(axis=0).round(2)}")
    # print("Setelah scaling:")
    # print(f"  Mean: {X_scaled.mean(axis=0).round(2)}")
    # print(f"  Std : {X_scaled.std(axis=0).round(2)}")
    #
    # return X_scaled, scaler
    ...


# ============================================
# 3. Elbow Method
# ============================================
def elbow_method(X_scaled):
    """Tentukan K optimal dengan Elbow Method dan Silhouette Score.

    Args:
        X_scaled (ndarray): Feature matrix yang sudah di-scale.

    Returns:
        int: K optimal berdasarkan silhouette score.
    """
    # TODO: Jalankan K-Means untuk K=2..10
    # K_range = range(2, 11)
    # inertias = []
    # silhouettes = []
    #
    # for k in K_range:
    #     km = KMeans(n_clusters=k, random_state=42, n_init=10)
    #     km.fit(X_scaled)
    #     inertias.append(km.inertia_)
    #     sil = silhouette_score(X_scaled, km.labels_)
    #     silhouettes.append(sil)
    #
    # TODO: Buat tabel hasil
    # print(f"{'K':>3} | {'Inertia':>10} | {'Silhouette':>12} | Visualisasi")
    # print("-" * 60)
    # for k, inertia, sil in zip(K_range, inertias, silhouettes):
    #     bar = "#" * int(sil / max(silhouettes) * 25)
    #     print(f"{k:>3} | {inertia:>10.1f} | {sil:>12.4f} | {bar}")
    #
    # TODO: Tentukan K optimal
    # best_k = K_range[np.argmax(silhouettes)]
    # print(f"\nK optimal (silhouette tertinggi): {best_k}")
    # print(f"Silhouette Score terbaik        : {max(silhouettes):.4f}")
    #
    # return best_k
    ...


# ============================================
# 4. K-Means Clustering
# ============================================
def train_kmeans(X_scaled, X_original, feature_names, optimal_k):
    """Jalankan K-Means dengan K optimal dan analisis cluster.

    Args:
        X_scaled (ndarray): Feature matrix (scaled).
        X_original (ndarray): Feature matrix (original, untuk interpretasi).
        feature_names (list): Nama fitur.
        optimal_k (int): Jumlah cluster optimal.

    Returns:
        tuple: (kmeans_model, labels, cluster_names)
    """
    # TODO: Jalankan K-Means
    # kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    # labels = kmeans.fit_predict(X_scaled)
    #
    # TODO: Tampilkan jumlah anggota per cluster
    # print(f"Jumlah cluster: {optimal_k}")
    # print(f"\nDistribusi anggota per cluster:")
    # for i in range(optimal_k):
    #     count = np.sum(labels == i)
    #     pct = count / len(labels) * 100
    #     print(f"  Cluster {i}: {count:>3} mahasiswa ({pct:.1f}%)")
    #
    # TODO: Tampilkan rata-rata fitur per cluster
    # print(f"\nRata-rata fitur per cluster:")
    # header = f"{'Cluster':>10}"
    # for name in feature_names:
    #     header += f" | {name:>20}"
    # print(header)
    # print("-" * (12 + 23 * len(feature_names)))
    #
    # for i in range(optimal_k):
    #     mask = labels == i
    #     row = f"{'Cluster ' + str(i):>10}"
    #     for j in range(len(feature_names)):
    #         mean_val = X_original[mask, j].mean()
    #         row += f" | {mean_val:>20.2f}"
    #     print(row)
    #
    # TODO: Silhouette Score keseluruhan
    # sil = silhouette_score(X_scaled, labels)
    # print(f"\nSilhouette Score: {sil:.4f}")
    #
    # TODO: Beri nama cluster berdasarkan karakteristik
    # cluster_names = {}
    # for i in range(optimal_k):
    #     mask = labels == i
    #     avg_ipk = X_original[mask, 0].mean()
    #     avg_jam = X_original[mask, 1].mean()
    #     avg_hadir = X_original[mask, 2].mean()
    #     avg_org = X_original[mask, 3].mean()
    #
    #     # Tentukan nama berdasarkan karakteristik dominan
    #     if avg_ipk >= 3.5 and avg_jam >= 15:
    #         name = "Mahasiswa Berprestasi"
    #     elif avg_org >= 7:
    #         name = "Aktivis Organisasi"
    #     elif avg_ipk >= 2.7:
    #         name = "Mahasiswa Rata-rata"
    #     else:
    #         name = "Mahasiswa Kurang Aktif"
    #
    #     cluster_names[i] = name
    #     print(f"  Cluster {i}: '{name}'")
    #     print(f"    IPK={avg_ipk:.2f}, Jam={avg_jam:.1f}, Hadir={avg_hadir:.1f}%, Org={avg_org:.1f}")
    #
    # return kmeans, labels, cluster_names
    ...


# ============================================
# 5. Prediksi Mahasiswa Baru
# ============================================
def prediksi_mahasiswa_baru(kmeans_model, scaler, feature_names, cluster_names):
    """Prediksi cluster untuk 5 mahasiswa baru.

    Args:
        kmeans_model: Model KMeans yang sudah di-train.
        scaler: StandardScaler yang sudah di-fit.
        feature_names (list): Nama fitur.
        cluster_names (dict): Mapping cluster_id -> nama cluster.
    """
    # TODO: Buat 5 data mahasiswa baru
    # mahasiswa_baru = np.array([
    #     [3.8, 22, 97, 8],    # Berprestasi
    #     [2.0, 3, 50, 1],     # Kurang aktif
    #     [3.1, 13, 80, 5],    # Rata-rata
    #     [2.7, 7, 68, 9],     # Aktivis
    #     [3.5, 18, 90, 3],    # Akademik fokus
    # ])
    #
    # deskripsi = [
    #     "Rajin & aktif organisasi",
    #     "Kurang motivasi",
    #     "Mahasiswa tipikal",
    #     "Fokus organisasi",
    #     "Fokus akademik",
    # ]
    #
    # TODO: Scaling dan prediksi
    # mhs_scaled = scaler.transform(mahasiswa_baru)
    # predictions = kmeans_model.predict(mhs_scaled)
    #
    # TODO: Tampilkan hasil
    # print(f"{'No':>2} | {'Deskripsi':<25} | {'IPK':>4} | {'Jam':>4} | {'Hadir':>5} | {'Org':>3} | {'Cluster':<25}")
    # print("-" * 90)
    # for i, (mhs, desc, pred) in enumerate(zip(mahasiswa_baru, deskripsi, predictions), 1):
    #     cname = cluster_names.get(pred, f"Cluster {pred}")
    #     print(f"{i:>2} | {desc:<25} | {mhs[0]:>4.1f} | {mhs[1]:>4.0f} | {mhs[2]:>5.0f} | {mhs[3]:>3.0f} | {cname:<25}")
    ...


# ============================================
# 6. Analisis & Rekomendasi
# ============================================
def analisis_dan_rekomendasi():
    """Tulis analisis dan rekomendasi per cluster."""
    # TODO: Tulis analisis dan rekomendasi per cluster
    # Jawab pertanyaan berikut:
    # 1. Berapa cluster yang terbentuk? Apakah sesuai ekspektasi?
    # 2. Apa karakteristik utama setiap cluster?
    # 3. Rekomendasi/intervensi apa yang cocok untuk setiap cluster?
    # 4. Apakah Silhouette Score menunjukkan cluster yang baik?
    #
    # Contoh:
    # print("=" * 50)
    # print("ANALISIS & REKOMENDASI PER CLUSTER")
    # print("=" * 50)
    # print("""
    # 1. Jumlah cluster optimal: ...
    #    Silhouette Score: ... (baik/cukup/kurang)
    #
    # 2. Karakteristik per cluster:
    #    - Cluster "Mahasiswa Berprestasi":
    #      IPK tinggi, jam belajar banyak, kehadiran tinggi
    #      Rekomendasi: Program beasiswa, mentor untuk mahasiswa lain
    #
    #    - Cluster "Mahasiswa Rata-rata":
    #      IPK sedang, cukup rajin
    #      Rekomendasi: Motivasi tambahan, study group
    #
    #    - Cluster "Mahasiswa Kurang Aktif":
    #      IPK rendah, jarang hadir
    #      Rekomendasi: Bimbingan akademik, konseling motivasi
    #
    #    - Cluster "Aktivis Organisasi":
    #      IPK sedang, sangat aktif organisasi
    #      Rekomendasi: Manajemen waktu, keseimbangan akademik-organisasi
    #
    # 3. Kesimpulan umum: ...
    # """)
    ...


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Jalankan semua fungsi secara berurutan
    # print("=" * 60)
    # print("TUGAS 3 - CLUSTERING SEGMENTASI MAHASISWA")
    # print("=" * 60)
    #
    # # 1. Buat dataset
    # print("\n=== 1. Membuat Dataset ===")
    # X, feature_names = buat_dataset()
    #
    # # 2. Preprocessing
    # print("\n=== 2. Preprocessing (Scaling) ===")
    # X_scaled, scaler = preprocessing(X)
    #
    # # 3. Elbow Method
    # print("\n=== 3. Elbow Method ===")
    # optimal_k = elbow_method(X_scaled)
    #
    # # 4. K-Means
    # print(f"\n=== 4. K-Means Clustering (K={optimal_k}) ===")
    # kmeans_model, labels, cluster_names = train_kmeans(
    #     X_scaled, X, feature_names, optimal_k
    # )
    #
    # # 5. Prediksi mahasiswa baru
    # print("\n=== 5. Prediksi Mahasiswa Baru ===")
    # prediksi_mahasiswa_baru(kmeans_model, scaler, feature_names, cluster_names)
    #
    # # 6. Analisis
    # print("\n=== 6. Analisis & Rekomendasi ===")
    # analisis_dan_rekomendasi()

    pass

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


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Agar hasil random konsisten
np.random.seed(42)

# 1. Generate Dataset (150 sampel) yang membentuk 3 cluster natural
def generate_student_data():
    # Cluster 1: Berprestasi (IPK tinggi, Belajar tinggi, Kehadiran tinggi)
    c1 = np.random.normal([3.7, 20, 95, 8], [0.2, 2, 3, 1], (50, 4))
    # Cluster 2: Standar (IPK menengah, Belajar menengah, Kehadiran menengah)
    c2 = np.random.normal([3.0, 12, 80, 5], [0.3, 3, 5, 2], (60, 4))
    # Cluster 3: Berisiko (IPK rendah, Belajar rendah, Kehadiran rendah)
    c3 = np.random.normal([2.2, 5, 60, 2], [0.4, 2, 8, 1], (40, 4))
    
    data = np.vstack([c1, c2, c3])
    # Pastikan dalam range yang valid
    data[:, 0] = np.clip(data[:, 0], 1.5, 4.0)
    data[:, 1] = np.clip(data[:, 1], 0, 25)
    data[:, 2] = np.clip(data[:, 2], 40, 100)
    data[:, 3] = np.clip(data[:, 3], 0, 10)
    
    return pd.DataFrame(data, columns=['ipk', 'jam_belajar', 'kehadiran', 'organisasi'])

df = generate_student_data()

# 2. Standardisasi
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# 3. Elbow Method untuk menentukan K optimal
print("===== PENENTUAN K OPTIMAL =====")
inertia = []
silhouette_vals = []
k_range = range(2, 11)

print(f"{'K':<3} | {'Inertia':<12} | {'Silhouette Score'}")
print("-" * 35)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)
    score = silhouette_score(df_scaled, kmeans.labels_)
    silhouette_vals.append(score)
    print(f"{k:<3} | {kmeans.inertia_:<12.2f} | {score:.4f}")

# Berdasarkan Silhouette tertinggi, K=3 biasanya optimal untuk data ini
k_opt = 3 

# 4. Jalankan K-Means dengan K Optimal
kmeans_final = KMeans(n_clusters=k_opt, random_state=42, n_init=10)
df['cluster'] = kmeans_final.fit_predict(df_scaled)

# 5. Profiling Cluster
cluster_names = {
    0: "Mahasiswa Berprestasi",
    1: "Mahasiswa Standar",
    2: "Mahasiswa Berisiko"
}

summary = df.groupby('cluster').agg({
    'ipk': 'mean',
    'jam_belajar': 'mean',
    'kehadiran': 'mean',
    'organisasi': 'mean',
    'cluster': 'count'
}).rename(columns={'cluster': 'jumlah'}).reset_index()

summary['Nama Segment'] = summary['cluster'].map(cluster_names)

print(f"\n===== SEGMENTASI MAHASISWA (K={k_opt}) =====")
print(f"Silhouette Score Keseluruhan: {silhouette_score(df_scaled, kmeans_final.labels_):.4f}")

print("\n--- Profil Cluster ---")
print(f"{'ID':<3} | {'Nama Segment':<22} | {'Jml':<4} | {'IPK':<4} | {'Belajar':<7} | {'Hadir':<6} | {'Org'}")
print("-" * 75)
for _, row in summary.iterrows():
    print(f"{int(row['cluster']):<3} | {row['Nama Segment']:<22} | {int(row['jumlah']):<4} | {row['ipk']:<4.2f} | {row['jam_belajar']:<7.1f} | {row['kehadiran']:<5.1f}% | {row['organisasi']:.1f}")

# 6. Prediksi Data Baru
data_baru = np.array([
    [3.8, 22, 98, 9], # Safriamsah (Ambisius)
    [2.0, 3, 50, 1],  # Malas
    [2.9, 11, 75, 4]  # Rata-rata
])
data_baru_scaled = scaler.transform(data_baru)
preds = kmeans_final.predict(data_baru_scaled)

print("\n--- Prediksi Mahasiswa Baru ---")
for i, p in enumerate(preds):
    print(f"Mahasiswa {i+1}: Masuk ke '{cluster_names[p]}'")

"""
ANALISIS KARAKTERISTIK & REKOMENDASI:
1. Mahasiswa Berprestasi: Fokus akademik & organisasi sangat baik. 
   Saran: Dorong untuk mengikuti riset atau kompetisi nasional/internasional.
2. Mahasiswa Standar: Performa cukup namun belum menonjol. 
   Saran: Berikan motivasi tambahan untuk meningkatkan jam belajar mandiri.
3. Mahasiswa Berisiko: Kehadiran dan IPK di bawah standar. 
   Saran: Perlu bimbingan akademik intensif dan monitoring kehadiran dari dosen wali.
"""

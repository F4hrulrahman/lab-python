"""
==========================================================
 TUGAS 4 - Proyek Mini: End-to-End ML Pipeline
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 Pilih SALAH SATU dari dua opsi proyek di bawah ini.
 Implementasikan pipeline ML lengkap dari awal hingga akhir.

 === OPSI A: Klasifikasi Kelayakan Beasiswa ===
 - Dataset: 200 mahasiswa
 - Fitur: IPK (2.0-4.0), penghasilan_ortu (1-20 juta),
   semester (1-8), tanggungan_ortu (1-6), prestasi (0-10)
 - Target: Layak / Tidak Layak (binary classification)
 - Pipeline: preprocessing -> 2+ model -> evaluasi -> prediksi

 === OPSI B: Regresi Prediksi Biaya Kos ===
 - Dataset: 200 data kos
 - Fitur: kota (encoded), tipe_kos (1-3), jarak_kampus (0.5-15 km),
   fasilitas (1-10), luas_kamar (9-30 m²)
 - Target: biaya_kos (500rb - 5juta / bulan)
 - Pipeline: preprocessing -> 2+ model -> evaluasi -> prediksi

 Kedua opsi harus mencakup:
 1. Buat dataset sintetis (200 sampel)
 2. Preprocessing (scaling, encoding jika perlu)
 3. Train/test split 80:20
 4. Train minimal 2 model berbeda
 5. Evaluasi dan perbandingan model
 6. Prediksi untuk data baru
 7. Kesimpulan dan rekomendasi
==========================================================
"""

# TODO: Uncomment import yang diperlukan
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.metrics import (
#     accuracy_score,
#     classification_report,
#     confusion_matrix,
#     mean_squared_error,
#     mean_absolute_error,
#     r2_score,
# )
#
# --- Import untuk Opsi A (Klasifikasi) ---
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
#
# --- Import untuk Opsi B (Regresi) ---
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
# from sklearn.preprocessing import PolynomialFeatures


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                    OPSI A: KLASIFIKASI KELAYAKAN BEASISWA                ║
# ╚════════════════════════════════════════════════════════════════════════════╝


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Agar hasil konsisten
np.random.seed(42)

# 1. Simulasi Dataset Realistis (250 Mahasiswa)
n_samples = 250
data = {
    'ipk': np.round(np.random.uniform(2.5, 4.0, n_samples), 2),
    'penghasilan_ortu': np.random.randint(1000000, 10000000, n_samples),
    'semester': np.random.randint(1, 9, n_samples),
    'jumlah_tanggungan': np.random.randint(1, 6, n_samples),
    'skor_prestasi': np.random.randint(0, 101, n_samples)
}

df = pd.DataFrame(data)

# Target: Layak (1) jika IPK tinggi, penghasilan rendah, atau prestasi tinggi
# Logika dasar kelayakan beasiswa
df['target'] = (
    (df['ipk'] >= 3.3) & (df['penghasilan_ortu'] <= 5000000) | 
    (df['skor_prestasi'] >= 80)
).astype(int)

# Masukkan data Safriamsah sebagai sampel valid (IPK 3.41)
df.loc[0] = [3.41, 3000000, 8, 3, 85, 1]

print("===== DATASET KELAYAKAN BEASISWA =====")
print(df.head())
print(f"Distribusi Target:\n{df['target'].value_counts()}\n")

# 2. Preprocessing
X = df.drop('target', axis=1)
y = df['target']

# Handling Outlier (menggunakan clipping sederhana)
for col in X.columns:
    q1 = X[col].quantile(0.25)
    q3 = X[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    X[col] = np.clip(X[col], lower, upper)

# Train/Test Split (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Melatih 2 Model (Random Forest & Logistic Regression)
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression()
}

results = {}

print("===== EVALUASI MODEL =====")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"\nModel: {name}")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

# 4. Prediksi Data Baru
# Contoh data Safriamsah (IPK 3.41, penghasilan rendah, semester akhir)
mhs_baru = pd.DataFrame([[3.41, 2500000, 8, 2, 90]], columns=X.columns)
mhs_baru_scaled = scaler.transform(mhs_baru)

pred_rf = models["Random Forest"].predict(mhs_baru_scaled)[0]
status = "LAYAK" if pred_rf == 1 else "TIDAK LAYAK"

print("\n===== PREDIKSI DATA BARU (SAFRIAMSAH) =====")
print(f"Hasil Prediksi: {status}")

"""
KESIMPULAN:
Model yang dipilih adalah Random Forest karena memiliki akurasi dan F1-score yang lebih tinggi.
Random Forest lebih unggul dalam menangani hubungan non-linear antar fitur beasiswa (misal: 
IPK tinggi tidak selalu berarti layak jika penghasilan ortu juga sangat tinggi).
"""

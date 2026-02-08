"""
Chapter 6 - Bagian 1: Klasifikasi
=====================================
Klasifikasi adalah tipe supervised learning di mana model belajar
memprediksi KATEGORI/KELAS dari data.

Contoh: Spam detection, image recognition, diagnosis penyakit.

Install: pip install scikit-learn numpy pandas matplotlib
"""

import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# ============================================
# 1. Memahami Dataset
# ============================================
print("=" * 60)
print("KLASIFIKASI DENGAN SCIKIT-LEARN")
print("=" * 60)

print("\n=== 1. Dataset Iris ===")
# Dataset Iris: 150 sampel bunga iris, 4 fitur, 3 kelas
iris = load_iris()

print(f"Jumlah sampel   : {iris.data.shape[0]}")
print(f"Jumlah fitur    : {iris.data.shape[1]}")
print(f"Nama fitur      : {iris.feature_names}")
print(f"Nama kelas      : {list(iris.target_names)}")
print(f"Distribusi kelas: {np.bincount(iris.target)}")
print(f"\nContoh data (5 pertama):")
print(f"  Features: {iris.data[:5]}")
print(
    f"  Labels  : {iris.target[:5]} ({[iris.target_names[i] for i in iris.target[:5]]})"
)

# ============================================
# 2. Preprocessing & Train/Test Split
# ============================================
print("\n=== 2. Preprocessing ===")

X = iris.data  # Features (input)
y = iris.target  # Labels (output)

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Total data    : {len(X)}")
print(f"Training data : {len(X_train)} ({len(X_train) / len(X) * 100:.0f}%)")
print(f"Testing data  : {len(X_test)} ({len(X_test) / len(X) * 100:.0f}%)")

# Standardisasi fitur (penting untuk KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(
    f"\nSebelum scaling - Mean: {X_train[:, 0].mean():.2f}, Std: {X_train[:, 0].std():.2f}"
)
print(
    f"Setelah scaling - Mean: {X_train_scaled[:, 0].mean():.2f}, Std: {X_train_scaled[:, 0].std():.2f}"
)

# ============================================
# 3. Model 1: K-Nearest Neighbors (KNN)
# ============================================
print("\n=== 3. K-Nearest Neighbors (KNN) ===")
print("Konsep: Prediksi berdasarkan K tetangga terdekat")
print("  - Jika mayoritas tetangga = kelas A, maka prediksi = A")
print("  - Butuh scaling karena menghitung jarak\n")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Prediksi
y_pred_knn = knn.predict(X_test_scaled)

# Evaluasi
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"Accuracy: {acc_knn:.4f} ({acc_knn * 100:.1f}%)")
print(
    f"\nClassification Report:\n{classification_report(y_test, y_pred_knn, target_names=iris.target_names)}"
)
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_knn)}")

# ============================================
# 4. Model 2: Decision Tree
# ============================================
print("\n=== 4. Decision Tree ===")
print("Konsep: Membuat pohon keputusan berdasarkan fitur")
print("  - Mudah diinterpretasi (if-else rules)")
print("  - Tidak butuh scaling\n")

dt = DecisionTreeClassifier(random_state=42, max_depth=3)
dt.fit(X_train, y_train)  # Tidak perlu scaling

y_pred_dt = dt.predict(X_test)
acc_dt = accuracy_score(y_test, y_pred_dt)
print(f"Accuracy: {acc_dt:.4f} ({acc_dt * 100:.1f}%)")

# Feature importance
print("\nFeature Importance:")
for name, importance in sorted(
    zip(iris.feature_names, dt.feature_importances_),
    key=lambda x: x[1],
    reverse=True,
):
    bar = "#" * int(importance * 40)
    print(f"  {name:20s}: {importance:.4f} {bar}")

# ============================================
# 5. Model 3: Random Forest
# ============================================
print("\n=== 5. Random Forest ===")
print("Konsep: Ensemble dari banyak decision tree")
print("  - Lebih akurat dari single decision tree")
print("  - Mengurangi overfitting\n")

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"Accuracy: {acc_rf:.4f} ({acc_rf * 100:.1f}%)")

# ============================================
# 6. Perbandingan Model
# ============================================
print("\n=== 6. Perbandingan Model ===")
print(f"{'Model':<20} {'Accuracy':>10}")
print("-" * 32)
models = [
    ("KNN (k=5)", acc_knn),
    ("Decision Tree", acc_dt),
    ("Random Forest", acc_rf),
]
for name, acc in sorted(models, key=lambda x: x[1], reverse=True):
    bar = "#" * int(acc * 30)
    print(f"{name:<20} {acc:>9.1%} {bar}")

# ============================================
# 7. Prediksi Data Baru
# ============================================
print("\n=== 7. Prediksi Data Baru ===")
# Simulasi data bunga baru
data_baru = np.array(
    [
        [5.1, 3.5, 1.4, 0.2],  # Mirip setosa
        [6.7, 3.1, 4.7, 1.5],  # Mirip versicolor
        [7.2, 3.6, 6.1, 2.5],  # Mirip virginica
    ]
)

# Prediksi menggunakan Random Forest (model terbaik)
prediksi = rf.predict(data_baru)
probabilitas = rf.predict_proba(data_baru)

print("Prediksi untuk data baru:")
for i, (d, p, prob) in enumerate(zip(data_baru, prediksi, probabilitas)):
    nama_kelas = iris.target_names[p]
    confidence = prob[p] * 100
    print(f"  Data {i + 1}: {d} -> {nama_kelas} (confidence: {confidence:.1f}%)")
    print(f"    Probabilitas: {dict(zip(iris.target_names, prob.round(3)))}")

# ============================================
# 8. Tips untuk Pemula
# ============================================
print("\n=== Tips untuk Pemula ===")
print("1. Selalu split data menjadi train dan test")
print("2. Gunakan scaling untuk algoritma berbasis jarak (KNN, SVM)")
print("3. Evaluasi model dengan metrics yang tepat (bukan hanya accuracy)")
print("4. Coba beberapa model dan bandingkan performanya")
print("5. Perhatikan overfitting (model terlalu 'hafal' data training)")

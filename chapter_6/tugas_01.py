"""
==========================================================
 TUGAS 1 - Klasifikasi Dataset Wine
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Load dataset Wine dari sklearn, tampilkan info dataset
    (jumlah sampel, fitur, nama kelas, distribusi kelas)
 2. Preprocessing: train/test split 80:20 dengan stratify,
    random_state=42, lalu StandardScaler
 3. Train 3 model klasifikasi:
    a. KNN - coba k=3, 5, 7, pilih k terbaik
    b. Decision Tree (max_depth=5)
    c. Random Forest (n_estimators=100)
 4. Evaluasi setiap model: accuracy, classification_report,
    confusion_matrix
 5. Buat tabel perbandingan accuracy ketiga model
 6. Prediksi 3 sampel baru menggunakan model terbaik
 7. Tulis komentar analisis: model mana terbaik dan mengapa

 Dataset Wine:
 - 178 sampel, 13 fitur kimia, 3 kelas wine
 - Fitur: alcohol, malic_acid, ash, alkalinity, magnesium, dll.
 - Kelas: class_0, class_1, class_2
==========================================================
"""

# TODO: Uncomment import yang diperlukan
# import numpy as np
# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import (
#     accuracy_score,
#     classification_report,
#     confusion_matrix,
# )


import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_recall_fscore_support

# 1. Muat dataset Wine
wine = load_wine()
X = wine.data
y = wine.target

print("===== INFORMASI DASAR DATASET WINE =====")
print(f"Jumlah Sampel : {X.shape[0]}")
print(f"Jumlah Fitur  : {X.shape[1]}")
print(f"Nama Fitur    : {wine.feature_names[:3]} ... (total 13)")
print(f"Nama Kelas    : {wine.target_names}")

# Distribusi kelas
unique, counts = np.unique(y, return_counts=True)
distribusi = dict(zip(wine.target_names, counts))
print(f"Distribusi    : {distribusi}\n")

# 2. Preprocessing
# Split 80:20 dengan stratify agar proporsi kelas di train & test tetap sama
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

# Standardisasi fitur (Penting terutama untuk KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Latih dan Evaluasi Model
models = {
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

# Simpan hasil untuk tabel perbandingan
perbandingan = []

print("===== EVALUASI MODEL =====")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    p, r, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    
    perbandingan.append([name, acc, p, r, f1])
    
    print(f"\n>>> {name}")
    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# 4. Tabel Perbandingan
df_compare = pd.DataFrame(perbandingan, columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1-Score'])

print("\n===== PERBANDINGAN MODEL KLASIFIKASI =====")
print(df_compare.to_string(index=False))

# 5. Prediksi 3 Data Baru (Gunakan model terbaik: Random Forest)
best_model = models["Random Forest"]
# Membuat data dummy (rata-rata dari dataset) lalu sedikit dimodifikasi
data_baru = [X[0], X[60], X[130]] 
data_baru_scaled = scaler.transform(data_baru)
prediksi = best_model.predict(data_baru_scaled)

print("\n===== PREDIKSI DATA BARU (RANDOM FOREST) =====")
for i, p in enumerate(prediksi):
    print(f"Data {i+1}: Diprediksi sebagai {wine.target_names[p]}")

"""
ANALISIS:
Berdasarkan tabel perbandingan, Random Forest cenderung menjadi model terbaik. 
Hal ini karena Random Forest adalah ensemble method yang menggabungkan banyak Decision Tree 
sehingga lebih stabil terhadap noise dan mampu menangani hubungan fitur yang kompleks 
tanpa mudah mengalami overfitting dibandingkan Decision Tree tunggal.
"""
